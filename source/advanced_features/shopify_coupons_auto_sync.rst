.. _advanced_features/shopify_coupons_auto_sync:

.. meta::
  :description: Talkable supports coupon auto-sync for Shopify. This feature allows to avoid manual coupon uploads and/or Shopify Discount management.

Shopify coupon auto-sync
========================

Talkable supports coupon auto-sync for Shopify. This feature allows the automation of code creation and management of Shopify Discounts, rather than manual code creation and upload to the Talkable Platform.

.. note::
  Shopify coupon auto-sync and :ref:`Coupon Webhook <web_hooks/create_coupon>` can be enabled simultaneously.
  In that case, coupons will be passed via the webhook only after successful Shopify sync.

Get started
-----------

Before using coupon auto-sync, you’ll need to install the Talkable Shopify app (Settings → Shopify Integration → Authorize).

To enable coupon auto-sync in a coupon list, go to the coupon list edit/create page (All reports → Coupon lists) and check "Enable Coupon List Shopify Auto-Sync".
If this checkbox is disabled (you are unable to check/uncheck it), it means that your user doesn't have rights for this site or Shopify Integration is not authorized.

.. note::
  Talkable uses a Shopify Discount ID (if present) to determine where to upload newly generated coupons. It is recommended to leave it blank when creating coupon lists. If blank, Talkable will create a Discount based on coupon list configuration and store its ID in the coupon list.
  When you try to create a coupon list with a 100% discount you have to provide a Discount ID manually. That was made for preventing mistakes in the Discount setup.

  Please see **Advanced features** for more information about Shopify Discount ID.


What is a Discount?
~~~~~~~~~~~~~~~~~~~

A Discount is the closest thing to Talkable coupon lists in Shopify. It defines the properties and applicability of associated coupon codes. You can read more on the Shopify site `here <https://shopify.dev/docs/api/admin-graphql/latest/objects/DiscountCodeBasic>`_.

What attributes will the auto-generated Discount have?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Talkable applies the below coupon list settings onto the Discount:

.. container:: ptable

  ===================== ======================================== ======================================
  Coupon list attribute Discount attribute (as in API)           Discount attribute (as in interface)
  ===================== ======================================== ======================================
  **Amount**            `customerGets.value`                     Value
  **Discount type**     `customerGets.value.percentage` or       Type
                        `customerGets.value.discountAmount`
  **Expiration date**   `endsAt`                                 End date
  **Minimum subtotal**  `minimumRequirement.subtotal`            Minimum purchase amount
                        `.greaterThanOrEqualToSubtotal`
  ===================== ======================================== ======================================

Some other Discount attributes that we set when generating the Discount:

.. container:: ptable

  ============================= ============================= =============================================
  Discount attribute            Value                         Attribute effect
  ============================= ============================= =============================================
  `title`                       e.g. "Talkable                Describes the Discount.
                                single-use coupons $10"
  `customerGets.items`          `{ all: true }`               The discount applies to all items in
                                                              the cart. Can be restricted to specific
                                                              products or collections.
  `customerGets.value`          `{ percentage: 0.1 }` or      Discount value - either percentage
                                `{ discountAmount: {...} }`   (0.0-1.0) or fixed amount.
  `appliesOncePerCustomer`      `false`                       Allows the customer to use discount
                                                              multiple times.
  `usageLimit`                  `1`                           Each discount code can be used exactly once.
  `customerSelection`           `{ all: true }`               The discount is valid for all customers.
                                                              Can be restricted to specific customers
                                                              or customer segments.
  `startsAt`                    Time of coupon list           The date and time when the discount starts.
                                creation
  ============================= ============================= =============================================


Why aren't there any coupons created for my auto-synced list?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Auto-sync generates and uploads coupons when there is demand for them. That means that nothing will happen until the first reward is requested from a specific coupon list. When this happens, Talkable will generate a code and sync it with Shopify, while scheduling a refill task that will generate a set of codes in advance. This logic is triggered every time a coupon is issued, so there  will always be some coupons available for future rewards.

Advanced features
-----------------

Shopify Discount ID
~~~~~~~~~~~~~~~~~~~

Talkable allows you to assign a custom Discount ID to a coupon list. This might be helpful if you want to deviate from our default Discount settings, e.g. restrict codes to a group of customers or group of products.

It is recommended to create a new Discount in Shopify if there is a need to use a custom one, instead of editing the Discount generated by Talkable.

.. warning::
  Talkable validates the Discount attached to a coupon list. There are certain Discount attributes that must match the coupon list configuration.
  These include:

  `Applies once per customer` - must be `false` (amount split across items)

  `Value` - must correspond to coupon list amount

  `Type` - must correspond to coupon list type

  `Ends At` - must be greater than or equal to coupon list expiration (and absent if coupon list has no expiration)

  `Minimum Subtotal` - must match coupon list minimum subtotal

If the Discount passes validation, it can be attached to a coupon list and will be used as a new destination for all the coupons created from that moment on.

.. note::
  All previously generated coupons will retain the attributes of the Discount that was used at the point at which they were created (auto-synced).

Shopify Discount Changed Email Notification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you modify a Discount on Shopify, it could make them incompatible with the coupon lists they are attached to. In order to find out about such changes as early as possible, we have a daily monitoring job that checks that Discounts have no critical differences from respective coupon lists.

Attributes that are checked in this job are the following:

- `customerGets.value.appliesOnEachItem` - must always be `false`
- `usageLimit` - must always be 1
- `customerGets.value` - must correspond to coupon list amount
- `customerGets.value.percentage` or `customerGets.value.discountAmount` - must correspond to coupon list type
- `endsAt` - must be greater than or equal to coupon list expiration (and absent if coupon list has no expiration)

If any of these attributes differ from what they are expected to be and Talkable cannot fix that by updating a coupon list (see **Coupon list sync**), Talkable sends an email notification.

Once the Discount becomes critically different from the coupon list it is assigned to, the coupon list is no longer editable. Please fix the issues listed in the email notification to remedy this situation.

Coupon list sync
~~~~~~~~~~~~~~~~

Talkable tries to keep up with the Discounts assigned to coupon lists when/if Discounts change.

As long as the Discount is otherwise valid for a coupon list, we update the coupon list's:

- **expiration date** - only if Discount end date is further in the future (or absent)
- **minimum subtotal**
- **entitled products**
- **entitled collections**

.. note::
  If there are any other changes in the Discount that make it not suitable for a certain coupon list, we won't sync the coupon list. In this case, a Shopify Discount Changed Email Notification will be delivered and action will be required to fix the issue.

  This sync is performed daily. Do not expect an immediate change to be reflected after a Discount update.
