In order to integrate Talkable campaign(s) on your site you need to set the following script into HEAD tag inside
your main layout which is used on every page. This is initialization of the Talkable JS integration library:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // Required - Talkable Site ID, you can find it on the Dashboard inside Talkable upon login
    }]);

    _talkableq.push(['authenticate_customer', {
      email: 'customer@example.com', // Optional - Customer email, it is recommended to always pass it when available
      first_name: 'Name', // Optional - Customer first name
      last_name: 'Surname' // Optional - Customer last name
    }]);
  </script>
  <script async src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->
