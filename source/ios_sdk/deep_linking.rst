.. _ios_sdk/deep_linking:
.. include:: /partials/common.rst

Deep Linking
============

Talkable uses GetSocial.im technology to provide installation attribution and deep linking functionality with its iOS SDK.
This guide describes how to configure your Talkable campaign for deep linking and add support for it to your iOS app.

Requirements
------------

* TalkableSDK supports iOS 8.0 or greater.
* TalkableSDK version 1.5.0 or greater is required for deep linking support.
* TalkableSDK requires the following frameworks to be added to the *Link Binary With Libraries* section of your target:

  - `AddressBook.framework`
  - `MessageUI.framework`
  - `SafariServices.framework`
  - `Security.framework`
  - `Social.framework`
  - `WebKit.framework`

Automated Installation
----------------------

Talkable provides the installation script that will add the Talkable and GetSocial SDKs
to your project as well as perform all the necessary configuration.

1. Download `the installation script`_ and unzip it into your project's root folder.
2. Open Terminal, ``cd`` into your project's root folder and execute the following command:

    .. code-block:: bash

      /bin/bash talkable.sh --site-id=YOUR_TALKABLE_SITE_ID --api-key=YOUR_TALKABLE_PUBLIC_API_KEY --getsocial-app-id=YOUR_GETSOCIAL_APP_ID

    .. note::

      Replace ``YOUR_TALKABLE_SITE_ID`` with your real Talkable Site ID, ``YOUR_TALKABLE_PUBLIC_API_KEY`` with your public API key,
      and ``YOUR_GETSOCIAL_APP_ID`` with your GetSocial App ID.

      All this information can be found on your site *Dashboard* at https://admin.talkable.com

      The script creates a backup of your ``project.pbxproj`` file before making any changes and stores it in your ``.xcodeproj`` folder.
      If anything goes wrong during the installation, you can always restore your project configuration from this backup.
      We suggest adding ``.backup`` files to your SCM ignore list.


6. Import the framework's header file and initialize Talkable framework by calling ``[Talkable manager]`` when your app finishes launching.

    .. code-block:: objc

      #import <TalkableSDK/Talkable.h>

      - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
      {
          [Talkable manager];
          ...
      }

Manual Installation
-------------------

Alternatively, you can add Talkable and GetSocial frameworks to your project manually.

1. Download `TalkableSDK v1.5.0`_.
2. Add the ``TalkableSDK.framework`` to your Xcode project.
3. Drag ``TalkableSDK.framework`` to the *Embedded Binaries* section of your target.
4. Import the framework's header file.

    .. code-block:: objc

      #import <TalkableSDK/Talkable.h>

5. Initialize Talkable in your ``application:didFinishLaunchingWithOptions:`` method.

    .. code-block:: objc

      [[Talkable manager] setApiKey:@"YOUR_TALKABLE_PUBLIC_API_KEY" andSiteSlug:@"YOUR_TALKABLE_SITE_ID"];

6. Register the Talkable URL scheme.

  - Define ``tkbl-YOUR_TALKABLE_SITE_ID`` URL Scheme in your Info.plist file:

    .. code-block:: xml

      <key>CFBundleURLTypes</key>
      <array>
        <dict>
          <key>CFBundleURLSchemes</key>
          <array>
            <string>tkbl-YOUR_TALKABLE_SITE_ID</string>
          </array>
        </dict>
      </array>

  - Add ``tkbl-YOUR_TALKABLE_SITE_ID`` and ``fb-messenger`` to the list of query schemes supported by your app:

    .. code-block:: xml

      <key>LSApplicationQueriesSchemes</key>
      <array>
        <string>tkbl-YOUR_TALKABLE_SITE_ID</string>
        <string>fb-messenger</string>
      </array>

    .. note::

      Replace ``YOUR_TALKABLE_SITE_ID`` with your real Talkable Site ID, which can be found
      on your site *Dashboard* at https://admin.talkable.com

7. Add the GetSocial Core framework to your project by following the `GetSocial iOS SDK Manual Integration Guide`_.

.. note::

  You don't need to include or call GetSocial framework explicitly for deep linking to work.
  The TalkableSDK will detect the GetSocial framework if it's present and will handle deep linking automatically.

.. _`the installation script`: https://talkable-downloads.s3.amazonaws.com/ios-sdk/talkable_ios_sdk_installer.zip
.. _`TalkableSDK v1.5.0`: https://talkable-downloads.s3.amazonaws.com/ios-sdk/talkable_ios_sdk_1.5.0.zip
.. _`GetSocial iOS SDK Manual Integration Guide`: https://docs.getsocial.im/knowledge-base/manual-integration/ios/