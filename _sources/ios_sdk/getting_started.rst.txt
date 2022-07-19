.. _ios_sdk/getting_started:
.. include:: /partials/common.rst

Getting Started
===============

The Getting Started guide shows you how to setup and launch Referral Campaign as quickly as possible with Talkable iOS SDK.

Requirements
------------

- Talkable SDK supports iOS *9.0* and later
- Add the `-ObjC` option to **Other Linker Flags** in the **Build Settings** tab

Step 1: Installation
--------------------

Talkable SDK could be integrated using `Swift Package Manager`_, `CocoaPods`_ or manually as a `Binary Framework`_.

Swift Package Manager
`````````````````````

Installing from Xcode:

1. Add a package by selecting **File** → **Add Packages…** in Xcode’s menu bar.
2. Search for the Talkable SDK using the repo's URL:

  .. code-block:: bash

    https://github.com/talkable/ios-sdk.git

3. Set the **Dependency Rule** to be `Up to Next Major Version` and specify `1.4.12` as the lower bound (default option).
4. Select **Add Package** and choose `TakableSDK` package.

Alternatively, you can add Talkable SDK directly to a `Package.swift` manifest:

  .. code-block:: swift

      dependencies: [
          .package(url: "https://github.com/talkable/ios-sdk.git", .upToNextMajor(from: "1.4.12"))
      ]

CocoaPods
`````````

To integrate Talkable SDK into your Xcode project using CocoaPods, specify it in your `Podfile`_:

  .. code-block:: ruby

    pod 'TalkableSDK', '~> 1.4.12'

Binary Framework
````````````````

To integrate the SDK manually as a Binary Framework, please follow next intructions:

1. Download the latest version of `Talkable SDK`_.
2. Navigate to your project settings by clicking on it in the project navigator.
3. Make sure that your target is selected and **General** tab is open.
4. Go to **Frameworks, Libraries, and Embedded Content** section and add the SDK by clicking **"+"** button → **Add Other...** → **Add Files...** and locate the downloaded SDK.
5. For **Embed** setting of the added framework select `Do Not Embed` option.
6. Make sure that Talkable SDK is linked with your project in **Link Binary With Libraries** section under **Build Phases** tab with `Required` Status.
   It should already be included by default after following the steps above, however in case it’s not – click on the **"+"** button and add it.

Step 2: Configuration
---------------------

1. Initialize Talkable SDK in your `application:didFinishLaunchingWithOptions:` method, like so:

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    // ...
    [[Talkable manager] setApiKey:@"YOUR_TALKABLE_PUBLIC_API_KEY" andSiteSlug:@"YOUR_SITE_SLUG"];

  .. note::

    You can locate your credentials inside Talkable site:

    - Visit https://admin.talkable.com/account/sites to find your site slug
    - Select site and go to **Dashboard** → **Settings** → **Site Settings**.
      Find **API integration** section and there you will see your API Keys.
      Use only the *Public API Key* in your application submitted to the App Store.

2. Register URL scheme for Talkable:

  - Defines `tkbl-YOUR-SITE-SLUG` as URL Scheme in your Info.plist file:

    .. code-block:: xml

      <key>CFBundleURLTypes</key>
      <array>
        <dict>
          <key>CFBundleURLSchemes</key>
          <array>
            <string>tkbl-YOUR-SITE-SLUG</string>
          </array>
        </dict>
      </array>

  - Add `tkbl-YOUR-SITE-SLUG` scheme to the list of schemes that are queried within application. Also add `fb-messenger`, `fbauth2`, `whatsapp` schemes if you going to utilize these sharing channels:

    .. code-block:: xml

      <key>LSApplicationQueriesSchemes</key>
      <array>
        <string>tkbl-YOUR-SITE-SLUG</string>
        <string>fb-messenger</string>
        <string>fbauth2</string>
        <string>whatsapp</string>
      </array>

  .. note::

    Please replace `YOUR-SITE-SLUG` with your actual site slug, which can
    be found on your site's **Dashboard** at https://admin.talkable.com.
    Make sure to keep `tkbl-` prefix in the `<string>` value. For example,
    if your site slug is `my-store`, the correct `<string>` value is `tkbl-my-store`.

3. Add following lines to `application:handleOpenURL:` or `application:openURL:sourceApplication:annotation:`

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>
    // ...
    [[Talkable manager] handleOpenURL:url];

Your environment is all set up! Now you can :ref:`integrate <ios_sdk/integration>` the Talkable campaign piece.

.. _`Talkable SDK`: https://talkable-downloads.s3.amazonaws.com/ios-sdk/talkable_ios_sdk.zip
.. _`Talkable SDK pod's page`: https://cocoapods.org/pods/TalkableSDK
.. _`Podfile`: https://guides.cocoapods.org/using/the-podfile.html
