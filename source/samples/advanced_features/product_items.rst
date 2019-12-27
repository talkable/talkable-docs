.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || [];
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
        order_number: '', // Required - Unique order number. Example: '100011'
        subtotal: '', // Required - Order subtotal (pre-tax, post-discount). Example: '23.97'
        coupon_code: '', // Coupon code that was used at checkout (pass multiple as an array). Example: 'SAVE20'
        shipping_zip: '', // Used for fraud protection by address. Example: '02222'
        shipping_address: '', // Full address of the order, make sure to strictly follow a format: 'Apt #, Street address, City, State, ZIP, Country'
        items: _talkable_purchase_items // Cart items declared in the example above
      },
      customer: {
        email: '', // Required - Email of the customer who issued a purchase. Example: 'customer@example.com'
        traffic_source: '' // The source of the traffic driven to the campaign. Example: 'facebook'
      }
    };

    window._talkableq.push(['register_purchase', _talkable_data]); // Pass data to Talkable and show Post Purchase campaign as a result
  </script>
  <!-- End Talkable integration code -->
