.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script type="text/javascript">
    var _talkableq = _talkableq || [];
    _talkableq.push(['init', {site_id: "YOUR-TALKABLE-SITE-ID"}]); /* REQUIRED - Replace with your Talkable Site ID */

    if (Shopify && Shopify.checkout) {
      checkout = Shopify.checkout
      var _talkable_order_items = [];
      for (idx in checkout.line_items) {
        line = checkout.line_items[idx];
        _talkable_order_items.push({
          product_id: line.sku || line.product_id, /* REQUIRED - First Item Product ID */
          price: line.price, /* REQUIRED - First Item Unit Price */
          quantity: line.quantity, /* REQUIRED - First Item Quantity */
          title: line.title, /* Optional - Name of product */
        });
      }

      var _talkable_data = {
        purchase: {
          order_number: checkout.order_id, /* REQUIRED - Order number */
          order_date: checkout.created_at, /* REQUIRED - Order Date and Time (ISO 8601 formatted datetime) */
          email: checkout.email, /* REQUIRED - Customer Email Address */
          subtotal: checkout.total_price, /* REQUIRED - Purchase Subtotal */
          coupon_code: checkout.discount ? checkout.discount.code : null,
          items: _talkable_order_items,
        },
        responsive: true,
      };

      _talkableq.push(['register_purchase', _talkable_data]);
    }
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->
