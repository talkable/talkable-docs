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
  
  - `Social.framework`
  - `MessageUI.framework`
  - `AddressBook.framework`

  To do this, click on your application's target, then click on Build Phases and expand the Link Binary With Libraries group.
  
4. Add the following import statement to any Objective-C header (.h) or implementation (.m) file in which you wish to use the Talkable SDK.

  .. code-block:: objc
  
    #import <TalkableSDK/Talkable.h>

Configuration
-------------

1. Initialize Talkable in your `application:didFinishLaunchingWithOptions:` method, like so:

  .. code-block:: objc
  
    [[Talkable manager] setApiKey:@"YOUR_TALKABLE_API_KEY" andSiteSlug:@"YOUR_SITE_SLUG"];
    
  .. note::
    
    You can locate your credentials inside Talkable site:
    
    - Visit https://www.talkable.com/account/sites to find you site slug
    - Select site and go to **Dashboard** |rarr| **Site Settings**. Find **Integration settings** section and there you will see the API Key

2. Add following lines to `application:handleOpenURL:` or `application:openURL:sourceApplication:annotation:`

  .. code-block:: objc
  
    [[Talkable manager] handleOpenURL:url];

Your environment is all set up! Now you need to :ref:`integrate <ios_sdk/integration>` the Talkable campaign piece.


Requirements
------------

The SDK supports iOS 7.0 and later.

.. _`Talkable SDK framework`: http://learn.talkable.com/downloads/talkable_ios_sdk.zip

.. container:: hidden

   .. toctree::
