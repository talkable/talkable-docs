.. _integration/magento/magento1:
.. include:: /partials/common.rst

.. meta::
   :description: A Magento Talkable extension is available for easy integration. The extension supports Magento versions 1.5+

Magento 1.x Integration
=======================
.. warning::

   From June 30, 2020 Adobe doesn't support Magento 1.

.. note::

   You must have Talkable account in order to get started

A `Magento Talkable extension`_ is available for easy
integration. The extension currently supports Magento versions 1.5+

1. Since Magento 1 reached EOL and Magento 1 extensions were removed from the
   Magento Marketplace, you only have ability to download them manually via SSH / FTP.

2. After the extension has been installed, you must enable the extension and set
   your Talkable Site ID. Click the **Return to Admin** link and navigate to
   **System** → **Configuration**:

   .. image:: /_static/img/magento/magento-flow-3.jpg

   Note: If you have more than one store, set the **Current Configuration Scope**
   on the top left to the store you want to enable Talkable on. Note this must be
   a Magento "Website", not a "Store view".

3. In the left sidebar navigation click on **Talkable** → **Extension Options** tab:

   .. image:: /_static/img/magento/magento-flow-4.jpg

4. Then, enter your Talkable Site ID. You can copy it from the integration page
   inside Talkable, or on your Talkable Site Dashboard:

   .. image:: /_static/img/magento/magento-flow-5.jpg

   Note: If you see an error opening Talkable extension settings, please
   re-login to Admin Panel and try again.

   Click **Save Config** to save your changes.

5. Go back to Talkable Integration page and click "Verify Integration" button:

   .. image:: /_static/img/magento/magento-flow-6.jpg

.. raw:: html

   <h2>Troubleshooting</h2>

In case you cannot find Talkable extension in the sidebar try clearing cache:

   * In Admin Panel, go to **System** → **Cache Management**.
   * Click **Flush Magento Cache**.
   * Then click **Select All**, select action *"Refresh"* and click **Submit**.

.. _Magento Talkable extension: https://github.com/talkable/talkable-magento/releases/latest
