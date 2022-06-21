.. _advanced_features/shopify_purchases_syncing:

.. meta::
  :description: Purchases Syncing is a feature available for Shopify customers integrated with Talkable extension. It allows automatic purchases synchronization from Shopify instead of (or additionally to) passing purchases with Talkable JavaScript integration.

Shopify Purchases Syncing
=========================

Purchases Syncing is a feature available for Shopify customers integrated with Talkable extension.
It allows automatic purchases synchronization from Shopify instead of (or additionally to) passing purchases with Talkable JavaScript integration from a browser.

To access this setting, go to the Shopify Integration page (Settings → Shopify Integration).

.. warning::
  Purchases Syncing currently is not supported for customers who pass to Talkable purchases with Purchase Order Number,
  different from Shopify Purchase ID (Talkable default Shopify integration behavior) as it will lead to double purchases registering.

How it works?
~~~~~~~~~~~~~

It works as a server-to-server integration between Shopify and Talkable using Shopify `orders/create` `webhook <https://shopify.dev/api/admin-rest/2022-04/resources/webhook>`_.

When enabling Purchases Syncing, Talkable creates and subscribes to this `orders/create` webhook from the customer's Shopify store. When disabling the setting, the webhook and the subscription are deleted.

Each time a purchase is placed on a customer's store, Shopify triggers the webhook and Talkable registers the purchase with attributes sent in the webhook’s payload.

Shopify Webhook payload and Talkable Purchase attributes mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Talkable uses next mapping when syncing purchases from Shopify Webhook payload:

.. container:: ptable

  =========================== =====================================================
  Talkable Purchase attribute Shopify Webhook payload (Shopify Purchase attribute)
  =========================== =====================================================
  **Order Number**            `payload.id` (Shopify Purchase ID)
  **Email**                   `payload.email`
  **Subtotal**                `payload.total_price`
  **Taxes**                   `payload.total_tax`
  **Discount Amount**         `payload.total_discounts`
  **Shipping Cost**           `payload.total_shipping_price_set`
  **Items Purchased**         `payload.line_items`
  **Coupon codes**            `payload.discount_codes`
  **IP Address**              `payload.browser_ip`
  **Shipping Address**        `payload.shipping_address` (joined by comma)
  **Shipping Zip**            `payload.shipping_address.zip`
  **Traffic Source**          "purchases-syncing" (constant value)
  **Visitor**                 None (empty)
  =========================== =====================================================

Post Purchase Campaign setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To render Talkable Post Purchase Campaign, there is still a need of registering purchases
with Talkable JavaScript integration (is managed automatically by Talkable).

JavaScript purchase registration has priority over Purchases Syncing and registers the purchase from JavaScript integration first.

In this setup Purchases Syncing is just ensuring that attributes passed with JavaScript integration are aligned with purchases data from Shopify
and notifies Talkable Integrations team in case it is not.

Here is detailed explanation of this logic:

  - Purchases Syncing tries to find Purchase in Talkable by Order Number (Shopify Purchase ID).

  - If there is no such Purchase, the one will be registered with attributes described in `Shopify Webhook payload and Talkable Purchase attributes mapping`

  - If such Purchase exists, Purchases Syncing compares **Email** and **Subtotal** with Shopify Webhook payload.
    In case these attributes differ, Talkable Integrations team will is notified. Otherwise, nothing happens and the existing Purchase data is kept unmodified.
