.. _integration/magento/magento2:
.. include:: /partials/common.rst

.. meta::
   :description: The Magento 2 Integration Extension is available to download in the Magento Marketplace. The extension supports all versions of Magento 2.0 or higher.

Magento 2.x Integration
=======================

.. note::

   To get started, you must have an account created with Talkable, and a Magento Marketplace account.
   If you do not have a Magento Marketplace account configured, follow
   `these steps <https://docs.magento.com/user-guide/magento/magento-marketplace.html#marketplace-credentials>`_
   to connect one to your Magento store.

The `Magento 2 Integration Extension`_ is available to download in the Magento Marketplace.
The extension supports all versions of Magento 2.0 or higher.

|page_break|

Installation
------------

.. note::

   Installation via Composer requires an IT administrator with SSH access to the server where Magento 2 is hosted.
   To install the Talkable extension, you’ll need to execute four commands.

1. Visit the Magento Marketplace and get the `Talkable extension`_.

   .. image:: /_static/img/magento2/install0.jpg

2. Log in to your Magento 2 server and navigate to the root directory of your Magento app from your command line tool.
   This guide shows example outputs for Terminal, but these steps can be modified for any command line tool of your choice.

3. Run the following command to access the latest version of the Talkable extension.

    .. code-block:: bash

       composer require talkable/magento2-integration

4. Run the following command to enable the Talkable extension you just downloaded:

    .. code-block:: bash

       php bin/magento module:enable Talkable_Integration --clear-static-content

   You should see the following output:

    .. code-block::

        The following modules have been enabled:
        - Talkable_Integration

        To make sure that the enabled modules are properly registered, run 'setup:upgrade'.
        Cache cleared successfully.
        Generated classes cleared successfully.
        Please run the 'setup:di:compile' command to generate classes.
        Generated static view files cleared successfully.

5. As displayed in the sample output, you must now enable any additional modules. Run the following command to enable them:

    .. code-block:: bash

        php bin/magento setup:upgrade

6. To ensure that the CSS and JS on your Magento 2 store continues to work properly, you’ll need to run a static content deploy command.

    .. code-block:: bash

        php bin/magento setup:static-content:deploy -f

7. Installation via Composer is complete! You can now return to the Magento admin dashboard from your browser.

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

   You need to paste the Site ID from your Talkable Site Dashboard into this field.

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

.. _Talkable extension:
.. _Magento 2 Integration Extension: https://commercemarketplace.adobe.com/talkable-magento2-integration.html
.. _Magento Extensions Guide: https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/tutorials/extensions.html
