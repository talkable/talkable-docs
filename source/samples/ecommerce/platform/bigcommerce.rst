.. code-block:: html

  <!-- Begin Curebit integration code -->
  <script type="text/javascript">
    //<![CDATA[
      (function(){function load_js(){var s=document.createElement('script');s.type='text/javascript';s.async=true; s.src='//d2jjzw81hqbuqv.cloudfront.net/assets/api/all-0.6.js'; var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x)} if(window.attachEvent)window.attachEvent('onload',load_js);else window.addEventListener('load',load_js,false)})();

      var _curebitq = _curebitq || [];
      _curebitq.push(['init', { site_id: 'YOUR-CUREBIT-SITE-ID' }]); /* REQUIRED - Curebit Site ID */

      var _curebit_order_details = {
        order_number: '%%ORDER_ID%%', /* REQUIRED - Order number */
        email: '%%ORDER_EMAIL%%', /* REQUIRED - Customer Email Address */
        subtotal: '%%ORDER_SUBTOTAL_DISCOUNTED%%', /* REQUIRED - Purchase Subtotal */
      };

      _curebitq.push(['register_purchase', _curebit_order_details]);
    //]]>
  </script>
  <!-- End Curebit integration code -->
