.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    var _talkableq = _talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // REQUIRED - Talkable Site ID
      // If you are using live ENV and test ENV you might need to switch over two sites based on current location host:
      // , site_id: window.location.host == "www.site.com" ? 'site' : 'site-testing'
      // , server: 'https://www.talkable.com' // OPTIONAL - use your own domain, that suppose to be setup as alias to talkable.com (this option is only possible for Enterprise client)
    }]);

    var _talkable_order_items = [];
    _talkable_order_items.push({
      product_id: 'sku1', /* Item Product ID */
      price: '199.00', /* Item Unit Price */
      quantity: '1', /* Item Quantity */
      title: 'Awesome Product', /* Name of product */
      url: 'http://www.store.com/product1', /* URL for product */
      image_url: 'http://www.store.com/product1/image.jpg' /* URL for product image */
    });

    _talkable_order_items.push({
      product_id: 'sku2', /* Item Product ID */
      price: '6.00', /* Item Unit Price */
      quantity: '2', /* Item Quantity */
      title: 'Amazing Product', /* Name of product */
      url: 'http://www.store.com/product2', /* URL for product */
      image_url: 'http://www.store.com/product2/image.jpg' /* URL for product image */
    });

    var _talkable_order_details = {
      order_number: '100011', // REQUIRED - Order number
      order_date: '2014-04-15T08:18:44+00:00', // REQUIRED - Order Date and Time (ISO 8601 formatted datetime)
      email: 'customer@example.com', // REQUIRED - Customer Email Address
      subtotal: '23.97', // REQUIRED - Purchase Subtotal
      coupon_code: 'SAVE20', // REQUIRED - Coupon code used at checkout, multiple coupons allowed as JS array: ['SAVE20', 'FREE-SHIPPING']. Pass null if there is no coupon code.
      campaign_tags: ['default'], // REQUIRED - Tag(s) of a campaign that should be shown on a screen as a result of successfully registered purchase
      items: _talkable_order_items, // OPTIONAL - Pass an array with produc items that were included in a shopping cart at checkout
      first_name: 'Name', // OPTIONAL - Customer First Name
      last_name: 'Surname', // OPTIONAL - Customer Last Name
      traffic_source: 'Post-checkout' // OPTIONAL - indicate person traffic source. Can be used as segmentation parameter in reporting.
      // , customer_id: '1234567890' // OPTIONAL - Set to your internal customer ID for tracking
      // , iframe: { // OPTIONAL - make iframe to be placed inline instead of a popup. This gives you ability to style it however needed
      //     container: 'id-example', // OPTIONAL - Tell Talkable where to insert the iframe (this is HTML id attribute value).
      //     width: '100%', // OPTIONAL - These are standard HTML attributes, feel free to add as many you need
      //     height: '800'
      // , } // OPTIONAL - display offer inline instead of popup
      // , loader: 'background: rgba(0, 0, 0, .85) url("//d2jjzw81hqbuqv.cloudfront.net/assets/api/loader.gif") no-repeat center center;' // OPTIONAL - change CSS of loading overlay or disable it completely by using 'display: none;'
      // , person_custom_properties: { // OPTIONAL - Additional customer properties
      //     key1: 'value1', // String value
      //     key2: '123.2' // Numeric value
      // }
    };

    _talkableq.push(['register_purchase', _talkable_order_details]); // Pass Purchase to Talkable
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->


