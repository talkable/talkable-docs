.. _android_sdk/integration/post_purchase:
.. include:: /partials/common.rst

Post Purchase Campaign
======================

Now that we know what a Standalone campaign is, let’s take a look at one more type of Talkable
campaign — Post Purchase. It is used to convert your existing customers into Advocates after
they make a purchase.  It has the same flow as a basic Standalone campaign except this is gated
by a purchase and shown to a customer immediately after.

Post Purchase campaign usually looks like a pop up right after a user made a purchase. This
campaign initializes on the order confirmation page and captures order details parameters. You
need to pass order data that includes your customer’s email address, order id, subtotal, coupon
code used at checkout in order to close a referral loop. This allows Talkable to detect and
close the loop on a referral.

Here is an example of a Purchase capturing, this action should be triggered on the order confirmation page:

.. code-block:: java

    Double price = 10.99;
    Integer quantity = 1;
    String productId = "1";
    Item item = new Item(subtotal, quantity, productId);

    Double subtotal = price * quantity; // Required
    Integer orderNumber = 1; // Required
    Date orderDate = Calendar.getInstance().getTime(); // Required
    String coupon = "EXAMPLE-CODE"; // Optional

    Purchase origin = new Purchase(subtotal, orderNumber, orderDate, coupon);
    origin.setCustomer(customer); // Required
    origin.addItem(item); // Optional

    Activity activity = this;
    String campaignTag = "post-purchase";
    Talkable.showOffer(activity, campaignTag, customer);

.. note::

  If Post Purchase campaign does not show up when testing make sure you have it live with a
  default tag on the Campaigns listing.

.. container:: hidden

   .. toctree::
