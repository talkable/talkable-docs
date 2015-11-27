.. code-block:: html

  <!-- Talkable iframe container, you are free to control its place in the DOM within the BODY tag -->
  <div id="talkable-sa-container"></div>

  <!-- Begin Talkable integration code -->
  <script>
    var _talkableq = _talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // REQUIRED - Talkable Site ID
    }]);

    var _talkable_affiliate = {
      affiliate_member: {
        email: 'advocate@example.com', // Optional — Advocate email address
        first_name: 'John', // Optional — Advocate first name
        last_name: 'Smith' // Optional — Advocate last name
      },
      iframe: {
        width: '100%', // You can set as many standard HTML attributes in here as you need: style, height, etc.
        container: 'talkable-sa-container' // Required — ID attribute of the HTML tag where to insert Talkable campaign iframe into
      },
      campaign_tags: ['invite'] // Optional — Campaign tag to load after the data is passed to Talkable
    };

    _talkableq.push(['register_affiliate', _talkable_affiliate]); // Pass data to Talkable and show Standalone campaign as a result
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

`Integration example <http://learn.talkable.com/docs/invite-basic-authorized>`__

