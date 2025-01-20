.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || [];
    var _talkable_purchase_items = [];

    // Start for loop
    _talkable_purchase_items.push({
      product_id: '', // Required — Item Product ID. Example: 'sku0001'
      price: '', // Required — Item Unit Price. Example: '199.00'
      quantity: '', // Required — Item Quantity. Example: '1'
      title: '', // Optional — Name of product. Example: 'Product Name'
      url: '', // Optional — URL for product. Example: 'http://www.store.com/product1'
      image_url: '' // Optional — URL for product image. Example: 'http://www.store.com/product1/image.jpg'
    });
    // End for loop

    var _talkable_data = {
      purchase: {
        order_number: '', // Required - Unique order number. Example: '100011'
        subtotal: '', // Required - Order subtotal (pre-tax, post-discount). Example: '23.97'
        coupon_code: '', // Coupon code that was used at checkout (pass multiple as an array). Example: 'SAVE20'
        currency_iso_code: '', // Required for multi-currency sites. Example: 'USD'
        shipping_zip: '', // Used for fraud protection by address. Example: '02222'
        shipping_address: '', // Full address of the order, make sure to strictly follow a format: 'Apt #, Street address, City, State, ZIP, Country'
        items: _talkable_purchase_items // Cart items declared in the example above
        segment1: '', // Segment 1: Represents custom segment (e.g., location, age group, source channel, platform, gender, interests).
        segment2: '', // Segment 2: Represents custom segment (e.g., location, age group, source channel, platform, gender, interests).
        segment3: '', // Segment 3: Represents custom segment (e.g., location, age group, source channel, platform, gender, interests).
      },
      customer: {
        email: '', // Required - Email of the customer who issued a purchase. Example: 'customer@example.com'
        traffic_source: '', // The source of the traffic driven to the campaign. Example: 'facebook'
        phone_optin: true, // To subscribe customer with phone number. Requires to pass phone number if value is true
        sub_choice: true // To subscribe customer
      }
    };

    window._talkableq.push(['register_purchase', _talkable_data]); // Pass data to Talkable and show Post Purchase campaign as a result
  </script>
  <!-- End Talkable integration code -->
