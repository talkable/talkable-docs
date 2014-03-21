.. code-block:: html

  <!-- Begin Curebit integration code -->
  <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.js"></script>
  <script type="text/javascript">
    jQuery.noConflict();
    jQuery(document).ready(function() {
      var curebitSiteId = 'YOUR-CUREBIT-SITE-ID'; // Curebit Site ID
      var curebitJsUrl = 'https://curebit.com/public/' + curebitSiteId + '/purchases/create_yahoo.js';
      var curebitVersion = '0.2';
      var curebitOrderNumber = orderNum;

      var curebitI = 0;
      var curebitItems = '';
      for (curebitI = 0; curebitI < ids.length; curebitI++) {
        curebitItems += 'purchase[items_attributes][' + curebitI + '][product_id]=' + encodeURIComponent(ids[curebitI]) + '&';
        curebitItems += 'purchase[items_attributes][' + curebitI + '][price]=' + encodeURIComponent(price[curebitI]) + '&';
        curebitItems += 'purchase[items_attributes][' + curebitI + '][quantity]=' + encodeURIComponent(qtys[curebitI]) + '&';
      }

      var str = jQuery('#ys_billToEmail').text() + jQuery('#ys_paypalConfirm').text();
      var curebitEmail = ""; // if no match, use this
      var emailsArray = str.match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+.[A-Z]{2,4}/i);
      if (emailsArray) curebitEmail = emailsArray[0];

      var curebitJsSrc = curebitJsUrl +
        '?v=' + encodeURIComponent(curebitVersion) +
        '&purchase[order_number]=' + encodeURIComponent(curebitOrderNumber) +
        '&purchase[subtotal]=' + encodeURIComponent(orderSubTotal) +
        '&purchase[email]=' + encodeURIComponent(curebitEmail) +
        '&' + curebitItems;

      var curebitHeadID = document.getElementsByTagName('head')[0];
      var curebitNewScript = document.createElement('script');
      curebitNewScript.type = 'text/javascript';
      curebitNewScript.src = curebitJsSrc;
      curebitHeadID.appendChild(curebitNewScript);
    });
  </script>
  <!-- End Curebit integration code -->
