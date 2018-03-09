.. _integration/magento2:
.. include:: /partials/common.rst

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

2. Navigate to **System** |rarr| **Web Setup Wizard** in your Magento store admin panel.

   .. image:: /_static/img/magento2/install1.jpg

3. Choose **Extension Manager**.

   .. image:: /_static/img/magento2/install2.jpg

4. The Extension Manager will indicate that you have extensions ready to be installed.
   Click the **Review and Install** button.

   .. image:: /_static/img/magento2/install3.jpg

5. Click the **Install** button at the top of the list to install all listed extensions.
   To just install Talkable, find the extension in the list and click **Install**.

   .. image:: /_static/img/magento2/install4.jpg

6. Follow the steps to complete the Talkable extension installation.

   .. image:: /_static/img/magento2/install5.jpg

.. warning::

  Take note of `Magento 2.x system requirements`_ regarding extension installation.
  Magento recommends that you have 2GB of RAM allocated to PHP for upgrading and installing
  extensions from the Marketplace.

  Refer to `Troubleshooting`_ section of this guide if you encounter problems during this step.

|page_break|

Activating the Integration
--------------------------

1. After successful installation, navigate to **System** |rarr| **Integrations** page of your admin panel.

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

1. To access Talkable extension settings, navigate to **Stores** |rarr| **Configuration** in
   your Magento admin panel.

   .. image:: /_static/img/magento2/access1.jpg

2. Then select **Talkable** |rarr| **Talkable Configuration** from the list of available configurations.
   If you have multiple stores, select the desired Store View you want to change settings for.

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
The paths must match placements you have configured in Talkable for this campaign type.
Default values correspond to default placements in Talkable.

   .. image:: /_static/img/magento2/configure5.jpg

.. warning::

  Only change these settings if you have configured custom placements for these campaign types
  in your Talkable dashboard. Incorrect values will prevent your Standalone or Dashboard campaign from showing.

   .. image:: /_static/img/magento2/configure6.jpg

|page_break|

Troubleshooting
---------------

This section describes some of the common issues that may be encountered during extension
installation and do not provide helpful error messages or a clear path forward.
If you encounter an issue that isn't described here, please refer to
Magento `troubleshooting suggestions`_ for Component Manager and other Magento documentation.

|nbsp|

* **Check Component Dependency** step fails without error message

  .. image:: /_static/img/magento2/troubleshooting1.jpg

  The Check Component Dependency script has likely ran out of memory.
  Magento 2.x requires at least 756MB of RAM allocated to PHP.
  However to use Web Setup Wizard for system upgrades and extension installation,
  Magento recommends allocating 2GB of memory to PHP. Please refer to `Required PHP Settings`_
  guide and update your configuration.

  |nbsp|

* **Create Backup** step fails without error message

  .. image:: /_static/img/magento2/troubleshooting2.jpg

  Backup creation in Component Manager is performed as a single web request.
  This request can take a long time, especially if you have chosen all three
  backup options (*Code*, *Media* and *Database*). If the backup request takes
  longer to complete than allowed by your server configuration, the server will
  terminate the request, resulting in backup failure.

  |page_break|

  Possible solutions:

  1. Choose to only back up *Code* at the Create Backup step. If you have your own backup procedure
     set up, we recommend performing it prior to installing the extension.

     .. image:: /_static/img/magento2/troubleshooting3.jpg

  2. Configure your server to allow long running requests.

    * In PHP configuration, increase ``max_execution_time`` to 300-600 seconds.
      This can be done either in your ``php.ini`` file, or in the ``.htaccess``
      file in your Magento root folder.

    * For Apache 2, increase ``TimeOut`` to 300-600 seconds in your server configuration.

    * For nginx + php-fpm, set the following directives in your server configuration::

        client_header_timeout 300s;
        client_body_timeout 300s;
        fastcgi_read_timeout 300s;

      .. warning::

        Increased request timeout settings can negatively affect server performance.

.. _Talkable extension:
.. _Magento 2 Integration Extension: https://marketplace.magento.com/talkable-magento2-integration.html
.. _Magento 2.X system requirements: http://devdocs.magento.com/guides/v2.0/install-gde/system-requirements-tech.html
.. _Required PHP Settings: http://devdocs.magento.com/guides/v2.0/install-gde/prereq/php-settings.html
.. _troubleshooting suggestions: http://devdocs.magento.com/guides/v2.0/comp-mgr/trouble/tshoot.html
