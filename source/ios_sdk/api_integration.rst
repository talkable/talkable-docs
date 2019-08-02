.. _ios_sdk/api_integration:
.. include:: /partials/common.rst

Native Integration via API
==========================

Talkable provides an API that can be utilized to implement a fully native referral program interface if you don't want to use
included WKWebView-based functionality. Below are the methods necessary to integrate the Talkable referral loop into your iOS app.

1. Create an Origin
-------------------

The Origin is a user event (e.g. a purchase or simply opening the app) that initiates the referral chain.
Create an Origin to retrieve an Offer and display it to an :ref:`Advocate <campaigns>`.

To create an Origin, make a request to :ref:`Origins <api_v2/origins>` endpoint using the ``createOrigin:withHandler:`` method.
If the request is successful, the ``handler`` block will receive attributes of created Origin and :ref:`Offer <api_v2/offers>` entities.

.. code-block:: objc

  NSDictionary* originParams = @{
      TKBLOriginTypeKey: TKBLOriginTypePurchase,
      TKBLOriginDataKey: @{
          TKBLPurchaseEmailKey: @"test@example.com",
          TKBLPurchaseSubtotalKey: @"17.43",
          TKBLPurchaseOrderNumberKey: @"100125",
          @"campaign_tags": @"your-campaign-tag"
      }
  };

  [[Talkable manager] createOrigin:originParams withHandler:^(NSDictionary* response, NSError* error) {
      NSDictionary* offerParams = [response objectForKey:TKBLOfferKey];
      NSDictionary* claimLinks = [offerParams objectForKey:@"claim_links"];
  }];


.. _ios_sdk/api_integration/sharing:

2. Create a Share
-----------------

Sharing an Offer is the next step in the referral chain. You will need the ``short_url_code`` of the Offer obtained from a previous request.

.. code-block:: objc

  NSString* shortUrlCode = [offerParams objectForKey:TKBLOfferShortUrlCodeKey];

Native sharing
~~~~~~~~~~~~~~

The ``nativeShare:`` method will display a native iOS sharing dialog. When content is shared,
the share will be automatically registered with Talkable and reflected on your dashboard.

.. code-block:: objc

  UIActivityViewController* sheet = [[Talkable manager] nativeShare:@{
      TKBLOfferShortUrlCodeKey: shortUrlCode,
      TKBLOfferClaimUrlKey: [claimLinks objectForKey:TKBLShareChannelOther]
  }];

  [self presentViewController:sheet animated:YES completion:^{}];

Social sharing
~~~~~~~~~~~~~~

Use frameworks provided by social networks to share your offer. Upon a successful share,
call the ``createSocialShare:channel:withHandler:`` method to register the share with Talkable and
create a :ref:`Share <api_v2/shares>` record.

.. code-block:: objc

  [[Talkable manager] createSocialShare:shortUrlCode channel:TKBLShareChannelOther withHandler:^(NSDictionary* response, NSError* error) {
      NSDictionary* rewardParams = [response objectForKey:@"reward"];
  }];

.. raw:: html

  <h4>Facebook example</h4>

.. code-block:: objc

   MyFBSDKDelegateClass* delegate = [self myFBSDKDelegate];
   delegate.shortUrlCode = shortUrlCode;
   FBSDKShareLinkContent *content = [[FBSDKShareLinkContent alloc] init];
   content.contentURL = [NSURL URLWithString:[params objectForKey:[claimLinks objectForKey:TKBLShareChannelFacebook]]];
   [FBSDKShareDialog showFromViewController:self
                                withContent:content
                                   delegate:delegate];

   ...

   @implementation MyFBSDKDelegateClass

   @synthesize shortUrlCode;

   - (void)sharer:(id)sharer didCompleteWithResults:(NSDictionary<NSString *, id> *)results {
    if (_shortUrlCode != nil)
       [[Talkable manager] createSocialShare:_shortUrlCode
                                     channel:TKBLShareChannelFacebook
                                 withHandler:^(NSDictionary* response, NSError* error) {...}];
   }

   @end

.. raw:: html

  <h4>Twitter example</h4>

.. code-block:: objc

   TWTRComposer *composer = [[TWTRComposer alloc] init];
   [composer setText:[params objectForKey:TKBLShareMessage]];
   [composer showFromViewController:self completion:^(TWTRComposerResult result) {
     if (result == TWTRComposerResultDone) {
       [[Talkable manager] createSocialShare:shortUrlCode
                                     channel:TKBLShareChannelTwitter
                                 withHandler:^(NSDictionary* response, NSError* error) {...}];
     }
   }];

.. note::

  This method will be called automatically when you use ``socialShare:`` or ``nativeShare:`` methods.

Legacy social sharing
~~~~~~~~~~~~~~~~~~~~~

3. The legacy ``socialShare:`` method was used prior to v1.4.9 and is provided for backwards compatibility.
   It will attempt to display a sharing dialog directly using the deprecated Social.framework.
   Only the Facebook sharing channel is currently supported.

   .. code-block:: objc

     SLComposeViewController* sheet = [[Talkable manager] socialShare:@{
       TKBLShareChannel:TKBLShareChannelFacebook,
       TKBLOfferClaimUrlKey:[claimLinks objectForKey:TKBLShareChannelFacebook],
       TKBLShareMessage:@"Personalized message",
       TKBLOfferShortUrlCodeKey:shortUrlCode
     }];

     [self presentViewController:sheet animated:YES completion:^{}];

   .. warning::

      Starting with v1.4.9, this method is deprecated and offers only limited Facebook sharing support.
      Native sharing or custom implementation based on Facebook/Twitter SDK should be used instead.
      See :ref:`Social Sharing <ios_sdk/social_sharing>` for details.


Email Share
~~~~~~~~~~~

To share an Offer via email, simply use the ``createEmailShare:recipients:withParams:andHandler:`` method to send an API request.
Talkable will send the emails for you. You will need to provide an interface for the user to specify recipients' email addresses, a subject, and a personal message.

.. code-block:: objc

  NSString* recipients = @"customer@example.com,elon@musk.com"; // comma separated email addresses
  NSDictionary* emailShareParams = @{
      @"subject": @"Custom Email Subject",
      @"body": @"Personal message that will be added to the email body",
      @"reminder": NO // Whether Talkable should send a reminder email later
  };

  [[Talkable manager] createEmailShare:shortUrlCode recipients:recipients withParams:emailShareParams andHandler:^(NSDictionary* response, NSError* error) {
      // process delivery stats
  }];

3. Check for Reward
-------------------

If a Talkable campaign is configured to give a reward to the Advocate just for sharing, the API call to create a :ref:`Share <api_v2/shares>`
will return a :ref:`Reward <api_v2/rewards>` you can display immediately. In most cases, however, the Advocate will receive a reward after
a Friend responds to a shared link, e.g. makes a purchase.
To check whether the current user has any outstanding rewards, use the ``retrieveRewardsWithHandler:`` method.

.. code-block:: objc

  [[Talkable manager] retrieveRewardsWithHandler:^(NSDictionary* response, NSError* error) {
      NSArray *rewards = (NSArray *)[response objectForKey:@"rewards"];
  }];

Extra Functionality
-------------------

Retrieve an Offer by Short Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to access an Offer for the Origin you've created earlier, store the offer's ``short_url_code`` and then use ``retrieveOffer:withHandler:`` method
to fetch the Offer.

.. code-block:: objc

  [[Talkable manager] retrieveOffer:shortUrlCode withHandler:^(NSDictionary* response, NSError* error) {
      NSDictionary* offerParams = [response objectForKey:TKBLOfferKey];
  }];

Alternatively, you can subscribe to a ``TKBLDidReceiveReward`` notification as described in the :ref:`Advanced Usage <ios_sdk/advanced/notifications>` section.

.. container:: hidden

   .. toctree::
