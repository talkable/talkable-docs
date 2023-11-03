.. _advanced_features/shopify_purchase_syncing:

.. meta::
  :description: Purchase Syncing is a feature available for Shopify customers integrated with Talkable extension. It allows automatic purchases synchronization from Shopify instead of (or additionally to) passing purchases with Talkable JavaScript integration.

Shopify Purchase Syncing
=========================

Purchase Syncing is a feature available for Shopify customers integrated with Talkable extension.
It allows automatic purchases synchronization from Shopify instead of (or additionally to) passing purchases with Talkable JavaScript integration from a browser.

To access this setting, go to the Shopify Integration page (Settings → Shopify Integration).

.. warning::
  Purchase Syncing currently is not supported for customers who pass to Talkable purchases with Purchase Order Number,
  different from Shopify Purchase ID (Talkable default Shopify integration behavior) as it will lead to double purchases registering.

How it works?
~~~~~~~~~~~~~

It works as a server-to-server integration between Shopify and Talkable using Shopify `orders/create` and `refunds/create` `webhooks <https://shopify.dev/api/admin-rest/2022-04/resources/webhook>`_.

When enabling Purchase Syncing, Talkable creates and subscribes to `orders/create` and `refunds/create` webhooks from the customer's Shopify store. When disabling the setting, the webhook's subscriptions are deleted.

Each time a purchase is placed on a customer's store, Shopify triggers the webhook and Talkable registers the purchase with attributes sent in the webhook’s payload.
Whenever a purchase is refunded on a customer's store, Shopify triggers the refund webhook and Talkable updates the purchase status as refunded. If a purchase has a pending referral and a full refund is issued, the referral will be voided.

Shopify Webhook payload and Talkable Purchase attributes mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Talkable uses next mapping when syncing purchases from Shopify Webhook payload:

.. container:: ptable

  =========================== =====================================================
  Talkable Purchase attribute Shopify Webhook payload (Shopify Purchase attribute)
  =========================== =====================================================
  **Order Number**            `payload.id` (Shopify Purchase ID)
  **Email**                   `payload.email`
  **Subtotal**                `payload.subtotal_price`
  **Taxes**                   `payload.total_tax`
  **Discount Amount**         `payload.total_discounts`
  **Shipping Cost**           `payload.total_shipping_price_set`
  **Items Purchased**         `payload.line_items`
  **Coupon codes**            `payload.discount_codes`
  **IP Address**              `payload.browser_ip`
  **Shipping Address**        `payload.shipping_address` (joined by comma)
  **Shipping Zip**            `payload.shipping_address.zip`
  **Traffic Source**          "purchase-syncing" (constant value)
  **Visitor**                 None (empty)
  =========================== =====================================================

Post Purchase Campaign setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To render Talkable Post Purchase Campaign, there is still a need of registering purchases
with Talkable JavaScript integration (is managed automatically by Talkable).

JavaScript purchase registration has priority over Purchase Syncing and registers the purchase from JavaScript integration first.

In this setup Purchase Syncing is just ensuring that attributes passed with JavaScript integration are aligned with purchases data from Shopify
and notifies Talkable Integrations team in case it is not.

Here is detailed explanation of this logic:

  - Purchase Syncing tries to find Purchase in Talkable by Order Number (Shopify Purchase ID).

  - If there is no such Purchase, the one will be registered with attributes described in `Shopify Webhook payload and Talkable Purchase attributes mapping`

  - If such Purchase exists, Purchase Syncing compares **Email** and **Subtotal** with Shopify Webhook payload.
    In case these attributes differ, Talkable Integrations team will is notified. Otherwise, nothing happens and the existing Purchase data is kept unmodified.
