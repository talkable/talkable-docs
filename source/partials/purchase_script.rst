.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || [];
    var _talkable_data = {
      purchase: {
        order_number: '', // Required - Unique order number. Example: '100011'
        subtotal: '', // Required - Order subtotal (pre-tax, post-discount). Example: '23.97'
        coupon_code: '', // Coupon code that was used at checkout (pass multiple as an array). Example: 'SAVE20'
        currency_iso_code: '', // Required for multi-currency sites. Example: 'USD'
        shipping_zip: '', // Used for fraud protection by address. Example: '02222'
        shipping_address: '', // Full address of the order, make sure to strictly follow a format: 'Apt #, Street address, City, State, ZIP, Country'
        segment1: '', // Segment 1: Represents custom segment (e.g., location, age group, source channel, platform, gender, interests).
        segment2: '', // Segment 2: Represents custom segment (e.g., location, age group, source channel, platform, gender, interests).
        segment3: '', // Segment 3: Represents custom segment (e.g., location, age group, source channel, platform, gender, interests).
      },
      customer: {
        email: '', // Required - Email of the customer who issued a purchase. Example: 'customer@example.com'
        traffic_source: '' // The source of the traffic driven to the campaign. Example: 'facebook'
      }
    };
    window._talkableq.push(['register_purchase', _talkable_data]);
  </script>
  <!-- End Talkable integration code -->
