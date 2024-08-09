:orphan:

.. include:: /partials/common.rst

Deep Linking
============

Talkable uses `GetSocial.im`_ technology to provide installation attribution and
deep linking functionality with its Android SDK. This guide describes how to
configure your Talkable campaign for deep linking and add support for it to
your Android app.

.. note::

   Credentials, mentioned in this document (``YOUR_SITE_SLUG``, ``YOUR_TALKABLE_PUBLIC_API_KEY``,
   ``YOUR_GETSOCIAL_APP_ID``, ``YOUR_LINK_DOMAIN_PREFIX``), will be provided
   with the document. Make sure to replace corresponding placeholders
   in examples with the providen values.

Application Attributes
----------------------

To enable the deep linking, you should provide us with *Package name* and
*Signing-certificate fingerprints*.

*Package name* is the ``applicationId`` in your app-level ``build.gradle`` file.

*Signing-certificate fingerprints* is a list of SHA-256 hashes of the certificates
you use to sign your application. You should provide fingerprints of all keys
you use to sign the app. This tutorial tells you how to do this:
`Finding SHA256 fingerprint for Android signing keys`_

Configure SDK and Dependencies
------------------------------

Talkable SDK is distributed as an Android Library in ``aar`` format.

1. Add ``talkable-sdk.aar`` as a module dependency in Android studio.

   .. note::

      To do this, open import popup using *File* → *New* → *New Module* → *Import .JAR/.AAR Package*
      and add Talkable SDK as a module dependency to your main module

2. Add Talkable SDK dependencies to ``build.gradle``:

   .. code-block:: groovy

      dependencies {
          ...
          implementation 'com.squareup.okhttp3:okhttp:3.2.0'
          implementation 'com.facebook.android:facebook-android-sdk:[4,5)'
          implementation 'im.getsocial:getsocial-core:[6,7)@aar'
          implementation 'com.android.installreferrer:installreferrer:1.0'
          implementation 'com.google.code.gson:gson:2.8.0'
          implementation 'com.android.support:support-v4:27.1.1'
          implementation project(':talkable-sdk')
          ...
      }

3. Add GetSocial Maven Repository to the list of project dependency
   repositories inside your top-level ``build.gradle``:

   .. code-block:: groovy

      allprojects {
          repositories {
              ...
              maven { url 'http://maven.getsocial.im/' }
              ...
          }
      }

Configure Manifest
------------------

Open your ``AndroidManifest.xml`` file and configure it by following next steps:

1. Specify Talkable credentials as a meta-data inside the ``<application>`` tag
   in the following format:

   .. code-block:: xml

       <application>
           ...
           <meta-data
               android:name="tkbl-api-key-YOUR_SITE_SLUG"
               android:value="YOUR_TALKABLE_PUBLIC_API_KEY" />
           ...
       </application>

2. Specify GetSocial App ID as a meta-data inside the ``<application>`` tag:

   .. code-block:: xml

      <application>
          ...
          <meta-data
              android:name="im.getsocial.sdk.AppId"
              android:value="YOUR_GETSOCIAL_APP_ID" />
          ...
      </application>

3. Add Content Provider for GetSocial SDK auto initialization inside the
   ``<application>`` tag:

   .. code-block:: xml

      <application>
          ...
          <provider
              android:authorities="YOUR_GETSOCIAL_APP_ID.AutoInitSdkContentProvider"
              android:exported="false"
              android:enabled="true"
              android:name="im.getsocial.sdk.AutoInitSdkContentProvider" />
          ...
      </application>

4. Configure Install Referrer Receiver as the *first* receiver for ``INSTALL_REFERRER``
   inside the ``<application>`` tag:

   .. code-block:: xml

      <application>
          ...
          <receiver android:name="im.getsocial.sdk.invites.MultipleInstallReferrerReceiver"  android:exported="true">
              <intent-filter>
                  <action android:name="com.android.vending.INSTALL_REFERRER"/>
              </intent-filter>
          </receiver>
          ...
      </application>

5. Add the following intent filter to the activity, that should be opened from the
   deep link, inside the corresponding tag:

   .. code-block:: xml

      <activity>
          ...
         <intent-filter>
             <action android:name="android.intent.action.VIEW"/>

             <category android:name="android.intent.category.DEFAULT"/>
             <category android:name="android.intent.category.BROWSABLE"/>

             <data
                 android:host="YOUR_GETSOCIAL_APP_ID"
                 android:scheme="getsocial"/>
         </intent-filter>

         <intent-filter>
             <action android:name="android.intent.action.VIEW" />

             <category android:name="android.intent.category.DEFAULT" />
             <category android:name="android.intent.category.BROWSABLE" />

             <data android:scheme="tkbl-YOUR_SITE_SLUG" />
         </intent-filter>
         ...
      </activity>

6. Setup App Links for Android 6+. App Links (supported on Android 6.0
   (API level 23) and higher) allow the user to be taken directly to the app
   on the link click without the browser window in the middle. Check
   the official `Android App Links docs`_ for more details.
   To set them up add intent filter with the following host configuration
   to the activity that must be opened from the deep link:

   .. code-block:: xml

      <activity>
          ...
         <intent-filter android:autoVerify="true">
             <action android:name="android.intent.action.VIEW" />
             <category android:name="android.intent.category.DEFAULT" />
             <category android:name="android.intent.category.BROWSABLE" />
             <data android:scheme="https" android:host="YOUR_LINK_DOMAIN_PREFIX.gsc.im" />
             <data android:scheme="https" android:host="YOUR_LINK_DOMAIN_PREFIX-gsalt.gsc.im" />
         </intent-filter>
         ...
      </activity>

SDK Initialization
------------------

1. Initialize Talkable in the ``Application``:

   .. code-block:: java

      import com.talkable.sdk.Talkable;

      public class App extends Application {
          @Override
          public void onCreate() {
              super.onCreate();
              Talkable.initialize(this);
          }
      }

   .. note::

      Make sure to add your application class name as ``android:name`` parameter
      of the ``<application>`` element in your manifest.

2. Call the ``Talkable.trackAppOpen`` method inside your main activity:

   .. code-block:: java

      import com.talkable.sdk.Talkable;

      public class MainActivity extends Activity {
          @Override
          public void onCreate(Bundle savedInstanceState) {
              super.onCreate();
              Talkable.trackAppOpen(this);
          }
      }

Requirements
------------

The SDK supports Android 4.1 and later.

.. _`GetSocial.im`: https://www.getsocial.im
.. _`Android App Links docs`: https://developer.android.com/training/app-links/index.html
.. _`Finding SHA256 fingerprint for Android signing keys`: https://docs.getsocial.im/knowledge-base/android-signing-key-sha256/

.. container:: hidden

   .. toctree::
