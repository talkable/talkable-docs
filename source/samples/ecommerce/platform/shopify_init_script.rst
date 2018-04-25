.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script type="text/javascript">
    window._talkableq = [['init', {
      site_id: '<YOUR-TALKABLE-SITE-ID>' // REQUIRED - Replace with your Talkable Site ID
    }]];
    {% if customer %}
      _talkableq.push(['authenticate_customer', {
        email:      {{ customer.email }},
        first_name: {{ customer.first_name }},
        last_name:  {{ customer.last_name }}
      }]);
    {% endif %}
    _talkableq.push(['register_affiliate', {}]);
  </script>
  <script src="https://YOUR-PER-CLIENT-INTEGRATION.js" type="text/javascript"></script>
  <!-- End Talkable integration code -->
