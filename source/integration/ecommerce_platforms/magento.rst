.. _integration/ecommerce_platforms/magento:
.. include:: /partials/common.rst

.. meta::
   :description: Seamlessly integrate Talkable's referral marketing platform with your Magento 2.x store. Get a powerful, customizable solution to drive customer acquisition and boost sales.

Magento
=======

Talkable offers free extension for Magento 2.4 which allows you to integrate and use Talkable with your Magento store.

Prerequisites
-------------

1.  Magento 2.4

    .. warning::

      Magento 1.x is no longer supported. If you are currently using Magento 1.x, we recommend upgrading to Magento 2.4 to use the Talkable extension.

    To check your Magento version, navigate to your store's admin panel. The version number will be listed in the page footer.

    * For Magento 1.x:

      .. image:: /_static/img/magento/version.png

    * For Magento 2.x:

      .. image:: /_static/img/magento2/version.png

2.  Talkable account

3.  Magento Marketplace account (optional)

    .. note::
      
      This account is required only if you plan to install the extension from the Adobe Commerce Marketplace. If you prefer to install it directly from the command line on your server, this account is not necessary.

    If you do not have a Magento Marketplace account configured, follow 
    `these steps <https://experienceleague.adobe.com/en/docs/commerce-admin/start/commerce-account/commerce-account-create>`_ 
    to connect one to your Magento store.


Installation
------------

From the Adobe Commerce Marketplace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Visit the Magento Marketplace and get the Talkable extension.

   .. image:: /_static/img/magento2/install.jpg


From the command line
~~~~~~~~~~~~~~~~~~~~~

.. note::

   Installation via Composer requires an IT administrator with SSH access to the server where Magento 2 is hosted.

2. Log in to your Magento 2 server and navigate to the root directory of your Magento app from your command line tool.
   This guide shows example outputs for Terminal, but these steps can be modified for any command line tool of your choice.

3. Run the following command to access the latest version of the Talkable extension.
    
   .. code-block:: bash

      composer require talkable/magento2-integration

4. Run the following command to enable the Talkable extension you just downloaded:

   .. code-block:: bash

      php bin/magento module:enable Talkable_Integration --clear-static-content

   You should see the following output:

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

.. _Magento Extensions Guide: https://experienceleague.adobe.com/docs/commerce-operations/installation-guide/tutorials/extensions.html
