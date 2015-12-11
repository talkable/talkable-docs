.. code-block:: html

  <!-- Begin Talkable integration code -->
  <div id="talkable-post-purchase-container"></div>

  <script>
    var _talkableq = _talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // Required - Talkable Site ID, you can find it on the Dashboard inside Talkable upon login
    }]);

    var _talkable_purchase_items = [];

    // Start for loop
    _talkable_purchase_items.push({
      product_id: 'sku1', // Required — Item Product ID
      price: '199.00', // Required — Item Unit Price
      quantity: '1', // Required — Item Quantity
      title: 'Awesome Product', // Optional — Name of product
      url: 'http://www.store.com/product1', // Optional — URL for product
      image_url: 'http://www.store.com/product1/image.jpg' // Optional — URL for product image
    });
    // End for loop

    var _talkable_purchase = {
      order_number: '100011', // Required - Order number
      email: 'customer@example.com', // Required - Customer Email Address
      subtotal: '23.97', // Required - Purchase Subtotal
      coupon_code: 'SAVE20', // Required - Coupon code used at checkout, multiple coupons allowed as JS array: ['SAVE20', 'FREE-SHIPPING']. Pass null if when no coupon code was used at the checkout.
      campaign_template: { name: 'post-purchase' }, // Loads Post Purchase campaign with tag "post-purchase"
      order_items: _talkable_purchase_items,
      first_name: 'Name', // Optional - Customer First Name
      last_name: 'Surname' // Optional - Customer Last Name
    };

    _talkableq.push(['register_purchase', _talkable_purchase]); // Pass data to Talkable and show Post Purchase campaign as a result
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

