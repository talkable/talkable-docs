.. _ios_sdk/advanced:
.. include:: partials/common.rst

Advanced Usage
==============

Specify a custom campaign tag
-----------------------------

By default if no campaign tag was specified, SDK uses `ios-invite` and `ios-post-purchase` tags for :ref:`Standalone <ios_sdk/integration/standalone>` and
:ref:`Post Purchase <ios_sdk/integration/post_purchase>` campaigns. But you can explicitly specify your own tag in this way:

.. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    // ...
    [[Talkable manager] registerOrigin:TKBLAffiliateMember params:@{TKBLCampaignTags: @"your-custom-tag"}];

.. _ios_sdk/advanced/delegate:

Implement TalkableDelegate
--------------------------

1. Assign your `ViewController` or other object as Talkable delegate by using the following code:

   .. code-block:: objc

    [[Talkable manager] setDelegate: yourObjectConformsToTalkableDelegateProtocol];

2. Take control of presenting offers to your users. Use the next two delegate methods to prevent
   or give an instruction as to where you want that offer to be displayed:

   .. code-block:: objc

    - (BOOL)shouldPresentTalkableOfferViewController:(UIViewController*)controller;
    - (UIViewController*)viewControllerForPresentingTalkableOfferViewController;

3. Customize ViewContoller title by implementing the method below. By default, title of offer page is used.

   .. code-block:: objc

    - (NSString*)titleForTalkableOfferViewController:(UIViewController*)controller;

   .. note::

    You can modify page title on a Talkable Site during campaign development.

4. Present offers to your users by yourself by handling request url or webView after origin was created.

   .. code-block:: objc

    - (void)didRegisterOrigin:(TKBLOriginType)type withURL:(NSURL*)url;
    - (void)didRegisterOrigin:(TKBLOriginType)type withWebView:(WKWebView*)webView;

   .. note::

    Talkable SDK assigns itself to WKWebView navigation delegate. Changing WKWebView navigation delegate
    may break some functionality so we strictly recommend not doing this.

5. Manage cases where origin wasn't created or offer hasn't been presented.

   .. code-block:: objc

    - (void)registerOrigin:(TKBLOriginType)type didFailWithError:(NSError*)error;

   .. note::

    `userInfo` may contain detailed information about the error.

6. Receive notification when the user taps Facebook or Twitter sharing button in the WebView and trigger
   corresponding sharing view.

   .. code-block:: objc

      - (void)showFacebookShareDialogWithParams:(NSDictionary*)params delegate:(id)delegate;
      - (void)showFacebookShareDialogWithParams:(NSDictionary*)params completion:(void (^)())completionHandler;
      - (void)showTwitterShareDialogWithParams:(NSDictionary*)params completion:(void (^)())completionHandler;

   .. note::

      See :ref:`Social Sharing <ios_sdk/social_sharing>` for details.

.. _ios_sdk/advanced/notifications:

Notifications
-------------

Subscribe to notifications that Talkable SDK publish and be aware of everything that happens around your campaigns.

1. Receive the coupon given to your users:

   .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    // ...
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(couponReceived:) name:TKBLDidReceiveCouponCode object:nil];
    // ...
    - (void)couponReceived:(NSNotification*)ntf {
      // Your logic here
    }

2. Catch every message from presented offer:

   .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    // ...
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(publishMessageNotification:) name:TKBLDidPublishMessageNotification object:nil];
    // ...
    - (void)publishMessageNotification:(NSNotification*)ntf {
      if ([[[ntf userInfo] objectForKey:TKBLMessageNameKey] isEqualToString:TKBLMessageOfferLoaded]) {
        // Your logic here
      }
    }

Available messages:
  - TKBLMessageOfferLoaded
  - TKBLMessageOfferClose
  - TKBLMessageCouponIssued

Contacts Import
---------------

It is possible to import contacts from a device with the SDK, so they will be accessible at the Share page with JavaScript.
The button at the Share page for contacts importing should have ``class="js-import-contacts"`` property.

Also, contacts usage description is required on iOS 10+ devices. It should be described under the ``NSContactsUsageDescription`` key
in the ``Info.plist`` file of your app. This message will be shown when asking for contacts permissions.

.. code-block:: xml

    <key>NSContactsUsageDescription</key>
    <string>Share the offer with your Friends from contacts</string>

  .. note::

    Talkable SDK asks for the contacts permissions dynamically only when "contacts import" functionality is implemented
    in the campaign and Advocate presses the corresponding button at the Share page for the first time.

Debugging
---------

See all debugging information in your console which can help you to understand what is going wrong:

.. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    // ...
    [Talkable manager].debug = YES;
