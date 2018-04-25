.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script type="text/javascript">
    window._talkableq = [['init', {
      site_id: '<YOUR-TALKABLE-SITE-ID>' // REQUIRED - Replace with your Talkable Site ID
    }]];

    if (Shopify && Shopify.checkout) {
      checkout = Shopify.checkout
      var _talkable_order_items = [];
      for (idx in checkout.line_items) {
        line = checkout.line_items[idx];
        _talkable_order_items.push({
          product_id: line.sku || line.product_id, // REQUIRED - First Item Product ID
          price: line.price, // REQUIRED - First Item Unit Price
          quantity: line.quantity, // REQUIRED - First Item Quantity
          title: line.title, // Optional - Name of product
        });
      }

      var _talkable_data = {
        purchase: {
          order_number: checkout.order_id, // REQUIRED - Order number
          subtotal: checkout.total_price, // REQUIRED - Purchase Subtotal
          coupon_code: checkout.discount ? checkout.discount.code : null,
          items: _talkable_order_items
        },
        customer: {
          email: checkout.email, // REQUIRED - Customer Email Address
          first_name: checkout.billing_address ? checkout.billing_address.first_name : null, // Optional - Customer first name
          last_name: checkout.billing_address ? checkout.billing_address.last_name : null // Optional - Customer last name
        }
      };

      if (checkout.shipping_address) {
        shipping_address = checkout.shipping_address;
        shipping_fields = ['address1', 'address2', 'city', 'province', 'zip', 'country'];
        address = [];

        for (var idx in shipping_fields) {
          address_key = shipping_fields[idx];
          if (shipping_address[address_key]) {
            address.push(shipping_address[address_key]);
          }
        }

        if (shipping_address.zip) {
          _talkable_data.purchase.shipping_zip = shipping_address.zip;
        }
        if (address.length) {
          _talkable_data.purchase.shipping_address = address.join(', ');
        }
      }

      _talkableq.push(['register_purchase', _talkable_data]);
    }
  </script>
  <script async src="YOUR-PER-CLIENT-INTEGRATION" type="text/javascript"></script>
  <!-- End Talkable integration code -->
