.. code-block:: html

  <!-- Begin Curebit integration code -->
  <script>
    //<![CDATA[
      var _curebitq = _curebitq || [];
      _curebitq.push(['init', {
        site_id: 'YOUR-CUREBIT-SITE-ID', // REQUIRED - Curebit Site ID
        server: 'https://www.curebit.com' // OPTIONAL - Use your own domain (enterprise only)
      }]);

      var _curebit_order_items = [];
      _curebit_order_items.push({
        product_id: 'sku1', /* Item Product ID */
        price: '199.00', /* Item Unit Price */
        quantity: '1', /* Item Quantity */
        title: 'Awesome Product', /* Name of product */
        url: 'http://www.store.com/product1', /* URL for product */
        image_url: 'http://www.store.com/product1/image.jpg' /* URL for product image */
      });

      _curebit_order_items.push({
        product_id: 'sku2', /* Item Product ID */
        price: '6.00', /* Item Unit Price */
        quantity: '2', /* Item Quantity */
        title: 'Amazing Product', /* Name of product */
        url: 'http://www.store.com/product2', /* URL for product */
        image_url: 'http://www.store.com/product2/image.jpg' /* URL for product image */
      });

      var _curebit_order_details = {
        order_number: '100011', // REQUIRED - Order number
        order_date: '2010-10-09 03:18:08', // REQUIRED - Order Date and Time (in UTC time zone, or as a timestamp with timezone information)
        email: 'customer@example.com', // REQUIRED - Customer Email Address
        subtotal: '23.97', // REQUIRED - Purchase Subtotal
        coupon_code: 'SAVE20', // REQUIRED - Coupon code used at checkout
        customer_id: '1234567890', // OPTIONAL - Set to your internal customer ID for tracking
        custom_field: null, // OPTIONAL - Any custom order data you might need
        items: _curebit_order_items,
        dont_redeem: false,  // OPTIONAL - Tell curebit that this purchase should not be redeemed
        first_name: 'Name',  // OPTIONAL - Customer First Name
        last_name: 'Surname',  // OPTIONAL - Customer Last Name
        // iframe: { width: '100%', height: '400' }, // OPTIONAL - display offer inline instead of popup
        responsive: true, // OPTIONAL - fit iframe into viewport (also on resize) and allow Curebit display mobile templates
        device: 'desktop', // OPTIONAL - enforce mobile/tablet/desktop view or skip this to allow Curebit choose corresponding template
        campaign_tags: ['default'] // OPTIONAL - Campaign tags used to target specific campaign for offer
      };

      _curebitq.push(['register_purchase', _curebit_order_details]);
    //]]>
  </script>
  <script src="//d2jjzw81hqbuqv.cloudfront.net/assets/api/all-0.6.js" type="text/javascript"></script>
  <!-- End Curebit integration code -->
