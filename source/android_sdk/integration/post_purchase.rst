.. _android_sdk/integration/post_purchase:
.. include:: /partials/common.rst

Post Purchase Campaign
======================

Now that we know what a Standalone campaign is, let’s take a look at one more type of Talkable
campaign — Post Purchase. It is used to convert your existing customers into Advocates after
they make a purchase.  It has the same flow as a basic Standalone campaign except this is gated
by a purchase and shown to a customer immediately after it.

Post Purchase campaign usually looks like a pop up right after a user made a purchase. This
campaign initializes on the order confirmation page and captures order details parameters. You
need to pass order data that includes your customer’s email address, order id, subtotal, coupon
code used at checkout in order to close a referral loop. This allows Talkable to detect and
close the loop on a referral.

Here is an example of a Purchase capturing, this action should be triggered on the order confirmation page:

.. code-block:: java

    import com.talkable.sdk.Talkable;
    ...
    Double price = 10.99;
    Integer quantity = 1;
    String productId = "1";
    Item item = new Item(subtotal, quantity, productId);

    Double subtotal = price * quantity; // Required
    Integer orderNumber = 1; // Required
    Date orderDate = Calendar.getInstance().getTime(); // Required
    String coupon = "EXAMPLE-CODE"; // Optional

    Purchase purchase = new Purchase(subtotal, orderNumber, orderDate, coupon);
    purchase.setCustomer(customer); // Required
    purchase.addItem(item); // Optional

    String campaignTag = "android-post-purchase";
    purchase.setCampaignTag(campaignTag); // Optional

    Activity activity = this;
    Talkable.showOffer(activity, purchase, new TalkableErrorCallback<TalkableOfferLoadException>() {
        @Override
        public void onError(TalkableOfferLoadException error) {
            // Error handling. Note that it runs on non UI thread
        }
    });

.. note::

  If Post Purchase campaign does not show up when testing make sure you have it live with
  `android-post-purchase` tag on the Campaigns listing.

.. container:: hidden

   .. toctree::
