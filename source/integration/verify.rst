.. _integration/verify:
.. include:: /partials/common.rst

Verifying Integration
=====================

After installing Talkable, you should verify that the integration is working:

1. Open your homepage (assuming the Talkable init script is placed on every page,
   otherwise visit the page where the initialization script was placed)
   with a secret URL parameter like so: |br| `https://www.site.com/?tkbl_verify_integration=true`.
   As a result you should see:

   .. image:: /_static/img/integration_check_affiliate_member_success.png

2. Issue a test purchase. Order subtotal should be > 0, |br|
   email should be `integration@talkable.com`. Preferably include a coupon code so we
   can verify it gets passed as well. As a result you should see:

   .. image:: /_static/img/integration_check_purchase_success.png

   Talkable verification dialog only appears to you, it will not be shown to anyone else.
   All purchases with `integration@talkable.com` email will not be recorded inside Talkable.

Verifying Integration in JS SPAs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case you are unable to pass **?tkbl_verify_integration=true**
URL parameter you can alternatively turn Talkable into "Verification mode" by setting: |br|
`talkable.config.verify_integration = true;`

All requests will now be coming with "Verification" flag turned on.

**Note:** do not use it in production, this mode is for debugging purpose only.

Troubleshooting
~~~~~~~~~~~~~~~

In case you are not seeing the verification popup please make sure the
:ref:`init script <integration/custom/integration_components/initialization_script>` (non-platform integration only)
is installed on the page. You may do so by making right click |br|
(Chrome) → Inspect Element → Inside Elements tab press Cmd+F (Ctrl+F on Windows) and
search for `d2jj` → make sure the init script matches the one provided inside your
Integration tab inside Talkable Admin.

If you see the init script on the page, but the verification popup still does
not appear on the screen, make sure a request is was passed to Talkable.
To do that open |br| Network tab (Chrome) → refresh the page → inside Search bar look
up for "create.html". Make sure you see something like:

.. image:: /_static/img/chrome_network_tab.png

If the request is coming through but you are still not seeing the verification
popup please contact Talkable support: support@talkable.com.
