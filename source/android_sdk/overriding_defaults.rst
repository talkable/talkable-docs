.. _android_sdk/overriding_defaults:
.. include:: /partials/common.rst

Overriding default behaviour
----------------------------

1. Create new fragment in your app which extends `TalkableOfferFragment`
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


2. Pass activity you want to run a fragment in and the overriden fragment classes to
   `Talkable.showOffer` call:

  .. code-block:: java

    Talkable.showOffer(activity, affiliateMember, MyFragmentActivity.class, OverridenTalkableOfferFragment.class);

And change manifest:

  .. code-block:: xml

    <!-- From -->
    <activity android:name="com.talkable.sdk.TalkableActivity" />

    <!-- To -->
    <activity android:name=".MyFragmentActivity" />

.. note::
   You can just override TalkableOfferFragment and use default TalkableActivity from Talkable SDK.
   In this case you souldn't change manifest
   (if you did steps from :ref:`Getting Started <android_sdk/getting_started>` section).

  .. code-block:: java

    Talkable.showOffer(activity, affiliateMember, TalkableActivity.class, OverridenTalkableOfferFragment.class);


.. container:: hidden

   .. toctree::
