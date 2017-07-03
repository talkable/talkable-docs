.. _integration/custom/alternate_post_purchase:
.. include:: /partials/common.rst

Alternate Post Purchase Script for cart line item passing
=========================================================

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    var _talkable_purchase_items = [];

    // Start for loop - iterate through cart and push details for each line item
    _talkable_purchase_items.push({
      product_id: 'sku0001', // Item Product ID
      price: '199.00', // Item Unit Price
      quantity: '1', // Item Quantity
      title: 'Product Name' // Name of product
    });  // End for loop

    var _talkable_data = {
      purchase: {
        order_number: '100011',
        subtotal: '23.97', //pre-tax, post-discount
        coupon_code: 'SAVE20', // can also accept multiple coupons as an array
        items: _talkable_purchase_items,  //cart items
        shipping_zip: '02222',  //optional - used for fraud protection on matching address
        shipping_address: 'Apt #, Street address, City, State, ZIP, Country' //pass full  address details in this order, comma delimited
      },
      customer: {
        email: 'customer@example.com'
      }
    };
    _talkableq.push(['register_purchase', _talkable_data]);
  </script>
  <!-- End Talkable integration code -->
