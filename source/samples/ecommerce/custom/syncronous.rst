.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    var _talkableq = _talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // REQUIRED - Talkable Site ID, you can find it on the Dashboard inside Talkable upon login
    }]);

    var _talkable_purchase = {
      order_number: '100011', // REQUIRED - Order number
      email: 'customer@example.com', // REQUIRED - Customer Email Address
      subtotal: '23.97', // REQUIRED - Purchase Subtotal
      coupon_code: 'SAVE20', // REQUIRED - Coupon code used at checkout, multiple coupons allowed as JS array: ['SAVE20', 'FREE-SHIPPING']. Pass null if when no coupon code was used at the checkout.
      first_name: 'Name', // OPTIONAL - Customer First Name
      last_name: 'Surname' // OPTIONAL - Customer Last Name
    };

    _talkableq.push(['register_purchase', _talkable_purchase]); // Pass data to Talkable and show Post Purchase campaign as a result
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

