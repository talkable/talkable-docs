.. _android_sdk/getting_started:
.. include:: /partials/common.rst

Getting Started
===============

The Getting Started guide shows you how to setup and launch Referral Campaign as quickly as possible with Talkable Android SDK.


Installation
------------

1. Download the latest version of `Talkable SDK framework`.
2. Add `talkable.aar` and add it as project dependency in android studio.


  .. note::

    To do this, open import popup using *File* |rarr| *New* |rarr| *New Module* |rarr| *Import .JAR/.AAR Package*

After this, add dependencies to `build.gradle`

  .. code-block:: groovy

      compile 'com.android.support:appcompat-v7:23.4.0'
      compile 'com.squareup.okhttp3:okhttp:3.2.0'
      compile 'com.facebook.android:facebook-android-sdk:[4,5)'
      compile 'com.google.code.gson:gson:2.4'


3. Add Talkable activity to your `AndroidManifest.xml`

  .. code-block:: xml

      <activity android:name="com.talkable.sdk.TalkableActivity" />

4. Setup Talkable credentials in `AndroidManifest.xml`

  .. code-block:: xml

      <meta-data android:name="TalkableServer" android:value="https://talkable.com" />
      <meta-data android:name="TalkableApiKey" android:value="{{YOUR_TALKABLE_API_KEY}}" />
      <meta-data android:name="TalkableSiteSlug" android:value="{{YOUR_SITE_SLUG}}" />

  .. note::

    You can locate your credentials inside Talkable site:

    - Visit https://www.talkable.com/account/sites to find you site slug
    - Select site and go to **Dashboard** |rarr| **Site Settings**.
      Find **Integration settings** section and there you will see the API Key

5. Add the following entry in your `AndroidManifest.xml` file to track app installs.

  .. code-block:: xml

      <receiver
          android:name="com.talkable.sdk.InstallReferrerReceiver"
          android:exported="true">
          <intent-filter>
              <action android:name="com.android.vending.INSTALL_REFERRER" />
          </intent-filter>
      </receiver>

6. Initialize Talkable in your main activity class, like so:

  .. code-block:: java

    import com.talkable.sdk.Talkable;

    public class MainActivity extends Activity {
        @Override
        public void onCreate(Bundle savedInstanceState) {
            ...

            Talkable.initialize(this);
        }
    }

Your environment is all set up! Now you need to :ref:`integrate <android_sdk/integration>` the Talkable campaign piece.


.. container:: hidden

   .. toctree::
