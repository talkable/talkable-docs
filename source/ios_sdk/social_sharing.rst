.. _ios_sdk/social_sharing:
.. include:: /partials/common.rst

Social Sharing
==============

Talkable iOS SDK provides the functionality to facilitate sharing offers via social networks.
Older versions of the SDK prior to 1.4.9 used Apple-provided Social.framework to implement
sharing to Facebook and Twitter. Starting with version 1.4.9, usage of Social.framework is
officially deprecated following Apple's decision to deprecate the framework. We still provide
limited support of Social.framework to ensure the stability of legacy implementations. However,
developers are encouraged to use Facebook and Twitter SDKs to enable sharing to these platforms.
This article describes how to use Talkable SDK with social sharing in various scenarios.

Social Sharing from a web-based campaign
----------------------------------------

The default Talkable iOS integration utilizes WebView to display web-based campaign views in your app.
If you have Facebook or Twitter sharing button on your sharing page, Talkable iOS SDK will automatically
detect when the user taps the share button and trigger one of the corresponding delegate methods
(see :ref:`Talkable Delegate <ios_sdk/advanced/delegate>`).

showFacebookShareDialogWithParams:delegate:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: objc

   - (void)showFacebookShareDialogWithParams:(NSDictionary*)params delegate:(id)delegate;

This method is called when user taps the 'Facebook Share' button.
The ``params`` dictionary contains information on the content being shared and will have the following keys:

   * ``TKBLOfferClaimUrlKey`` - the link URL to share
   * ``TKBLShareMessage`` - the message to share

The ``delegate`` param is a delegate object that conforms to Facebook iOS SDK ``SharingDelegate`` protocol.
Pass this object as a ``delegate:`` param when sharing the link using FBSDK to automatically notify Talkable SDK
that sharing was completed successfully. Talkable SDK will then register share with Talkable so that you can see it
in your Talkable Dashboard.

Example
~~~~~~~

.. code-block:: objc

   - (void)showFacebookShareDialogWithParams:(NSDictionary *)params delegate:(id)delegate {
        FBSDKShareLinkContent *content = [[FBSDKShareLinkContent alloc] init];
        content.contentURL = [NSURL URLWithString:[params objectForKey:TKBLOfferClaimUrlKey]];
        [FBSDKShareDialog showFromViewController:self
                                     withContent:content
                                        delegate:delegate];
    }


showFacebookShareDialogWithParams:completionHandler:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: objc

   - (void)showFacebookShareDialogWithParams:(NSDictionary*)params completion:(void (^)())completionHandler;

This method is also called when the user taps the 'Facebook Share' button, but instead of ``delegate`` param it
provides the ``completionHandler`` block that should be called when sharing is completed successfully. Use
this method if you already have a delegate object that you use for Facebook sharing.
Pass the ``completionHandler`` block to the delegate object and call it in your
``sharer:didCompleteWithResults:`` method.

Example
~~~~~~~

.. code-block:: objc

   - (void)showFacebookShareDialogWithParams:(NSDictionary *)params completion:(void (^)())completionHandler {
       MyFBSDKDelegateClass* delegate = [self myFBSDKDelegate];
       delegate.talkableCompletionHandler = completionHandler;
       FBSDKShareLinkContent *content = [[FBSDKShareLinkContent alloc] init];
       content.contentURL = [NSURL URLWithString:[params objectForKey:TKBLOfferClaimUrlKey]];
       [FBSDKShareDialog showFromViewController:self
                                    withContent:content
                                       delegate:delegate];
   }

   ...

   @implementation MyFBSDKDelegateClass

   @synthesize talkableCompletionHandler;

   - (void)sharer:(id)sharer didCompleteWithResults:(NSDictionary<NSString *, id> *)results {
    if ((_talkableCompletionHandler) != nil)
      _talkableCompletionHandler();
   }

   @end


showTwitterShareDialogWithParams:completionHandler:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: objc

   - (void)showTwitterShareDialogWithParams:(NSDictionary*)params completion:(void (^)())completionHandler;

This method is called when the user taps the Twitter Share button. The ``params`` and ``completionHandler``
attributes are analogous to the previous method.

Example
~~~~~~~

.. code-block:: objc

   - (void)showTwitterShareDialogWithParams:(NSDictionary *)params completion:(void (^)())completionHandler {
      TWTRComposer *composer = [[TWTRComposer alloc] init];

      [composer setText:[params objectForKey:TKBLShareMessage]];

      [composer showFromViewController:self completion:^(TWTRComposerResult result) {
          if (result == TWTRComposerResultDone) {
               completionHandler();
          }
      }];
   }

Legacy Sharing using Social.framework
-------------------------------------

Prior to v1.4.9, TalkableSDK used Social.framework to automatically display Facebook and Twitter sharing dialog
when the user taps on a corresponding button. This way of sharing relied on functionality built into iOS and did not
require the use of additional SDKs. Staring with iOS 11, Apple deprecated this way of sharing and now requires
developers to utilize frameworks provided by Facebook and Twitter.
While Social.framework is officially deprecated, Talkable SDK still supports a limited subset of its functionality
to ensure a seamless transition to new implementations.

* If `Talkable Delegate <ios_sdk/advanced/delegate>` doesn't implement either of the two Facebook methods,
  TalkableSDK will attempt to trigger Facebook share via Social.framework.
* Facebook sharing popup will only be displayed if Facebook app is installed on a customer's phone, otherwise it will
  silently fail.
* Twitter sharing is not supported by Social.framework anymore.

.. note::

   Talkable iOS SDK v1.4.9 features improved support of legacy Facebook sharing via Social.framework. If you are having trouble
   with your current implementation, please upgrade to the latest version. Note that we can only try to provide the best
   transitioning experience, and this fallback should not be regarded as a permanent solution. We encourage developers to switch
   to delegate methods for social sharing.

Social Sharing from a native campaign
-------------------------------------

The methods documented above are designed to work with web-based campaigns only. If you have integrated using our API,
please refer to the :ref:`Sharing <ios_sdk/api_integration/sharing>` section of the Native Integration page.
