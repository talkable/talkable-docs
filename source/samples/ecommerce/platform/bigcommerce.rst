.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script type="text/javascript">
    //<![CDATA[
      (function(){function load_js(){var s=document.createElement('script');s.type='text/javascript';s.async=true; s.src='|integration_url|'; var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x)} if(window.attachEvent)window.attachEvent('onload',load_js);else window.addEventListener('load',load_js,false)})();

      var _talkableq = _talkableq || [];
      _talkableq.push(['init', { site_id: 'YOUR-TALKABLE-SITE-ID' }]); /* REQUIRED - Talkable Site ID */

      var _talkable_order_details = {
        order_number: '%%ORDER_ID%%', /* REQUIRED - Order number */
        email: '%%ORDER_EMAIL%%', /* REQUIRED - Customer Email Address */
        subtotal: '%%ORDER_SUBTOTAL_DISCOUNTED%%', /* REQUIRED - Purchase Subtotal */
      };

      _talkableq.push(['register_purchase', _talkable_order_details]);
    //]]>
  </script>
  <!-- End Talkable integration code -->
