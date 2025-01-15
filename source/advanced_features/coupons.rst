.. _advanced_features/coupons:
.. include:: /partials/common.rst

.. meta::
  :description: You can reward Advocate and their Friend with coupons. Talkable supports both one-time-use coupons as well as multi-use coupons.

Coupons
=======

You can reward |advocate| and their |friend| with coupons. Talkable supports both
one-time-use coupons as well as multi-use coupons. If you are using one-time-use
coupons there is a need to refill a list of coupons within Talkable. You will need
to export a list of coupons or provide a multi-use coupon code creation endpoint.

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

1. Create a coupon list at ``All reports → Coupon Lists`` page
2. Generate a list of coupons on the merchant site using mass coupon generation tool. Check the `Requirements`_ section before generating coupons.
3. Upload generated coupons to coupon list
4. Use a coupon list in the Incentive with "Coupon Code" reward type

.. raw:: html

  <h2>REST API to Create Coupons</h2>

Talkable can create coupons via a webhook using your REST API endpoint.
Read :ref:`Create Coupon Webhook Documentation <web_hooks/create_coupon>` for implementation details.

Shopify coupon auto-sync
------------------------

Read :ref:`Shopify coupon auto-sync documentation <advanced_features/shopify_coupons_auto_sync>` for details.

.. container:: hidden

  .. toctree::

Requirements
------------

Coupons should be unique and 3 to 255 characters long.
All coupons would be converted to uppercase, consider that during code generation, ``fr_coupon`` and ``FR_COUPON`` would be equal.

Only the following characters are allowed in a coupon code:

.. code-block:: text

  A-Z 0-9 - _ / . % : * + @ & #

.. note::
  Spaces are forbidden.

Try to avoid ambiguous characters. This simple solution generates a string of easily readable characters for activation codes.
We do not want people confusing 8 with B, 1 with I, 0 with O, L with 1, etc.

.. code-block:: ruby

  # Generates a random string from a set of easily readable characters
  def generate_activation_code(size = 6)
    charset = ["2", "3", "4", "6", "7", "9", "A", "C", "D", "E", "F", "G", "H", "J", "K", "M", "N", "P", "Q", "R", "T", "V", "W", "X", "Y", "Z"]
    (0...size).map { charset[rand(charset.size)] }.join
  end
