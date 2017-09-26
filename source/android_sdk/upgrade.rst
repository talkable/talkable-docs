.. _android_sdk/upgrade:
.. include:: /partials/common.rst

Upgrade
=======

Sometimes we need you to upgrade existing integration to use our latest features.

0.4.2
-----

Read Contacts permission is optional from this version.

In case you used ``import_contacts`` callback, you have to define ``READ_CONTACTS``
permission inside the manifest:

   .. code-block:: xml

     <manifest xmlns:android="http://schemas.android.com/apk/res/android"
       package="com.android.app.myapp" >
       <uses-permission android:name="android.permission.READ_CONTACTS" />
       ...
     </manifest>

0.4.1
-----

Fixed an issue inside ``TalkableOfferFragment``.

0.4.0
-----

Added multiple site slugs support. Bugs fixing.
...............................................

From this moment you can operate with multiple Talkable sites inside Talkable SDK.
Look in :ref:`Advanced Usage <android_sdk/advanced>` for more detailed information if needed.

To update from the previous version please do following steps.

1. Update dependencies inside ``build.gradle``.

   .. code-block:: groovy

     // From
     compile 'com.google.code.gson:gson:2.4'
     compile 'com.android.support:support-v4:24.2.1'

     // To
     compile 'com.google.code.gson:gson:2.7'
     compile 'com.android.support:support-v4:25.3.1'

2. Change credentials setup inside the manifest.

   .. code-block:: xml

      <!-- From -->
       <application>
           ...
           <meta-data
               android:name="TalkableApiKey"
               android:value="{{YOUR_TALKABLE_PUBLIC_API_KEY}}" />
           <meta-data
               android:name="TalkableSiteSlug"
               android:value="{{YOUR_SITE_SLUG}}" />
           ...
       </application>

       <!-- To -->
       <application>
           ...
           <meta-data
               android:name="tkbl-api-key-{{YOUR_SITE_SLUG}}"
               android:value="{{YOUR_TALKABLE_PUBLIC_API_KEY}}" />
           ...
       </application>

3. Initialize Talkable in the ``Application``.

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

4. Call ``Talkable.trackAppOpen`` inside you main activity class, like before.

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

From this version defining of ``TalkableActivity`` and ``InstallReferrerReceiver``
inside Android Manifest is not necessary.

0.3.1
-----

Introducing ``TalkableOfferFragmentListener`` interface. Bugs fixing.
.....................................................................

Fixed a bug when no campaign found and added ``TalkableOfferFragmentListener`` interface.

To use instance of ``TalkableOfferFragment`` directly you have to implement ``TalkableOfferFragmentListener``
interface from ``TalkableOfferFragment`` class inside an activity that uses the fragment.
Look in :ref:`Advanced Usage <android_sdk/advanced>` for more detailed information if needed.

0.3.0
-----

Move to Fragments
.................

Talkable SDK is built on top of `Fragments <https://developer.android.com/reference/android/support/v4/app/Fragment.html>`_
(from Support Library) instead of Activities now to provide more flexibility for end users.

0.2.0
-----

Deep linking scheme
...................

Add this to ``AndroidManifest.xml`` inside definition of Talkable activity

.. code-block:: xml

  <intent-filter>
      <action android:name="android.intent.action.VIEW" />

      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />

      <data android:scheme="tkbl-{{YOUR_SITE_SLUG}}" />
  </intent-filter>

Tracking app opening
....................

Replace ``Talkable.initialize(this);`` with ``Talkable.trackAppOpen(this);`` in your main activity.
Look in :ref:`installation section <main_activity_setup>` for more detailed information if needed.

0.1.0
-----

It’s initial release, nothing to do.


.. container:: hidden

   .. toctree::
