.. _integration/custom/recharge:
.. include:: /partials/common.rst

.. meta::
  :description: With Recharge app Talkable clients allow consumers to apply accumulated rewards towards upcoming subscription orders.

Recharge
========

.. note::

   This is a custom integration that can be implemented with extra effort. If you wish to integrate this vendor, please
   contact your Customer Success Manager to apply it to your campaigns.

Recharge allows consumers to apply accumulated rewards towards upcoming subscription orders. Please note this is essentially ‘stacking’ of referral rewards.

Talkable integration with Recharge enables next use cases:

1. Tracking Recharge orders (includes initial, subsequent).

2. Showing the Post Purchase campaign on subscription checkout with the ability to tweak it for Recharge flow specifically

3. Coupon auto-sync.
   |br|
   Talkable will reward with coupons applicable on both Recharge and Shopify checkouts.
   The offer should be equal for both Recharge and Shopify within the same campaign.

4. Coupon auto-apply.
   |br|
   Talkable will try to apply a coupon to the next charge of the customer’s subscription. This coupon will also be sent to the customer’s email in case they want to use it for Shopify instead.
   |br|
   **Version 2**  of the integration also allows for accrued discounts in case the customer refers multiple friends.

5. If the Gleam widget is enabled, it can behave differently depending on the customer’s actions (if it’s set up according to a non-default flow):

   Once the Advocate receives a reward, they will be shown a Gleam widget that will be showing the coupon code as well as a notice that the coupon would be automatically applied to the ongoing subscription if the advocate has the one. The discount is still available for use on regular Shopify flow, but once used it won’t be applied to the subscription of the customer.

.. include:: /partials/contact_us.rst
