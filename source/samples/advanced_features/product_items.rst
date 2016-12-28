.. code-block:: html

  <!-- Begin Talkable integration code -->
  <div id="talkable-offer"></div>

  <script>
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

    var _talkable_data = {
      purchase: {
        order_number: '100011', // Required - Order number
        subtotal: '23.97', // Required - Purchase Subtotal
        coupon_code: 'SAVE20', // Required - Coupon code used at checkout, multiple coupons allowed as JS array: ['SAVE20', 'FREE-SHIPPING']. Pass null if when no coupon code was used at the checkout.
        items: _talkable_purchase_items
      }
    };

    _talkableq.push(['register_purchase', _talkable_data]); // Pass data to Talkable and show Post Purchase campaign as a result
  </script>
  <!-- End Talkable integration code -->
