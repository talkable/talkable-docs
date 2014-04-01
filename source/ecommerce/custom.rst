.. _ecommerce/custom:

Default Integration
===================

On your final checkout receipt page (which includes things like the customer's
order number or confirmation code), you will include a Javascript snippet
containing the order and purchased product information. This version of the
Curebit integration code can be asyncronous or syncronous depending on your decision.

The parameters you will need to provide are:

* Order Number
* Order Date and Time (in UTC time zone, or as a timestamp with timezone information)
* Customer Email Address
* Coupon code used at checkout
* Customer ID from your site (Optional)
* Any custom order data you might need (Optional)
* Purchase Subtotal
* Cart items are OPTIONAL. If provided, then for each item:

  * Product ID
  * Item Unit Price
  * Quantity
  * Product Name/Title (Optional)
  * Product URL (Optional)
  * Product Image URL (Optional)

Below is the sample code for a purchase with two items.

.. include:: /partials/note_sample_code.rst

.. raw:: html

   <h2>Main Integration Code</h2>

.. include:: /samples/ecommerce/custom/syncronous.rst

.. include:: /partials/optimizing_for_viewport.rst

.. include:: /partials/verifying_integration.rst

.. container:: hidden

   .. toctree::

