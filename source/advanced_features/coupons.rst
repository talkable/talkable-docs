.. _advanced_features/coupons:
.. include:: /partials/common.rst

.. meta::
   :description: You can reward Advocate and their Friend with coupons. Talkable supports both one-time-use coupons as well as multi-use coupons.

Automatic Coupon Creation
=========================

You can reward |advocate| and their |friend| with coupons. Talkable supports both
one-time-use coupons as well as multi-use coupons. If you are using one-time-use
coupons there is a need to refill a list of coupons within Talkable. You will need
to export a list of coupons or provide a multi-use coupon code creation end point.

Multi-use Coupons
-----------------

Multi-use Coupons can be given to Talkable customers as a reward by create an Incentive with reward type "Coupon".
It can be done from Campaign Rules page.

Multi-use coupon will be given to any customer that perfomed action that matcher Incentive Reward Criteria.

Single-use Coupons
------------------

In case you want to give a unique coupon to each customer, you may attach a coupon list to campaign incentive.
In this case each, customer will receive unique coupon code from the pool available in coupon list.

There are several steps that need to be taken for this scenario:

1. Create a coupon list at "Manage Coupon Lists" page
2. Generate a list of coupons on the merchant site using mass coupon generation tool
3. Upload generated coupons to coupon list
4. Use a coupon list in the Incentive with "Coupon Code" reward type

.. raw:: html

   <h2>REST API to Create Coupons</h2>

Talkable can create coupons via a webhook using your REST API end point.
Read :ref:`Create Coupon Webhook Documentation <web_hooks/create_coupon>` for implementation details.

.. container:: hidden

   .. toctree::
