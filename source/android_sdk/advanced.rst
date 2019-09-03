.. _android_sdk/advanced:
.. include:: /partials/common.rst

Advanced Usage
==============

.. _error_handling:

Error Handling
--------------

Errors from ``Talkable.showOffer`` and ``Talkable.loadOffer`` are handled
inside ``onError`` callback, which provides an instance of ``TalkableOfferLoadException`` class.
You can get error type and error message with ``error.getErrorCode()``
and ``error.getMessage()`` respectively.

Here is a list of possible error codes from ``TalkableOfferLoadException`` with descriptions:

   ``NETWORK_ERROR``: General network error

   ``API_ERROR``: Talkable API unavailable

   ``REQUEST_ERROR``: Bad request

   ``CAMPAIGN_ERROR``: Campaign not found

Using multiple site slugs
-------------------------

To use multiple site slugs in your application, follow these steps:

1. Add credentials for each site you are going to use inside your manifest file.
   Format is the same as from corresponding
   :ref:`Getting Started <setup_credentials>` section.

2. Add deep linking schemas handlers into the main activity entry for each site
   you are going to use. The format is the same as the corresponding
   :ref:`Getting Started <deep_linking_scheme>` section.

3. Set default site slug.

   This can be done by adding this information into the manifest file using
   ``<application>`` entry:

   .. code-block:: xml

      <application>
          ...
          <meta-data
              android:name="tkbl-default-site-slug"
              android:value="{{YOUR_DEFAULT_SITE_SLUG}}" />
          ...
      </application>

   or by passing it through ``Talkable.initialize`` in the ``Application``:

   .. code-block:: java

      import com.talkable.sdk.Talkable;
      import android.app.Application;

      public class App extends Application {
          @Override
          public void onCreate() {
              super.onCreate();
              Talkable.initialize(this, "your-default-site-slug");
          }
      }

   .. note::

      You can set the site slug at any time after initialization in the following way:

      .. code-block:: java

         Talkable.setSiteSlug("some-site-slug");

   Make sure to add the credentials for this site inside the manifest file.
   Otherwise, an exception will be raised.

Sharing via Facebook
--------------------

By default sharing via Facebook is disabled. You can enable it by setting up
your project with the Facebook SDK: `Android - Getting Started`_

Overriding default behaviour
----------------------------

1. Create a new fragment in your app which extends `TalkableOfferFragment`
   and override methods there. Example:

   .. code-block:: java

      import com.talkable.sdk.TalkableOfferFragment;

      public class OverriddenTalkableOfferFragment extends TalkableOfferFragment {
          @Override
          public void copyToClipboard(String string) {
              super.copyToClipboard(string);

              Toast.makeText(getActivity(), "Text copied!", Toast.LENGTH_LONG).show();
          }
      }

2. Pass Class of an activity you want to run a fragment in and the overriden fragment to
   `Talkable.showOffer` call:

   .. code-block:: java

      Talkable.showOffer(activity, affiliateMember, OverridenTalkableOfferFragment.class, new TalkableErrorCallback<TalkableOfferLoadException>() {
          @Override
          public void onError(TalkableOfferLoadException error) {
              // Error handling. Note that it runs on non UI thread
          }
      });

.. _fragment_listener:

If you want to implement custom offer closing handling you should implement
``TalkableOfferFragmentListener`` interface from ``TalkableOfferFragment`` inside your Activity.

.. code-block:: java

   import com.talkable.sdk.TalkableOfferFragment.TalkableOfferFragmentListener;

   public class MyActivity implements TalkableOfferFragmentListener {
       ...
       @Override
       public void onOfferClosed() {
           finish();
       }
       ...
   }

.. _using_fragment_directly:

Using TalkableOfferFragment directly
------------------------------------

By default Talkable Android SDK displays Talkable offer as a fullscreen modal view. If you need to embed the Talkable offer into your layout
or otherwise control the way it's displayed, you can obtain an instance of ``TalkableOfferFragment``, which is a `Fragment`_ that comes
preloaded with Talkable offer content and can be added to your layout dynamically.

To use ``TalkableOfferFragment`` directly, follow these steps:

1. Get an offer code using the ``Talkable.loadOffer(origin, callback)`` method
2. Create a fragment instance by passing the offer code to the ``TalkableOfferFragment.newInstance(shortCode)`` method
3. Use `Fragment Transactions`_ or another method of your choice to display the fragment.

.. code-block:: java

   AffiliateMember affiliateMember = new AffiliateMember();
   ...

   Talkable.loadOffer(affiliateMember, new TalkableCallback<String, TalkableOfferLoadException>() {
       // Note that it runs on non UI thread
       @Override
       public void onSuccess(String offerCode) {
           TalkableOfferFragment fragment = TalkableOfferFragment.newInstance(offerCode);
           myMethodToDisplayTalkableOfferFragment(fragment);
       }

       @Override
       public void onError(TalkableOfferLoadException error) {
           // Error handling
       }
    );

.. note::

   Make sure to `handle configuration changes`_, as ``TalkableOfferFragment``
   is built on top of ``WebView`` and restoring its state is up to you. If you
   need to reinitialize a fragment, you don't need to call ``loadOffer`` again.
   Simply store the ``offerCode`` and use it to create a new ``TalkableOfferFragment``
   instance.

Native integration via API
--------------------------

Talkable provides an :ref:`API <android_sdk/api>` that can be utilized to
implement a fully native referral program interface if the default solution
(based on ``WebView``) doesn't work for you.
Below are the methods necessary to integrate the Talkable referral loop into
your Android application.

1. The first step is to get an ``Offer`` by creating an ``Origin``: :ref:`Create origin <android-api-origins>`
2. Then, share the obtained ``Offer``: :ref:`Create offer share <android-api-sharing>`
3. Check for rewards: :ref:`Retrieve rewards <android-api-rewards>`

.. _`Android - Getting Started`: https://developers.facebook.com/docs/android/getting-started
.. _`handle configuration changes`: https://developer.android.com/guide/topics/resources/runtime-changes.html
.. _`Fragment`: https://developer.android.com/guide/components/fragments
.. _`Fragment Transactions`: https://developer.android.com/guide/components/fragments#Transactions

.. container:: hidden

   .. toctree::
