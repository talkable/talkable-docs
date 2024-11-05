.. _integration/ecommerce_platforms/bigcommerce:
.. include:: /partials/common.rst

.. meta::
   :description: BigCommerce integration allows synchronizing coupons to BigCommerce with webhook support.

BigCommerce Integration
=======================

.. note::

   To begin integration with BigCommerce, you must configure webhook support for coupon synchronization. Additionally, Talkable requires API credentials to enable custom app creation.

The BigCommerce integration allows seamless synchronization of coupons between Talkable and BigCommerce stores, facilitating automated coupon management. Once set up, this integration enables efficient management of marketing campaigns with coupon distribution synced to BigCommerce.

**Endpoint for Coupon Auto-Sync Support:**
|br|
`<https://esp.talkable.com/bigcommerce>`_

**Extras configuration for auto-sync support**

.. code-block:: javascript

   const extras = {
     ids: [205],
     entity: "categories",
     client_id: "sdc0k1m5************0kj4vs6tdxgju",
     store_hash: "1**0**qymg",
     access_token: "76jczj75*******boq9dp4p73ypgbt7x4"
   };

Webhook Support
---------------
Coupon creation is supported through webhook configuration, ensuring automated and up-to-date coupon syncing.
