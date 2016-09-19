.. _android_sdk/getting_started:
.. include:: /partials/common.rst

Getting Started
===============

The Getting Started guide shows you how to setup and launch Referral Campaign as quickly as possible with Talkable Android SDK.


Installation
------------

1. Download the latest version of `Talkable SDK framework`_.
2. Add `talkable-sdk.aar` and add it as project dependency in Android studio.


  .. note::

    To do this, open import popup using *File* |rarr| *New* |rarr| *New Module* |rarr| *Import .JAR/.AAR Package*

After this, add dependencies to `build.gradle`

  .. code-block:: groovy

      compile 'com.squareup.okhttp3:okhttp:3.2.0'
      compile 'com.facebook.android:facebook-android-sdk:[4,5)'
      compile 'com.google.code.gson:gson:2.4'
      compile project(':talkable-sdk')


3. Add Talkable activity to your `AndroidManifest.xml`

  .. code-block:: xml

      <activity android:name="com.talkable.sdk.TalkableActivity" />

4. Setup Talkable credentials in `AndroidManifest.xml`

  .. code-block:: xml

      <meta-data android:name="TalkableApiKey" android:value="{{YOUR_TALKABLE_API_KEY}}" />
      <meta-data android:name="TalkableSiteSlug" android:value="{{YOUR_SITE_SLUG}}" />

  .. note::

    You can locate your credentials inside Talkable site:

    - Visit https://www.talkable.com/account/sites to find you site slug
    - Select site and go to **Dashboard** |rarr| **Site Settings**.
      Find **Integration settings** section and there you will see the API Key

5. Add deep linking schema handler into your main activity entry.

.. code-block:: xml

  <intent-filter>
      <action android:name="android.intent.action.VIEW" />

      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />

      <data android:scheme="tkbl-{{YOUR_SITE_SLUG}}" />
  </intent-filter>


6. Add the following entry in your `AndroidManifest.xml` file to track app installs.

  .. code-block:: xml

      <receiver
          android:name="com.talkable.sdk.InstallReferrerReceiver"
          android:exported="true">
          <intent-filter>
              <action android:name="com.android.vending.INSTALL_REFERRER" />
          </intent-filter>
      </receiver>

.. _main_activity_setup:

7. Initialize Talkable in your main activity class, like so:

  .. code-block:: java

    import com.talkable.sdk.Talkable;

    public class MainActivity extends Activity {
        @Override
        public void onCreate(Bundle savedInstanceState) {
            ...

            Talkable.trackAppOpen(this);
        }
    }

Your environment is all set up! Now you need to :ref:`integrate <android_sdk/integration>` the Talkable campaign piece.


Requirements
------------

The SDK supports Android 4.1 and later.

.. _`Talkable SDK framework`: https://talkable-downloads.s3.amazonaws.com/android-sdk/talkable-sdk.aar

.. container:: hidden

   .. toctree::
