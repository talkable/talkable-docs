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
      campaign_template: { name: 'invite' } // Loads Post Purchase campaign with tag "invite"
    };

    _talkableq.push(['register_affiliate', _talkable_affiliate]); // Pass data to Talkable and show Standalone campaign as a result
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

`Integration example <http://learn.talkable.com/docs/invite-basic>`__

