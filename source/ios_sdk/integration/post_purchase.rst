.. _ios_sdk/integration/post_purchase:
.. include:: /partials/common.rst

Post Purchase Campaign
======================

Now that we know what a Standalone campaign is, let’s take a look at one more type of Talkable campaign — Post Purchase. It is used to convert your existing customers into Advocates after they make a purchase.  It has the same flow as a basic Standalone campaign except this is gated by a purchase and shown to a customer immediately after.

Post Purchase campaign usually looks like a pop up right after a user made a purchase. This campaign is initialized on the order confirmation page and captures order with it's details. You need to pass order data to Talkable that includes your customer’s email address, order number, subtotal, coupon code used at checkout to allow Talkable detect and close a referral loop.

Here is an example of a Purchase capturing, this action should be triggered on the order confirmation page:

.. code-block:: objc

   @import TalkableSDK;
   ...
   NSDictionary* params = @{
     TKBLPurchaseKey: @{
       TKBLPurchaseOrderNumberKey: @"100130", // REQUIRED - Order number
       TKBLPurchaseEmailKey: @"customer@example.com", // REQUIRED - Customer Email
       TKBLPurchaseSubtotalKey: [NSNumber numberWithDouble:22.33], // REQUIRED - Purchase Subtotal
       TKBLPurchaseCouponCodeKey: @"TEST25", // REQUIRED - Coupon code used at checkout, pass multiple as an array: @[@"SAVE20", @"FREE-SHIPPING"]. Pass @"" if there is no coupon code.
       TKBLPurchaseOrderItemsKey:@[
         @{
           TKBLPurchaseOrderItemProductIDKey: @"sku3", // Item Product ID
           TKBLPurchaseOrderItemPriceKey: [NSNumber numberWithDouble:4.99], // Item Unit Price
           TKBLPurchaseOrderItemQuantityKey: [NSNumber numberWithUnsignedInt:5], // Item Quantity
           TKBLPurchaseOrderItemTitleKey: @"Amazing Product 3", // Name of the product
           TKBLPurchaseOrderItemUrlKey: @"http://www.store.com/product2", // URL of the product page
           TKBLPurchaseOrderItemImageUrlKey: @"http://www.store.com/product2/image.jpg" // URL of the product image
         }
       ]
     }
   };
   ...
   [[Talkable manager] registerOrigin:TKBLPurchase params:params];

.. note::

  If Post Purchase campaign does not show up when testing, make sure you have it
  Live on the Campaigns listing with a default tag (`ios-post-purchase`) or with
  a tag you specified in the `registerOrigin` call.

.. container:: hidden

   .. toctree::
