.. _ecommerce/platform/opencart:
.. include:: /partials/common.rst

OpenCart Store Integration
--------------------------

After setting up a Curebit account, you need to create a site for each store you
wish to integrate. Then, download the `OpenCart Curebit Checkout Extension`_.

1. Extract the extension file in the root of your OpenCart directory
   (no files will be overwritten).
2. Log in to the admin section of your OpenCart site and click
   **Extensions** |rarr| **Modules**.
3. Locate the Curebit Checkout module and click **Install**.
4. Click the **Edit** action for Curebit Checkout.
5. Set the status to *Enabled*, and enter your Curebit Site ID. You can get this
   from your Curebit dashboard after you log in and create a site.
6. For OpenCart version 1.5+, edit:

   | */catalog/controller/checkout/success.php*

   and merge in the 3 lines indicated:

   .. include:: /samples/ecommerce/platform/opencart.rst

.. raw:: html

   <h2>Reporting Problems with Integration</h2>

| OpenCart Curebit Checkout Extension is open sourced and `available on GitHub`_.
| Please report any bugs and make any feature requests on the GitHub `issue tracker`_.
| If you would like to contribute, please feel free to open a pull request.

.. _OpenCart Curebit Checkout Extension: http://www.opencart.com/index.php?route=extension/extension/info&extension_id=15716
.. _available on GitHub: https://github.com/curebit/curebit-opencart-extension
.. _issue tracker: https://github.com/curebit/curebit-opencart-extension/issues

.. include:: /partials/verifying_integration.rst

.. container:: hidden

   .. toctree::
