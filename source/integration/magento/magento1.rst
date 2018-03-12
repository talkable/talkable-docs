.. _integration/magento/magento1:
.. include:: /partials/common.rst

Magento 1.x Integration
=======================

.. note::

  You must have Talkable account in order to get started

A `Magento Talkable extension`_ (`direct download`_) is available for easy
integration. The extension currently supports Magento versions 1.5+

1. Log into your Magento Admin Panel (usually located at
   `http://your-site.com/index.php/admin`). We will install the Talkable extension
   using Magento Connect Manager. Go to
   **System** |rarr| **Magento Connect** |rarr| **Magento Connect Manager**.
   You may be required to log in again:

   .. image:: /_static/img/magento/magento-flow-1.jpg

2. Copy the extension key: **http://connect20.magentocommerce.com/community/talkable** |rarr| then paste it into an extension key input field (2) and click **Install** (3). In the table below you should see a status "Ready to install", hit **Proceed** (4):

   .. image:: /_static/img/magento/magento-flow-2.jpg

   You should see the console window indicate successful installation.

3. After the extension has been installed, you must enable the extension and set
   your Talkable Site ID. Click the **Return to Admin** link and navigate to
   **System** |rarr| **Configuration**:

   .. image:: /_static/img/magento/magento-flow-3.jpg

   Note: If you have more than one store, set the **Current Configuration Scope**
   on the top left to the store you want to enable Talkable on. Note this must be
   a Magento "Website", not a "Store view".

4. In the left sidebar navigation click on **Talkable** |rarr| **Extension Options** tab:

   .. image:: /_static/img/magento/magento-flow-4.jpg

5. Then, enter your Talkable Site ID. You can copy it from the integration page
   inside Talkable, or on your Talkable Site Dashboard:

   .. image:: /_static/img/magento/magento-flow-5.jpg

   Note: If you see an error opening Talkable extension settings, please
   re-login to Admin Panel and try again.

   Click **Save Config** to save your changes.

6. Go back to Talkable Integration page and click "Verify Integration" button:

   .. image:: /_static/img/magento/magento-flow-6.jpg

.. raw:: html

  <h2>Troubleshooting</h2>

In case you cannot find Talkable extension in the sidebar try clearing cache:

   * In Admin Panel, go to **System** |rarr| **Cache Management**.
   * Click **Flush Magento Cache**.
   * Then click **Select All**, select action *"Refresh"* and click **Submit**.

.. _Magento Talkable extension: https://marketplace.magento.com/talkable-talkable.html
.. _direct download: https://github.com/talkable/talkable-magento/releases/latest
