.. _ecommerce/platform/demandware:
.. include:: /partials/common.rst

Demandware Store Integration
----------------------------

Curebit is a Demandware LINK partner and has easy integration into your
Demandware store. You will need to download the `Demandware Curebit cartridge`_
and follow the instructions below.

Add Curebit catridge and configuration settings

1. Login to your Demandware console with your administrator account.
2. Navigate to
   **Administration** |rarr| **Sites** |rarr| **Manage Sites**
   and select your site.
3. Under **Settings**, add the *int_curebitcartridge* cartridge to your
   Cartridges path.
4. Navigate to
   **Administration** |rarr| **Site Development** |rarr| **Import & Export**.
5. Upload the *'meta_data_curebitcartridge.xml'* file and then proceed
   to import the settings.
6. Navigate to
   **Site** |rarr| **Site Preferences** |rarr| **Custom Preferences** |rarr| **Curebit**.
7. Enter your Curebit Site ID. You can get this from your Curebit dashboard
   after you log in and create a site.
8. Check **Enable Curebit**.

Integrate into order confirmation page

1. In your Demandware UX Studio, locate your *pt_orderconfirmation* page.
2. Near the bottom (immediately preceding `</div> <!-- END: container -->`),
   include this code:

   .. code::

      <!-- Curebit : Code - start - Confirmation -->
      <isinclude template="curebit/curebit_salestrack"/>
      <!-- Curebit : Code - ends - Confirmation -->

3. Save the file and upload it to your Demandware console.
4. Invalidate the page caches (under
   **Administration** |rarr| **Sites** |rarr| **Manage Sites** |rarr| **Site** |rarr| **Cache Tab**)

.. _Demandware Curebit cartridge: http://curebit.com/demandware/curebit_integration_r1.0.0.zip

.. include:: /partials/verifying_integration.rst

.. container:: hidden

   .. toctree::
