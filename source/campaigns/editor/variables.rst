.. _campaigns/editor/variables:
.. include:: /partials/common.rst

.. _editor_variables:

Variables
=========

Variables are used to show dynamic data like Campaign tag, Advocate info, etc.
|br|
All Variables are enclosed into ``{{ }}`` which means
`Liquid Output <http://docs.shopify.com/themes/liquid-basics/output>`_.

Each Campaign View has its own set of Variables located inside Editor
navigation:

.. image:: /_static/img/editor/vars-menu-item.png
  :alt: Variables: menu item

|br|

Each Variable is represented with Name, Liquid notation, Value:

.. image:: /_static/img/editor/vars-variable.png
  :alt: Variables: variable

* Name describes meaning of the Variable
* Notation explains how to write Variable inside Template/Styles editor area
* Value shows what this particular Variable results with (Value may be
  different between preview and production scenarious)

|br|
|hr|

{{ advocate_info }}
-------------------

**Available in**: all Views |br|
**Type**: ``Object``

Personal data for Advocate.

.. container:: ptable

  ==================== ========================= =======================================
  Property             Value                     Description
  ==================== ========================= =======================================
  email                "affiliate@example.com"   Advocate email he is registered with
  first_name           "John"                    Advocate first name provided on Signup
  last_name            "Smith"                   Advocate last name provided on Signup
  gender               null | "male" | "female"  Advocate gender provided on Signup
  external_customer_id "1jsh17136"               Advocate unique ID passed by Merchant
                                                 to :ref:`Curebit Integration
                                                 <ecommerce/custom>` as ``customer_id``
  sub_choice           false | true              Advocate custom parameter which can be
                                                 used to pass additional data to
                                                 Advocate Share Page. Passed values
                                                 should be: 0 for false, 1 for true.
  purchases_count      0                         Advocate number of tracked store
                                                 purchases
  ==================== ========================= =======================================

|br|

{{ coupon_code }}
-----------------

**Available in**: Friend Claim Page, Advocate Redemption Email, Advocate Reward
Paid Email |br|
**Type**: ``String``

Coupon Code is given to a person as a Reward based on Incentive (condition of
giving out the Reward).

When you want to use this Variable always keep in mind who you want to
show it to because it has a scope:

* for Views which name starts with ``Advocate`` it means Advocate Coupon Code
* for Views which name starts with ``Friend`` it means Friend Coupon Code

.. image:: /_static/img/editor/vars-friend-coupon-code.png
  :alt: Variables: friend coupon code

|br|

Make sure Incentives are correct:

* If its ``single-use`` Coupon Code, make sure Coupon List exist and it has
  enough coupons and they are valid in terms of uniqueness and validity
* If its ``multi-use`` Coupon Code, make sure it has a correct value

.. image:: /_static/img/editor/vars-coupon-list.png
  :alt: Variables: coupon list

|hr|

