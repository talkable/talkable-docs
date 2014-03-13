.. code-block:: html

  <!-- Begin Curebit integration code -->
  <script type="text/javascript">
    //<![CDATA[
      (function(){function load_js(){var s=document.createElement('script');s.type='text/javascript';s.async=true; s.src='//d2jjzw81hqbuqv.cloudfront.net/assets/api/all-0.6.js'; var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x)} if(window.attachEvent)window.attachEvent('onload',load_js);else window.addEventListener('load',load_js,false)})();

      var _curebitq = _curebitq || [];
      _curebitq.push(['init', { site_id: 'YOUR-CUREBIT-SITE-ID' }]); /* REQUIRED - Replace with your Curebit Site ID */
      var _curebit_order_items = [];
      {% for line in line_items %}
        _curebit_order_items.push({
          product_id: '{% if line.sku and line.sku != "" %}{{ line.sku }}{% else %}{{ line.product.id }}{% endif %}', /* REQUIRED - First Item Product ID */
          price: '{{ line.price | money_without_currency }}', /* REQUIRED - First Item Unit Price */
          quantity: '{{ line.quantity }}', /* REQUIRED - First Item Quantity */
          title: '{{ line.title }}', /* Optional - Name of product */
          url: '{{ shop.url }}{{ line.product.url }}', /* Optional - URL for product */
          image_url: '{{ line.product.featured_image | product_img_url }}' /* Optional - URL for product image */
        });
      {% endfor %}

      var couponCodes = [];
      {% for discount in discounts %}
        couponCodes.push('{{ discount.code }}');
      {% endfor %}

      var _curebit_order_details = {
        order_number: '{{ order_number }}', /* REQUIRED - Order number */
        order_date: '{{ created_at }}', /* REQUIRED - Order Date and Time (in UTC time zone, or as a timestamp with timezone information) */
        email: '{{ customer.email }}', /* REQUIRED - Customer Email Address */
        customer_id: '', /* Optional - Set to your internal customer ID for tracking */
        subtotal: '{{ subtotal_price | money_without_currency }}', /* REQUIRED - Purchase Subtotal */
        coupon_code: couponCodes.join(','),
        items: _curebit_order_items
      };

      _curebitq.push(['register_purchase', _curebit_order_details]);
    //]]>
  </script>
  <!-- End Curebit integration code -->
