.. code-block:: html

  <!-- Begin Talkable integration code -->
  <div id="talkable-offer"></div>

  <script>
    var _talkable_data = {
      purchase: {
        order_number: '100011', // Required - Order number
        subtotal: '23.97', // Required - Purchase Subtotal
        coupon_code: 'SAVE20' // Required - Coupon code used at checkout, multiple coupons allowed as JS array: ['SAVE20', 'FREE-SHIPPING']. Pass null if when no coupon code was used at the checkout.
      },
      customer: {
        email: 'customer@example.com' // Required - customer email
      },
      campaign_tags: ['post-purchase'] // Loads Post Purchase campaign with tag "post-purchase"
    };

    _talkableq.push(['register_purchase', _talkable_data]); // Pass data to Talkable and show Post Purchase campaign as a result
  </script>
  <!-- End Talkable integration code -->
