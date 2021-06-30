.. _advanced_features/shopify_coupons_auto_sync:

.. meta::
  :description: Talkable supports coupon auto-sync for Shopify. This feature allows to avoid manual coupon uploads and/or Shopify Price Rule management.

Shopify coupon auto-sync
========================

Talkable supports coupon auto-sync for Shopify. This feature allows the automation of code creation and management of Shopify Price Rules, rather than manual code creation and upload to the Talkable Platform.

Get started
-----------

Before using coupon auto-sync, you’ll need to install the Talkable Shopify app (Settings → Shopify Integration → Authorize).

To enable coupon auto-sync in a coupon list, go to the coupon list edit/create page (All reports → Coupon lists) and check "Enable Coupon List Shopify Auto Sync". If this checkbox is disabled (you are unable to check/uncheck), it means this site already uses the :ref:`Coupon Webhook <web_hooks/create_coupon>` and will be created automatically — no coupons can be directly uploaded to Shopify. Instead, coupons are delivered to Coupon Webhook URL, and should be handled from there. If you’d like to turn on/off Shopify auto-sync, you’ll need to first disable the Coupon Webhook.

.. note::
  Talkable uses a Shopify Price Rule ID (if present) to determine where to upload newly generated coupons. It is recommended to leave it blank when creating coupon lists. If blank, Talkable will create a Price Rule based on coupon list configuration and store its ID in the coupon list. Please see **Advanced features** for more information about Shopify Price Rule ID.


What is Price Rule?
~~~~~~~~~~~~~~~~~~~

A price rule is the closest thing to Talkable coupon lists in Shopify. It defines the properties and applicability of associated coupon codes. You can read more on the Shopify site `here <https://shopify.dev/docs/admin-api/rest/reference/discounts/pricerule>`_.

What attributes will the auto-generated Price Rule have?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Talkable applies the below coupon list settings onto Price Rule:

.. container:: ptable

  ===================== =================================== ======================================
  Coupon list attribute Price rule attribute (as in API)    Price rule attribute (as in interface)
  ===================== =================================== ======================================
  **Amount**            `value`                             Value
  **Discount type**     `value_type`                        Type
  **Expiration date**   `ends_at`                           End date
  **Minimum subtotal**  `prerequisite_subtotal_range`       Minimum purchase amount
  ===================== =================================== ======================================

Some other Price Rule attributes that we set when generating Price Rule:

.. container:: ptable

  ======================== ======================= =============================================
  Price Rule attribute     Value                   Attribute effect
  ======================== ======================= =============================================
  `title`                  e.g. "Talkable          Describes Price Rule.
                           single-use coupons $10"
  `target_type`            `line_item`             The price rule applies to the cart's line
                                                   items.
  `target_selection`       `all`                   The price rule applies the discount to all
                                                   line items in the checkout.
  `allocation_method`      `across`                The calculated discount amount will be
                                                   applied across the entitled items.
                                                   For example, for a price rule that takes
                                                   $15 off, the discount will be applied across
                                                   all the entitled items.
  `usage_limit`            `1`                     Each discount code can be used exactly once.
  `customer_selection`     `all`                   The price rule is valid for all customers.
  `starts_at`              Time of coupon list     The date and time when the price rule starts.
                           creation
  ======================== ======================= =============================================


Why aren't there any coupons created for my auto-synced list?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auto-sync generates and uploads coupons when there is demand for them. That means that nothing will happen until the first reward is requested from a specific coupon list. When this happens, Talkable will generate a code and sync it with Shopify, while scheduling a refill task that will generate a set of codes in advance. This logic is triggered every time a coupon is issued, so there  will always be some coupons available for future rewards.

Advanced features
-----------------

Shopify Price Rule ID
~~~~~~~~~~~~~~~~~~~~~

Talkable allows you to assign a custom Price Rule ID to a coupon list. This might be helpful if you want to deviate from our default Price Rule settings, e.g. restrict codes to a group of customers or group of products.

It is recommended to create a new Price Rule in Shopify if there is a need to use a custom one, instead of editing the Price Rule generated by Talkable.

.. warning::
  Talkable validates the Price Rule attached to a coupon list. There are certain Price Rule attributes that must match the coupon list configuration.
  These include:

  `value` - must correspond to coupon list amount

  `value_type` - must correspond to coupon list type

  `ends_at` - must be greater than or equal to coupon list expiration (and absent if coupon list has no expiration)

  `prerequisite_subtotal_range` - must match coupon list minimum subtotal

If the Price Rule passes validation, it can be attached to a coupon list and will be used as a new destination for all the coupons created from that moment on.

.. note::
  All previously generated coupons will retain the attributes of the Price Rule that was used at the point at which they were created (auto-synced).

Shopify Price Rule Changed Email Notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you modify a Price Rules on Shopify, it could make them incompatible with the coupon lists they are attached to. In order to find out about such changes as early as possible, we have a daily monitoring job that checks that Price Rules have no critical differences from respective coupon lists.

Attributes that are checked in this job are the following:

  - `usage_limit` - must always be 1

  - `value` - must correspond to coupon list amount

  - `value_type` - must correspond to coupon list type

  - `ends_at` - must be greater than or equal to coupon list expiration (and absent if coupon list has no expiration)

  - `prerequisite_subtotal_range` - must match coupon list minimum subtotal

If any of these attributes differ from what they are expected to be and Talkable cannot fix that by updating a coupon list (see **Coupon list sync**), Talkable sends an email notification.

Once the Price Rule becomes critically different from the coupon list it is assigned to, the coupon list is no longer editable. Please fix the issues listed in the email notification to remedy this situation.

Coupon list sync
~~~~~~~~~~~~~~~~

Talkable tries to keep up with the Price Rules assigned to coupon lists when/if Price Rules change.

As long as the Price Rule is otherwise valid for a coupon list, we update the coupon list’s:

**expiration date** - only if Price Rule end date is further in the future (or absent)

**minimum subtotal**

.. note::
  If there are any other changes in the Price Rule that make it not suitable for a certain coupon list, we won’t sync the coupon list. In this case, a Shopify Price Rule Changed Email Notification will be delivered and action will be required to fix the issue.

  This sync is performed daily. Do not expect an immediate change to be reflected  after a Price Rule update.
