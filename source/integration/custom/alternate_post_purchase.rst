.. _integration/custom/alternate_post_purchase:
.. include:: /partials/common.rst

Alternate Post Purchase Script for cart line item passing
=========================================================

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || [];
    var _talkable_purchase_items = [];

    // Start for loop - iterate through cart and push details for each line item
    _talkable_purchase_items.push({
      product_id: '', // Item Product ID. Example: 'sku0001'
      price: '', // Item Unit Price. Example: '199.00'
      quantity: '', // Item Quantity. Example: '1'
      title: '' // Name of a product. Example: 'Product Name'
    });  // End for loop

    var _talkable_data = {
      purchase: {
        order_number: '', // Required - Unique order number. Example: '100011'
        subtotal: '', // Required - Order subtotal (pre-tax, post-discount). Example: '23.97'
        coupon_code: '', // Coupon code that was used at checkout (pass multiple as an array). Example: 'SAVE20'
        currency_iso_code: '', // It is required for multi-currency sites. Example: 'USD'
        items: _talkable_purchase_items,  // Cart items declared in the example above
        shipping_zip: '', // Used for fraud protection by address. Example: '02222'
        shipping_address: '' // Full address of the order, make sure to strictly follow a format: 'Apt #, Street address, City, State, ZIP, Country'
      },
      customer: {
        email: '', // Required - Email of the customer who issued a purchase. Example: 'customer@example.com'
        traffic_source: '' // The source of the traffic driven to the campaign. Example: 'facebook'
      }
    };
    window._talkableq.push(['register_purchase', _talkable_data]);
  </script>
  <!-- End Talkable integration code -->
