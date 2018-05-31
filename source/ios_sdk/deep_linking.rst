.. _ios_sdk/deep_linking:
.. include:: /partials/common.rst

Deep Linking
============

Talkable uses GetSocial.im technology to provide installation attribution and deep linking functionality with its iOS SDK.
This guide describes how to configure your Talkable campaign for deep linking and add support for it to your iOS app.

.. note::

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

Talkable provides the installation script that will add Talkable and GetSocial SDK to your project as well as perform all
necessary configuration.

1. Download `the installation script`_ and unzip it into your project's root folder.
2. Open your XCode project settings, select the target you want to modify and go to *Build Phases* tab.
3. Create a new *Run Script* phase with content:

  .. code-block:: bash

    "$PROJECT_DIR/talkable.sh" --version=1.5.0 --site-id=YOUR_SITE_ID --api-key=YOUR_TALKABLE_PUBLIC_API_KEY --getsocial-app-id=YOUR_GETSOCIAL_APP_ID

  .. note::

    Replace ``YOUR_SITE_SLUG`` with your real site slug, ``YOUR_TALKABLE_PUBLIC_API_KEY`` with your public API key,
    and ``YOUR_GETSOCIAL_APP_ID`` with your GetSocial App ID.

    All this information can be found on your site *Dashboard* at https://admin.talkable.com

4. Move the new *Run Script* phase before the *Compile Sources* phase.
5. Build your project.

.. note::

  Initial configuration performed by the installation script may result in build stopping with *Build cancelled* status.
  If this happens, simply re-run the build. This might happen up to 2 times, as the script has to configure two frameworks.
  This does not mean the installation was unsuccessful. Any errors raised by the script will result in *Build failed*
  status.

  The script creates a backup of your ``project.pbxproj`` file before making any changes and stores it in your ``.xcodeproj`` folder.
  If anything goes wrong during the installation, you can always restore your project configuration from this backup.
  We suggest adding ``.backup`` files to your SCM ignore list.

Manual Installation
-------------------

Alternatively you can add Talkable and GetSocial frameworks to your project manually.

1. Download `TalkableSDK v1.5.0`_.
2. Add the ``TalkableSDK.framework`` to your Xcode project.
3. Drag ``TalkableSDK.framework`` to the *Embedded Binaries* section of your target.
4. Import the framework's header file.

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>

5. Initialize Talkable in your `application:didFinishLaunchingWithOptions:` method.

  .. code-block:: objc

    [[Talkable manager] setApiKey:@"YOUR_TALKABLE_PUBLIC_API_KEY" andSiteSlug:@"YOUR_SITE_SLUG"];

6. Register the Talkable URL scheme.

  - Define `tkbl-YOUR_SITE_SLUG` URL Scheme in your Info.plist file:

    .. code-block:: xml

      <key>CFBundleURLTypes</key>
      <array>
        <dict>
          <key>CFBundleURLSchemes</key>
          <array>
            <string>tkbl-YOUR_SITE_SLUG</string>
          </array>
        </dict>
      </array>

  - Add `tkbl-YOUR_SITE_SLUG` and `fb-messenger` to the list of query schemes supported by your app:

    .. code-block:: xml

      <key>LSApplicationQueriesSchemes</key>
      <array>
        <string>tkbl-YOUR_SITE_SLUG</string>
        <string>fb-messenger</string>
      </array>

  .. note::

    Replace ``YOUR_SITE_SLUG`` with your real site slug, which can be found
    on your site *Dashboard* at https://admin.talkable.com


7. Add the GetSocial Core framework to your project by following the `GetSocial iOS SDK Manual Integration Guide`_.

.. note::

  You don't need to include or call GetSocial framework explicitly for deep linking to work.
  TalkableSDK will detect GetSocial framework if it's present and handle deep linking automatically.

.. _`the installation script`: https://talkable-downloads.s3.amazonaws.com/ios-sdk/talkable.sh
.. _`TalkableSDK v1.5.0`: https://talkable-downloads.s3.amazonaws.com/ios-sdk/talkable_ios_sdk-1.5.0.zip
.. _`GetSocial iOS SDK Manual Integration Guide`: https://docs.getsocial.im/knowledge-base/manual-integration/ios/