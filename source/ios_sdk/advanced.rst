.. _ios_sdk/advanced:
.. include:: /partials/common.rst

Advanced Usage
==============

Specify a custom campaign tag
-----------------------------

By default if no campaign tag was specified SDK uses `ios-invite` and `ios-post-purchase` tags for :ref:`Standalone <ios_sdk/integration/standalone>` and
:ref:`Post Purchase <ios_sdk/integration/post_purchase>` campaigns. But you can explicitly specify your own tag in this way:

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    ...
    [[Talkable manager] registerOrigin:TKBLAffiliateMember params:@{TKBLCampaignTags: @"your-custom-tag"}];
    ...

Implement TalkableDelegate
--------------------------

1. Assign your `ViewController` or other object as Talkable delegate by following code:

  .. code-block:: objc

    [[Talkable manager] setDelegate: yourObjectConformsTalkableDelegateProtocol];

2. Take control of presenting offers to your users. Use next two delegate methods to prevent or give an instruction where you want that offer will be displayed:

  .. code-block:: objc

    - (BOOL)shouldPresentTalkableOfferViewController:(UIViewController*)controller;
    - (UIViewController*)viewControllerForPresentingTalkableOfferViewController;

3. Customize ViewContoller title by implementing method below. By default title of offer page is used.

  .. code-block:: objc

    - (NSString*)titleForTalkableOfferViewController:(UIViewController*)controller;

  .. note::

    You can modify page title on Talkable Site during campaign developing.

4. Present offers to your users by yourself by handling request url or webView after origin was created.

  .. code-block:: objc

    - (void)didRegisterOrigin:(TKBLOriginType)type withURL:(NSURL*)url;
    - (void)didRegisterOrigin:(TKBLOriginType)type withWebView:(WKWebView*)webView;

  .. note::

    Talkable SDK assigns itself to WKWebView navigation delegate. Changing WKWebView navigation delegate may brokes some functionality so we strictly not recommend to do this.

Notifications
-------------

Subscribe to notifications that Talkable SDK publish and be aware of everything that happens around your campaigns.

1. Receive the coupon given to your users:

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    ...
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(couponReceived:) name:TKBLDidReceiveCouponCode object:nil];
    ...
    - (void)couponReceived:(NSNotification*)ntf {
      // Your logic here
    }
    ...

2. Catch every message from presented offer:

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    ...
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(publishMessageNotification:) name:TKBLDidPublishMessageNotification object:nil];
    ...
    - (void)publishMessageNotification:(NSNotification*)ntf {
      if ([[[ntf userInfo] objectForKey:TKBLMessageNameKey] isEqualToString:TKBLMessageOfferLoaded]) {
        // Your logic here
      }
    }
    ...

  Available messages:

  - TKBLMessageOfferLoaded
  - TKBLMessageOfferClose
  - TKBLMessageCouponIssued

Debugging
---------

See all debugging information in your console which can help you to realise what is going wrong:

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    ...
    [Talkable manager].debug = YES;

.. container:: hidden

   .. toctree::
