.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script type="text/javascript">
    window._talkableq = window._talkableq || [];
    {% if customer %}
      window._talkableq.push(['authenticate_customer', {
        email:        '{{ customer.email }}',
        phone_number: '{{ customer.phone }}',
        first_name:   '{{ customer.first_name }}',
        last_name:    '{{ customer.last_name }}'
      }]);
    {% endif %}
  </script>
  <script async src="//d2jjzw81hqbuqv.cloudfront.net/integration/clients/<YOUR-TALKABLE-SITE-ID>.min.js" type="text/javascript"></script>
  <!-- End Talkable integration code -->
