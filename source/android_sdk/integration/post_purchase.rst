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

  import com.talkable.*;
  ...
  String orderNumber = "100130";
  String orderDate = new Date();
  String email = "customer@example.com";
  double subtotal = 24.95;
  String couponCode = "TEST25";

  String productID = "sku3";
  double priceKey = 4.99;
  int quantity = 5;
  OrderItem[] orderItems = {new OrderItem(productID, price, quantity)};
  Purchase purchase = new Purchase(orderNumber, orderDate, email, subtotal, coupon, orderItems)

  RegisteredOrigin registeredOrigin = Talkable.registerOrigin(purchase);

.. note::

  If Post Purchase campaign does not show up when testing make sure you have it live with a
  default tag on the Campaigns listing.

.. include:: /partials/android_webview.rst

.. container:: hidden

   .. toctree::
