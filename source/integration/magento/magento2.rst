.. _integration/magento/magento2:
.. include:: /partials/common.rst

.. meta::
   :description: The Magento 2 Integration Extension is available to download in the Magento Marketplace. The extension supports all versions of Magento 2.0 or higher.

Magento 2.x Integration
=======================

.. note::

   To get started, you must have an account created with Talkable, and a Magento Marketplace account.
   If you do not have a Magento Marketplace account configured, follow
   `these steps <http://docs.magento.com/marketplace/user_guide/quick-tour/install-extension.html>`_
   to connect one to your Magento store.

The `Magento 2 Integration Extension`_ is available to download in the Magento Marketplace.
The extension supports all versions of Magento 2.0 or higher.

|page_break|

Installation
------------

1. Visit the Magento Marketplace and get the `Talkable extension`_.

   .. image:: /_static/img/magento2/install0.jpg

2. Follow `Magento Extensions Guide`_ for installation.

|page_break|

Activating the Integration
--------------------------

1. After successful installation, navigate to **System** → **Integrations** page of your admin panel.

   .. image:: /_static/img/magento2/activate1.jpg

2. Find *"Talkable"* in the list of integrations and click the **Activate** link.

   .. image:: /_static/img/magento2/activate2.jpg

3. Review the list of permissions that the Talkable extension needs and click **Allow**.

   .. image:: /_static/img/magento2/activate3.jpg

4. Log in to your Talkable account (if you’re already logged in, this step will be omitted).

   .. image:: /_static/img/magento2/activate4.jpg

|page_break|

5. All done! You have successfully integrated Talkable. To verify your Talkable integration,
   please visit **Integration** tab in **Site Settings**.

   .. image:: /_static/img/magento2/activate5.jpg

.. note::

  Activating the integration allows Talkable to configure your extension automatically.
  If you choose not to activate the integration, you will need to specify your Talkable Site ID in
  the Integration_ section of extension settings.

|page_break|

Accessing Talkable Configuration
--------------------------------

1. To access Talkable extension settings, navigate to **Stores** → **Configuration** in
   your Magento admin panel.

   .. image:: /_static/img/magento2/access1.jpg

2. Then select **Talkable** → **Talkable Configuration** from the list of available configurations.
   If you have multiple stores, select the desired Store View you want to change the settings for.

   .. image:: /_static/img/magento2/access2.jpg

|page_break|

Configuring Talkable Extension
------------------------------

The extension configuration screen consists of three sections: Integration_, Campaigns_ and `Page URLs`_.

   .. image:: /_static/img/magento2/configure1.jpg

|page_break|

Integration
~~~~~~~~~~~

The Integration section allows you to change the Talkable Site ID, which is used to connect your store
to your Talkable account.

   .. image:: /_static/img/magento2/configure2.jpg

.. warning::

   Only change this setting if you need to connect your store to a different site in the Talkable dashboard.
   An incorrect value will prevent your campaigns from showing.

   Changing the Site ID will invalidate the full page cache. Magento will display a warning message with
   a link to the Cache Management page. Please follow this link and refresh the invalidated cache types.

   .. image:: /_static/img/magento2/cache.jpg

.. note::

   If you have activated the extension's integration, the Site ID will be prefilled
   (see `Activating the Integration`_). If you chose not to activate the integration,
   you need to paste the Site ID from your Talkable Site Dashboard into this field.

   .. image:: /_static/img/magento2/configure3.jpg

|page_break|

Campaigns
~~~~~~~~~

The Campaigns section allows you to enable or disable different types of campaigns on your site.
For example, if you don’t have Standalone or Advocate Dashboard campaigns configured in Talkable,
you can disable these campaigns in extension config, so the corresponding pages are not accessible.

.. image:: /_static/img/magento2/configure4.jpg

|page_break|

Page URLs
~~~~~~~~~

The Page URLs section allows you to change paths to the Standalone Share and Advocate Dashboard pages.
The paths must match the placements you have configured in Talkable for this campaign type.
Default values correspond to default placements in Talkable.

.. image:: /_static/img/magento2/configure5.jpg

.. warning::

   Only change these settings if you have configured custom placements for these campaign types
   in your Talkable dashboard. Incorrect values will prevent your Standalone or Dashboard campaign from showing.

.. image:: /_static/img/magento2/configure6.jpg

|page_break|

.. _Talkable extension:
.. _Magento 2 Integration Extension: https://marketplace.magento.com/talkable-magento2-integration.html
.. _Magento Extensions Guide: https://devdocs.magento.com/extensions/install/
