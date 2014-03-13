.. _ecommerce/custom:

Custom Integration
==================

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

   <h2>Choose Integration Method</h2>

You can track your purchases in Curebit in one of the following ways:

* `Syncronous Method (Recommended)`_
* `Asyncronous Method`_

Finally, you must verify your integration.

Syncronous Method (Recommended)
-------------------------------

.. include:: /samples/ecommerce/custom/syncronous.rst

Asyncronous Method
------------------

.. include:: /samples/ecommerce/custom/asyncronous.rst

.. raw:: html

   <h2>Optimizing for Viewport</h2>

Curebit provides flexibility for the merchant to decide how they want to
optimize mobile.

If your site is responsive, all you'll want to do is set ``responsive: true``.
In your campaign, there are different views for mobile, tablet and desktop.
We'll automatically pull the correct theme view based on the user's device
once we detect the viewport. We'll use our responsive engine to size the
Curebit iframe to the right size. Like Magic! You'll also want to comment out
``device: 'desktop'`` line.

If you have separate mobile, tablet and desktop sites (or any combination of
the three), you can leave ``responsive: true`` on but also specifically set the
campaign theme view to use. This will prevent Curebit from automatically
assigning the theme view to use, but will allow us to resize within the screen
to make sure all elements fit well.

.. raw:: html

   <h2>Setup Your Theme</h2>

Make sure you have this CSS in your campaign theme so it won't have a double
scrollbars on resize (if ``responsive: true``)

.. code:: css

   body { overflow: hidden; }

.. include:: /partials/verifying_integration.rst

.. toctree::
