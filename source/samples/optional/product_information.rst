.. code-block:: html

  <!-- Begin Curebit product integration code -->
  <script src="//d2jjzw81hqbuqv.cloudfront.net/assets/api/all-0.6.js" type="text/javascript"></script>
  <script type="text/javascript">
    curebit.init({site_id: 'YOUR-CUREBIT-SITE-ID'});

    var products = [
      {
        url: 'http://www.merchant.com/ProductPage1.htm', /* REQUIRED */
        image_url: 'http://www.merchant.com/Image1.jpg', /* REQUIRED */
        title: 'Awesome Item', /* REQUIRED */
        product_id: '12345', /* REQUIRED */
        price: '19.99' /* OPTIONAL */
      },
      {
        url: 'http://www.merchant.com/ProductPage2.htm', /* REQUIRED */
        image_url: 'http://www.merchant.com/Image2.jpg', /* REQUIRED */
        title: 'Sweet Item', /* REQUIRED */
        product_id: '67890', /* REQUIRED */
        price: '10.23' /* OPTIONAL */
      }
    ];

    curebit.register_products(products);
  </script>
  <!-- End Curebit product integration code -->
