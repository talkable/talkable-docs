.. _android_sdk/upgrade:
.. include:: /partials/common.rst

Upgrade
=======

Sometimes we need you to upgrade existing integration to use our latest features.

0.3.1
-----

Introducing ``TalkableOfferFragmentListener`` interface. Bugs fixing.
.....................................................................

Fixed a bug when no campaign found and added ``TalkableOfferFragmentListener`` interface.

To use ``TalkableOfferFragment`` directly you have to implement ``TalkableOfferFragmentListener``
inside an activity that uses the fragment. See :ref:`Advanced Usage <android_sdk/advanced>`.

0.3.0
-----

Move to Fragments
.................

Talkable SDK is built on top of `Fragments <https://developer.android.com/reference/android/support/v4/app/Fragment.html>`_
(from Support Library) instead of Activities now to provide more flexibility for end users.

0.2.0
-----

Deep linking schema
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

It's initial release, nothing to do.


.. container:: hidden

   .. toctree::
