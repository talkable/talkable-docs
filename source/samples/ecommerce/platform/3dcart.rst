.. code-block:: html

  <!-- Begin Curebit integration code -->
  <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/1.4.1/jquery.js"></script>
  <script type="text/javascript">
    function correctTotalCost (strValue) {
      if (strValue.indexOf(',') >= 0 && strValue.indexOf('.') >= 0) {
        if (strValue.indexOf(',') < strValue.indexOf('.')) {
          strValue = strValue.replace(/,/g, "");
        } else {
          strValue = strValue.replace(/\./g, "");
          strValue = strValue.replace(/,/g, ".");
        }
      }
      return strValue;
    }

    jQuery.noConflict();
    jQuery(document).ready(function() {
      var curebitSiteId = 'YOUR-CUREBIT-SITE-ID'; // Curebit site id
      var curebitJsUrl = '//www.curebit.com/public/' + curebitSiteId + '/purchases/create.js';
      var curebitVersion = '0.2';
      var curebitOrderNumber = '[invoicenum]';
      var curebitEmail = '[oemail]';
      var curebitItems = '';
      var i = 0;
      var curebitProducts = new Array();
      var curebitTemplate = document.body.innerHTML.match(/<!--(START): items-->([\s\S]*?)<!--(END): items-->/ig)[1];
      // fix for subtotal
      var t = '[subtotal]';
      var curebitFindTemplate = curebitTemplate;
      curebitTemplate = curebitTemplate.replace(t, '['+'subtotal'+']');
      // end
      var curebitReplaceTemplate = '';

      /* <!--START: items--> */
      curebitProducts[i] = new Object;
      curebitProducts[i]['product_id'] = '[id]';
      curebitProducts[i]['itemname'] = '[itemname]';
      curebitProducts[i]['price'] = correctTotalCost('[unitprice]'.replace('$', ''));
      curebitProducts[i]['quantity'] = '[numitems]';
      curebitProducts[i]['subtotal'] = '[subtotal]';

      curebitItems += 'p[i][' + i + '][\'product_id\']=' + encodeURIComponent(curebitProducts[i]['product_id']) + '&';
      curebitItems += 'p[i][' + i + '][\'price\']=' + encodeURIComponent(curebitProducts[i]['price']) + '&';
      curebitItems += 'p[i][' + i + '][\'quantity\']=' + encodeURIComponent(curebitProducts[i]['quantity']) + '&';

      var t = curebitTemplate.replace(/\[id\]/i, curebitProducts[i]['product_id']);
      t = t.replace(/\[itemname\]/i, curebitProducts[i]['itemname']);
      t = t.replace(/\[unitprice\]/i, curebitProducts[i]['price']);
      t = t.replace(/\[numitems\]/i, curebitProducts[i]['quantity']);
      t = t.replace(/\[subtotal\]/i, curebitProducts[i]['subtotal']);
      curebitReplaceTemplate = curebitReplaceTemplate + t;
      i++;
      /* <!--END: items--> */
      document.body.innerHTML=document.body.innerHTML.replace(curebitFindTemplate, curebitReplaceTemplate);

      var curebitJsSrc = curebitJsUrl +
        '?v=' + encodeURIComponent(curebitVersion) +
        '&p[\'order_number\']=' + encodeURIComponent(curebitOrderNumber) +
        '&p[\'subtotal\']=' + encodeURIComponent(correctTotalCost('[total]')) +
        '&p[\'email\']=' + encodeURIComponent(curebitEmail) +
        '&' + curebitItems;

      var curebitHeadID = document.getElementsByTagName('head')[0];
      var curebitNewScript = document.createElement('script');
      curebitNewScript.type = 'text/javascript';
      curebitNewScript.src = curebitJsSrc.replace(/\['/gi, "[").replace(/'\]/gi, "]");
      curebitHeadID.appendChild(curebitNewScript);
    });
  </script>
  <!-- End Curebit integration code -->
