.. _ios_sdk/api_integration:
.. include:: /partials/common.rst

Native Integration via API
==========================

Talkable provides API that can be utilized to implement fully native referral program interface if you don't want to use
included web-based views. Below are the methods necessary to integrate Talkable referral loop into your iOS app.

1. Create an Origin
-------------------

The Origin is an user event (e.g. a purchase or simply opening the app) that initiates the referral chain.
Create an Origin to retrieve an Offer and display it to an :ref:`Advocate <campaigns>`.

To create an Origin, make a request to :ref:`Origins <api_v2/origins>` endpoint using the `createOrigin:withHandler:` method.
If the request is successful, the `handler` block will receive attributes of created Origin and :ref:`Offer <api_v2/offers>` entities.

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
  }];


2. Create a Share
-----------------

Sharing an Offer is the next step in the referral chain.

Social Share
~~~~~~~~~~~~

Talkable SDK provides several ways to share an Offer using social media channels.

1. `socialShare:` method will display a sharing dialog directly. Supported channels are Facebook and Twitter.

    .. code-block:: objc

      SLComposeViewController* sheet = [[Talkable manager] socialShare:@{
        TKBLShareChannel:TKBLShareChannelTwitter,
        TKBLOfferClaimUrlKey:[claimLinks objectForKey:TKBLShareChannelTwitter],
        TKBLShareMessage:@"Personalized message",
        TKBLShareImage:@"Image URL as NSString", //You can also pass an UIImage
        TKBLOfferShortUrlCodeKey:shortUrlCode
      }];

      [self presentViewController:sheet animated:YES completion:^{}];

2. `nativeShare:` method will display a native iOS sharing dialog.

    .. code-block:: objc

      NSString* shortUrlCode = [offerParams objectForKey:TKBLOfferShortUrlCodeKey];
      NSDictionary* claimLinks = [offerParams objectForKey:@"claim_links"];

      UIActivityViewController* sheet = [[Talkable manager] nativeShare:@{
          TKBLOfferShortUrlCodeKey: offerShortUrlCode,
          TKBLOfferClaimUrlKey: [claimLinks objectForKey:TKBLShareChannelOther]
      }];

      [self presentViewController:sheet animated:YES completion:^{}];

3. Implement your own way for the Advocate to share the link. On successful share,
call the `createSocialShare:channel:withHandler:` method to sync the share with Talkable and create a :ref:`Share <api_v2/shares>` record.

    .. code-block:: objc

      [[Talkable manager] createSocialShare:shortUrlCode channel:TKBLShareChannelOther withHandler:^(NSDictionary* response, NSError* error) {
          NSDictionary* rewardParams = [response objectForKey:@"reward"];
      }];

Email Share
~~~~~~~~~~~

To share an Offer via email, simply use the `createEmailShare:recipients:withParams:andHandler:` method to send an API request.
Talkable will send the emails for you. You will need to provide an interface for the user to specify recipients' email addresses
and add an optional personal message.

.. code-block:: objc

  NSString* recipients = @"customer@example.com,elon@musk.com"; //comma separated email addresses
  NSDictionary* emailShareParams = @{
      @"subject": @"Custom Email Subject",
      @"body": @"Personal message that will be added to the email body",
      @"reminder": @NO // Whether Talkable should send a reminder email later
  };

  [[Talkable manager] createEmailShare:shortUrlCode recipients:recipients withParams:emailShareParams andHandler:^(NSDictionary* response, NSError* error) {
      // process delivery stats
  }];

3. Check for Reward
-------------------

If a Talkable campaign is configured to give a reward to Advocate just for sharing, the API call to create a :ref:`Share <api_v2/shares>`
will return a :ref:`Reward <api_v2/rewards>` you can display immediately. In most cases, however, Advocate will receive a reward after
a Friend responds to a shared link, e.g. makes a purchase.
To check whether the current user has any outstanding rewards, use the `retrieveRewardsWithHandler:` method.

.. code-block:: objc

  [[Talkable manager] retrieveRewardsWithHandler:^(NSDictionary* response, NSError* error) {
      NSArray *rewards = (NSArray *)[response objectForKey:@"rewards"];
  }];

Extra Functionality
-------------------

Retrieve an Offer by Short Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to access an Offer for the Origin you've created earlier, store the offer's `short_url_code` and then use `retrieveOffer:withHandler:` method
to fetch the Offer.

.. code-block:: objc

  [[Talkable manager] retrieveOffer:shortUrlCode withHandler:^(NSDictionary* response, NSError* error) {
      NSDictionary* offerParams = [response objectForKey:TKBLOfferKey];
  }];

Alternatively, you can subscribe to a `TKBLDidReceiveReward` notification as described in the :ref:`Advanced Usage <ios_sdk/advanced/notifications>` section.

.. container:: hidden

   .. toctree::
