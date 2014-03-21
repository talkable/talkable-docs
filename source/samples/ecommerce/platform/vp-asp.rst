.. code::

      'Begin Curebit integration code
  dim strordertime, strorderdate, xcurebiturl
  strordertime = rsorder("otime")
  strorderdate = formatdatetime(strordertime,vblongtime)
  xcurebiturl = "https://curebit.com/public/YOUR-CUREBIT-SITE-ID/purchases/create.js"
  %>
  <script type="text/javascript" src="<%=xcurebiturl%>?v=0.2&purchase[order_number]=<%=ordernumber%>&purchase[subtotal]=<%=getsess("OrderTotal")%>&purchase[email]=<%=GetSess("email")%>&purchase[order_date]=<%=strorderdate%>"& >
  </script>
  <%
  'End Curebit integration code
