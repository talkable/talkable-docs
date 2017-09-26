In order to integrate Talkable campaign(s) on your site you need to set the following script into HEAD tag inside
your main layout which is used on every page. This is initialization of the Talkable JS integration library:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || [];
    _talkableq.push(['init', {
      site_id: '' // Required - Talkable Site ID, you can find it on the Dashboard inside Talkable upon login. Example: 'your-talkable-site-id'
    }]);

    _talkableq.push(['authenticate_customer', {
      email: '', // Optional, pass when available. Example: 'customer@example.com'
      first_name: '', // Optional, pass when available. Example: 'John'
      last_name: '' // Optional, pass when available. Example: 'Smith'
    }]);
  </script>
  <script async src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->
