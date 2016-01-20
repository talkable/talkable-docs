.. _android_sdk/getting_started:
.. include:: /partials/common.rst

Getting Started
===============

The Getting Started guide shows you how to setup and launch Referral Campaign as quickly as possible with Talkable Android SDK.


Installation
------------

1. Download the latest version of `Talkable SDK framework`.
2. Add `talkable.jar` to `libs` directory
3. Add the following entry in your `AndroidManifest.xml` file to track app installs.

  ..  TODO

  .. code-block:: xml

      <service android:name="com.talkable.sdk.InstallReferrerService"/>
      <receiver
          android:name="com.talkable.sdk.InstallReferrerReceiver"
          android:exported="true">
          <intent-filter>
              <action android:name="com.android.vending.INSTALL_REFERRER" />
          </intent-filter>
      </receiver>


4. Add the following import statement to any file in which you wish to use the Talkable SDK.

  .. code-block:: java

    import com.talkable.sdk;

Configuration
-------------

1. Initialize Talkable in your `MainActivity` class, like so:

  .. code-block:: java

    import com.talkable.sdk;

    public class YourActivityName extends Activity {
        @Override
        public void onCreate() {
            Talkable.configure("YOUR_TALKABLE_API_KEY", "YOUR_SITE_SLUG");
            Talkable.registerURLScheme("YOUR_APPLICATION_URL_SCHEME");
        }
    }

  .. note::

    You can locate your credentials inside Talkable site:

    - Visit https://www.talkable.com/account/sites to find you site slug
    - Select site and go to **Dashboard** |rarr| **Site Settings**. Find **Integration settings** section and there you will see the API Key

2. Add following lines to `application:handleOpenURL:` or `application:openURL:sourceApplication:annotation:`

  .. code-block:: objc

    [[Talkable manager] handleOpenURL:url];

Your environment is all set up! Now you need to :ref:`integrate <ios_sdk/integration>` the Talkable campaign piece.


.. container:: hidden

   .. toctree::
