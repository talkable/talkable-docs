.. _ios_sdk/getting_started:
.. include:: /partials/common.rst

Getting Started
===============

The Getting Started guide shows you how to setup and launch Referral Campaign as quickly as possible with Talkable iOS SDK.

  .. note::

    Make sure your application meets the `Requirements`_

Installation
------------

1. Download the latest version of `Talkable SDK framework`_.
2. Drag and place the `TalkableSDK.framework` somewhere suitable into your Xcode project. Make sure to add the framework to the relevant targets.
3. Add the following frameworks to your project:

  - `AddressBook.framework`
  - `MessageUI.framework`
  - `SafariServices.framework`
  - `Security.framework`
  - `Social.framework`
  - `WebKit.framework`

  To do this, click on your application’s target, then click on Build Phases and expand the Link Binary With Libraries group.

4. Add the following import statement to any Objective-C header (.h) or implementation (.m) file in which you wish to use the Talkable SDK.

  .. code-block:: objc

    #import <TalkableSDK/Talkable.h>

Configuration
-------------

1. Initialize Talkable in your `application:didFinishLaunchingWithOptions:` method, like so:

  .. code-block:: objc

    [[Talkable manager] setApiKey:@"YOUR_TALKABLE_PUBLIC_API_KEY" andSiteSlug:@"YOUR_SITE_SLUG"];

  .. note::

    You can locate your credentials inside Talkable site:

    - Visit https://admin.talkable.com/account/sites to find your site slug
    - Select site and go to **Dashboard** → **Settings** → **Site Settings**.
      Find **Integration settings** section and there you will see your API Keys.
      Use only the public key in your application submitted to the App Store.

2. Register talkable URL scheme:

  - Defines `tkbl-<your-site-slug>` as URL Scheme in your Info.plist file:

    .. code-block:: xml

      <key>CFBundleURLTypes</key>
      <array>
        <dict>
          <key>CFBundleURLSchemes</key>
          <array>
            <string>tkbl-<your-site-slug></string>
          </array>
        </dict>
      </array>

  - Add `tkbl-<your-site-slug>` scheme to the list of schemes that are queried within application. Also add `fb-messenger`, `fbauth2`, `whatsapp` schemes if you going to utilize these sharing channels:

    .. code-block:: xml

      <key>LSApplicationQueriesSchemes</key>
      <array>
        <string>tkbl-your-site-slug</string>
        <string>fb-messenger</string>
        <string>fbauth2</string>
        <string>whatsapp</string>
      </array>

  .. note::

    Please replace `<your-site-slug>` with your actual site slug, which you are
    able to find on your site **Dashboard** at https://admin.talkable.com

3. Add following lines to `application:handleOpenURL:` or `application:openURL:sourceApplication:annotation:`

  .. code-block:: objc

    [[Talkable manager] handleOpenURL:url];

Your environment is all set up! Now you need to :ref:`integrate <ios_sdk/integration>` the Talkable campaign piece.

Requirements
------------

The SDK supports iOS 9.0 and later.

.. _`Talkable SDK framework`: https://talkable-downloads.s3.amazonaws.com/ios-sdk/talkable_ios_sdk.zip

.. container:: hidden

   .. toctree::
