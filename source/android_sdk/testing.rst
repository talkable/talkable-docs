.. _android_sdk/testing:
.. include:: /partials/common.rst

Testing
=======

By default, Talkable SDK assigns a permanent ID to each device and uses it to prevent multiple registrations
from a single phone. This helps prevent fraud but can make it challenging to test the referral cycle on
real devices, requiring the developer to either flush all their Talkable campaign data, or use a new campaign
for each test run. Talkable SDK provides tools designed to help with this situation that are available
in debug mode.

The full form of `Talkable.initialize` method allows you to enable the debug mode. In debug mode Talkable SDK
will assign a new ID to the device every time it's initialized, allowing you to be registered as a new visitor each time
the app is launched.

.. code-block:: java

   String initialSiteSlug = null; // pass null to use the siteSlug specified in your manifest
   boolean debug = true;

   Talkable.initialize(this, initialSiteSlug, debug, null);

You can use the last param to pass a custom device ID, allowing you to switch between user identities manually. This way
you can use a single device to pose as an Advocate or Friend and easily replicate various scenarios. The custom device ID
will be applied only if debug is set to `true`.

.. code-block:: java

   String initialSiteSlug = null;
   boolean debug = true;
   String customDeviceId = "qa-advocate-007";

   Talkable.initialize(this, initialSiteSlug, debug, customDeviceId);

.. warning::

   Debug mode must be turned off for release builds. Leaving it enabled will break the referral cycle and expose you to fraud.

.. container:: hidden

   .. toctree::
