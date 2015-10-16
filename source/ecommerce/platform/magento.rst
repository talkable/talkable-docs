.. _ecommerce/platform/magento:
.. include:: /partials/common.rst

Magento Store Integration
-------------------------

.. note::

  You must have Talkable account in order to get started

A `Magento Talkable extension`_ (`direct download`_) is available for easy
integration. The extension currently supports Magento versions 1.5+

1. Log into your Magento Admin Panel (usually located at
   http://your-site.com/index.php/admin). We will install the Talkable extension
   using Magento Connect Manager. Go to
   **System** |rarr| **Magento Connect** |rarr| **Magento Connect Manager**.
   You may be required to log in again.

2. Enter the extension name and click **Install**:

   | *http://connect20.magentocommerce.com/community/talkable*

   .. image:: /_static/img/magento_connect.png
      :alt: Magento Connect Manager

   You should see the console window indicate successful installation.

3. After the extension has been installed, you must enable the extension and set
   your Talkable Site ID.

   * Click the **Return to Admin** link and navigate to
     **System** |rarr| **Configuration**. If you have more than one store, set
     the **Current Configuration Scope** on the top left to the store you want
     to enable Talkable on. Note this must be a Magento "Website", not a "Store view".
   * Open the **Talkable** tab and under Post-Checkout Integration set the
     **Enabled** state to *Yes*. Then, enter your Talkable Site ID.

     You will need to get your Talkable Site ID from your dashboard after you
     have created the site.

   Click **Save Config** to save your changes.

4. Flush the caches:

   * In Admin Panel, go to **System** |rarr| **Cache Management**.
   * Click **Flush Magento Cache**.
   * Then click **Select All**, select action *"Refresh"* and click **Submit**.

.. _Magento Talkable extension: http://www.magentocommerce.com/magento-connect/talkable-customizable-refer-a-friend-programs.html
.. _direct download: https://www.talkable.com/magento/talkable-0.1.6.tgz

|br|

:ref:`Verifying Integration Instructions <ecommerce/verify>`

.. container:: hidden

   .. toctree::
