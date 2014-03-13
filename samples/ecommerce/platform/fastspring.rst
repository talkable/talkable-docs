.. code-block:: html

  <!-- Begin Curebit integration code -->
  <script type="text/javascript">
    <![CDATA[
      var curebitSiteId = 'YOUR-CUREBIT-SITE-ID';
      var curebitJsUrl = 'https://curebit.com/public/' + curebitSiteId + '/purchases/create_fastspring.js';
      var curebitVersion = '0.2';
      var curebitOrderNumber = "#{order.reference}";

      var curebitI = 0;
      var curebitItems = '';
    ]]>

    <repeat value="#{order.allItems}" var="orderItem">
      <![CDATA[
        curebitItems += 'purchase[items_attributes][' + curebitI + '][product_id]=' + '#{orderItem.productName}' + '&';
        curebitItems += 'purchase[items_attributes][' + curebitI + '][price]=' + '#{orderItem.priceTotal.value}' + '&';
        curebitItems += 'purchase[items_attributes][' + curebitI + '][quantity]=' + '#{orderItem.quantity}' + '&';
        curebitI++;
      ]]>
    </repeat>

    <![CDATA[
      var curebitJsSrc = curebitJsUrl +
        '?v=' + encodeURIComponent(curebitVersion) +
        '&purchase[order_number]=' + curebitOrderNumber +
        '&purchase[subtotal]=' + '#{order.subTotal.value}' +
        '&purchase[order_date]=' + '#{order.created}' +
        '&purchase[email]=' + '#{order.customer.email}' +
        '&' + curebitItems;

      var curebitHeadID = document.getElementsByTagName('head')[0];
      var curebitNewScript = document.createElement('script');
      curebitNewScript.type = 'text/javascript';
      curebitNewScript.src = curebitJsSrc;
      curebitHeadID.appendChild(curebitNewScript);
    ]]>
  </script>
  <!-- End Curebit integration code -->
