.. code-block:: html

  <!-- Place Talkable Container into appropriate place in the DOM -->
  <div id="talkable-invite"></div>

  <!-- Begin Talkable integration code -->
  <script>
    var _talkable_data = {
      campaign_template: { name: 'invite' } // Loads Invite campaign with tag "invite"
    };

    _talkableq.push(['register_affiliate', _talkable_data]); // Pass data to Talkable and show Invite campaign as a result
  </script>
  <!-- End Talkable integration code -->

