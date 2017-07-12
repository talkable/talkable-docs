.. _android_sdk/getting_started:
.. include:: /partials/common.rst

Getting Started
===============

The Getting Started guide shows you how to setup and launch Referral Campaign as quickly as possible with Talkable Android SDK.


Installation
------------

1. Download the latest version of `Talkable SDK framework`_.
2. Add ``talkable-sdk.aar`` and add it as project dependency in Android studio.

   .. note::

     To do this, open import popup using *File* |rarr| *New* |rarr| *New Module* |rarr| *Import .JAR/.AAR Package*

   After this, add dependencies to ``build.gradle``

   .. code-block:: groovy

       compile 'com.squareup.okhttp3:okhttp:3.2.0'
       compile 'com.facebook.android:facebook-android-sdk:[4,5)'
       compile 'com.google.code.gson:gson:2.7'
       compile 'com.android.support:support-v4:25.3.1'
       compile project(':talkable-sdk')


3. Add Talkable activity to your ``AndroidManifest.xml`` file inside ``<application>`` element.

   .. code-block:: xml

       <activity android:name="com.talkable.sdk.TalkableActivity" />

.. _setup_credentials:

4. Setup Talkable credentials in ``AndroidManifest.xml`` file inside
   ``<application>`` element in the following format:

   .. code-block:: xml

       <application>
           ...
           <meta-data
               android:name="tkbl-api-key-{{YOUR_SITE_SLUG}}"
               android:value="{{YOUR_TALKABLE_PUBLIC_API_KEY}}" />
           ...
       </application>

   .. note::

     You can locate your credentials inside Talkable site:

     - Visit https://admin.talkable.com/account/sites to find your site slug
     - Select site and go to **Dashboard** |rarr| **Settings** |rarr| **Site Settings**.
       Find **Integration settings** section and there you will see your API Keys.
       Use only the public key in your application.

.. _deep_linking_scheme:

5. Add deep linking schema handler into your main activity entry.

   .. code-block:: xml

     <intent-filter>
         <action android:name="android.intent.action.VIEW" />

         <category android:name="android.intent.category.DEFAULT" />
         <category android:name="android.intent.category.BROWSABLE" />

         <data android:scheme="tkbl-{{YOUR_SITE_SLUG}}" />
     </intent-filter>

6. Add the following entry into ``<application>`` element in your ``AndroidManifest.xml`` file to track app installs.

   .. code-block:: xml

       <receiver
           android:name="com.talkable.sdk.InstallReferrerReceiver"
           android:exported="true">
           <intent-filter>
               <action android:name="com.android.vending.INSTALL_REFERRER" />
           </intent-filter>
       </receiver>

.. _main_activity_setup:

7. Initialize Talkable in the ``Application``:

   .. code-block:: java

     import com.talkable.sdk.Talkable;
     import android.app.Application;

     public class App extends Application {
         @Override
         public void onCreate() {
             super.onCreate();
             Talkable.initialize(this);
         }
     }

   .. note::

     Make sure to add your application class name as ``android:name`` parameter of
     the ``<application>`` element in your manifest

8. Call ``Talkable.trackAppOpen`` inside you main activity class, like so:

   .. code-block:: java

     import com.talkable.sdk.Talkable;
     import android.app.Activity;

     public class MainActivity extends Activity {
         @Override
         public void onCreate(Bundle savedInstanceState) {
             ...

             Talkable.trackAppOpen(this);
         }
     }

Here is an example of ``AndroidManifest.xml`` file (with ``"demo-site"`` site slug) you should setup after steps above:

  .. code-block:: xml

      <?xml version="1.0" encoding="utf-8"?>
      <manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="com.talkable.demo">

          <application
              android:allowBackup="true"
              android:icon="@mipmap/ic_launcher"
              android:label="@string/app_name"
              android:supportsRtl="true"
              android:theme="@style/AppTheme"
              android:name=".App">
              <activity android:name=".MainActivity">
                  <intent-filter>
                      <action android:name="android.intent.action.MAIN" />

                      <category android:name="android.intent.category.LAUNCHER" />
                  </intent-filter>

                  <intent-filter>
                      <action android:name="android.intent.action.VIEW" />

                      <category android:name="android.intent.category.DEFAULT" />
                      <category android:name="android.intent.category.BROWSABLE" />

                      <data android:scheme="tkbl-demo-site" />
                  </intent-filter>
              </activity>

              <!-- Talkable -->

              <activity android:name="com.talkable.sdk.TalkableActivity" />

              <meta-data
                  android:name="tkbl-api-key-demo-site"
                  android:value="nacsc9XseW4Kxne6AaJ" />

              <receiver
                  android:name="com.talkable.sdk.InstallReferrerReceiver"
                  android:exported="true">
                  <intent-filter>
                      <action android:name="com.android.vending.INSTALL_REFERRER" />
                  </intent-filter>
              </receiver>

              <!-- End Talkable -->
          </application>
      </manifest>

Your environment is all set up! Now you need to :ref:`integrate <android_sdk/integration>` the Talkable campaign piece.


Requirements
------------

The SDK supports Android 4.1 and later.

.. _`Talkable SDK framework`: https://talkable-downloads.s3.amazonaws.com/android-sdk/talkable-sdk.aar

.. container:: hidden

   .. toctree::
