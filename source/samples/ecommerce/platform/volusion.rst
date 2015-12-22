.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script type="text/javascript">
    if (typeof Order != 'undefined') {
      (function(){function load_js(){var s=document.createElement('script');s.type='text/javascript';s.async=true; s.src='|integration_url|'; var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x)} if(window.attachEvent)window.attachEvent('onload',load_js);else window.addEventListener('load',load_js,false)})();

      var _talkableq = _talkableq || [];
      _talkableq.push(['init', { site_id: 'YOUR-TALKABLE-SITE-ID' }]); /* REQUIRED - Talkable Site ID */
      var _talkable_order_items = [];

      $.each(OrderDetails, function() {
        _talkable_order_items.push({
          url: 'http://' + window.location.host + '/ProductDetails.asp?ProductCode=' + this[2],
          image_url: 'http://' + window.location.host + '/v/vspfiles/photos/' + this[2] + '-1.jpg',
          title: this[3],
          product_id: this[2],
          price: this[5],
          quantity: this[6]
        });
      });

      var _talkable_data = {
        purchase: {
          order_number: Order[0],
          email: Order[9],
          subtotal: Order[3],
          items: _talkable_order_items
        }
      };

      _talkableq.push(['register_purchase', _talkable_data]);
    }
  </script>
  <!-- End Talkable integration code -->
