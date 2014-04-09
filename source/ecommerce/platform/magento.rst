.. _ecommerce/platform/magento:
.. include:: /partials/common.rst

Magento Store Integration
-------------------------

A `Magento Curebit extension`_ (`direct download`_) is available for easy
integration. The extension currently supports Magento versions 1.3.x and 1.4.x.

1. Log into your Magento Admin Dashboard (usually located at
   http://your-site.com/index.php/admin). We will install the Curebit extension
   using Magento Connect Manager. Go to
   **System** |rarr| **Magento Connect** |rarr| **Magento Connect Manager**.
   You may be required to log in again.
2. For Magento 1.3/1.4, enter the extension name:

   | *magento-community/Curebit_Checkout*

   For Magento 1.5+, enter the extension name:

   | *http://connect20.magentocommerce.com/community/Curebit_Checkout*

   and click **Install**.
   You should see the console window indicate successful installation.
3. After the extension has been installed, you must enable the extension and set
   your Curebit Site ID.

   * Click the **Return to Admin** link and navigate to
     **System** |rarr| **Configuration**. If you have more than one store, set
     the **Current Configuration Scope** on the top left to the store you want
     to enable Curebit on. Note this must be a Magento "Website", not a "Store view".
   * On the left navigation under **Sales**, click **Checkout**. You will need
     to uncheck **Use Default** if you have more than one site.
   * Open the Curebit Integration tab and set the **Enabled** state to *Yes*.
     Then, enter your Curebit Site ID.

     You will need to get your Curebit Site ID from your dashboard after you
     have created the site.

   Click **Save Config** to save your changes.
4. Flush the caches:

   * In admin panel, **System** |rarr| **Cache Management**.
   * Click **Flush Magento Cache**.
   * Then click **Select All**, select action *"Refresh"* and click **Submit**.

5. If you are using Magento 1.3.x, and you are using a theme from a package that
   is NOT "default", you must copy the Curebit layout files into your custom
   theme directory.

   * Copy the directory:

     | *{{base_dir}}/app/design/frontend/base/default/template/curebit*

     to:

     | *{{base_dir}}/app/design/frontend/<your theme name>/default/template/curebit*

   * Copy the file:

     | *{{base_dir}}/app/design/frontend/base/default/layout/curebit.xml*

     to:

     | *{{base_dir}}/app/design/frontend/<your theme name>/default/layout/curebit.xml*

.. _Magento Curebit extension: http://www.magentocommerce.com/magento-connect/curebit-checkout.html
.. _direct download: http://curebit.com/magento/Curebit_Checkout-0.1.10.tgz

|br|

:ref:`Verifying Integration Instructions <ecommerce/verify>`

.. container:: hidden

   .. toctree::
