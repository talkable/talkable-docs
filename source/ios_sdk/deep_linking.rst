.. _ios_sdk/deep_linking:
.. include:: /partials/common.rst

Deep linking integration
========================

Talkable iOS SDK supports third party deep linking providers such as GetSocial, Branch.io, and Firebase. Talkable can use deep linking functionality to track app installations and reward your advocates and friends for installing your mobile app on their phones.

Deep linking services provide a special referral link that can be given to Advocates to be shared with their friends. Once opened on a Friend's mobile device, this link will not only redirect them to App Store to install the app, but also track that the app was installed using a referral link. The deep link can also be used to send a friend to a specific place in the app once it's installed and opened for the first time, show them personalized messages, and more.

1. Create a deep link
~~~~~~~~~~~~~~~~~~~~~

Use your deep linking service dashboard to create a deep link and connect it to your app. Copy the deep link URL.

2. Set up your Talkable campaign
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the deep link URL as Friend Destination URL in your Talkable campaign,
appending following GET parameters: ``?talkable_visitor_uuid={{ visitor_uuid }}&talkable_visitor_offer_id={{ friend_offer.id }}``.

The end result should look like one of the following examples:

.. code-block:: none

    https://your-app.gsc.im/1/your-link-name?talkable_visitor_uuid={{ visitor_uuid }}&talkable_visitor_offer_id={{ friend_offer.id }}

    https://example.app.link/fzmLEhobLD?talkable_visitor_uuid={{ visitor_uuid }}&talkable_visitor_offer_id={{ friend_offer.id }}

.. note::

    All major deep linking providers support passing additional GET parameters to the deep link.
    This functionality is used to pass friend's identifying information to the TalkableSDK in your iOS app.
    To use this functionality with Firebase, refer to this document: `Manually constructing a Dynamic Link URL`_.

3. Pass deep linking params to TalkableSDK
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve deep linking params as described in your deep linking provider's documentation
and pass these params to the Talkable SDK using ``handleOpenURL:`` or ``handleURLParams:`` method.

Use ``handleURLParams:`` method if you have a ``NSDictionary`` with params in a custom handler (Branch.io, GetSocial).

.. code-block:: objc

    // For Branch.io

    [[Branch getInstance] initSessionWithLaunchOptions:launchOptions andRegisterDeepLinkHandler:^(NSDictionary *params, NSError *error) {
        [[Talkable manager] handleURLParams:params];
    }];

    // For GetSocial

    [GetSocial referralDataWithSuccess:^(GetSocialReferralData * _Nullable referralData) {
        [[Talkable manager] handleURLParams:[referralData linkParams]];
    } failure:^(NSError * _Nonnull error) {}];

Use ``handleOpenURL:`` method if you handle deep link as ``NSURL`` using the standard
``application:openURL:options:`` method (Firebase).

.. code-block:: objc

    // For Firebase

    - (BOOL)application:(UIApplication *)app
                openURL:(NSURL *)url
                options:(NSDictionary<NSString *, id> *)options {
                    [[Talkable manager] handleOpenURL:url];
                }

Calling either of these methods will register the app installation event in Talkable and complete the referral cycle.
You can then use :ref:`retrieveRewardsWithHandler: <ios_sdk/api_integration>` method to check for rewards or subscribe
to a corresponding :ref:`notification <ios_sdk/advanced/notifications>`.


.. _Manually constructing a Dynamic Link URL: https://firebase.google.com/docs/dynamic-links/create-manually