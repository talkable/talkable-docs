.. _android_sdk/advanced:
.. include:: /partials/common.rst

Advanced Usage
==============

Using multiple site slugs
-------------------------

To use multiple site slugs inside your application, you have to do next steps:

1. Add credentials for each site you are going to use inside your manifest file.
   Format is the same as from corresponding
   :ref:`Getting Started <setup_credentials>` section.

2. Add deep linking schemas handlers into your main activity entry for each site
   you are going to use too. Format is the same as from corresponding
   :ref:`Getting Started <deep_linking_scheme>` section.

3. Set default site slug.

   It can be done by adding this information to the manifest file into
   ``<application>`` entry:

   .. code-block:: xml

      <application>
          ...
          <meta-data
              android:name="tkbl-default-site-slug"
              android:value="{{YOUR_DEFAULT_SITE_SLUG}}" />
          ...
      </application>

   or by passing through ``Talkable.initialize`` in the ``Application``:

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

     You can set site slug at any time after initialization in the following way:

     .. code-block:: java

       Talkable.setSiteSlug(context, "some-site-slug");

     Make sure to add credentials for this site inside the manifest file.
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

     Talkable.showOffer(activity, affiliateMember, MyFragmentActivity.class, OverridenTalkableOfferFragment.class);

   .. note::

      You can just override ``TalkableOfferFragment`` and use default
      ``TalkableActivity`` from Talkable SDK.
      In this case, you shouldn’t change the manifest
      (if you did steps from :ref:`Getting Started <android_sdk/getting_started>` section).

     .. code-block:: java

       Talkable.showOffer(activity, affiliateMember, TalkableActivity.class, OverridenTalkableOfferFragment.class);

Using TalkableOfferFragment directly
------------------------------------

To use instance of ``TalkableOfferFragment`` you have to implement ``TalkableOfferFragmentListener``
interface from ``TalkableOfferFragment`` class inside your activity.

.. code-block:: java

  import com.talkable.sdk.TalkableOfferFragment.TalkableOfferFragmentListener;

  public class MyActivity implements TalkableOfferFragmentListener {

      ...

      @Override
      public void onOfferClosed() {
          if (mTalkableOfferFragment.isOfferLoaded()) {
              finish();
          }
      }

      ...
  }

Then you should :ref:`create an origin <android_sdk/integration>` and
pass it to ``TalkableOfferFragment`` instance via ``Bundle``.
After this you can start using the fragment.

.. code-block:: java

  AffiliateMember affiliateMember = new AffiliateMember();

  Bundle arguments = new Bundle();
  arguments.putParcelable(TalkableOfferFragment.ORIGIN_PARAM, affiliateMember);

  TalkableOfferFragment talkableOfferFragment = new TalkableOfferFragment();
  talkableOfferFragment.setArguments(arguments);

.. _`Android - Getting Started`: https://developers.facebook.com/docs/android/getting-started

.. container:: hidden

   .. toctree::
