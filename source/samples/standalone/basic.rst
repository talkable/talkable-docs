.. code-block:: html

  <!-- Talkable iframe container, you are free to control its place in the DOM within the BODY tag -->
  <div id="talkable-sa-container"></div>

  <!-- Begin Talkable integration code -->
  <script>
    var _talkableq = _talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // REQUIRED - Talkable Site ID
    }]);

    _talkableq.push(['register_affiliate', {
      campaign_tags: ['default'], // REQUIRED - campaign tags for offer targeting

      iframe: { // REQUIRED - any valid HTML attributes can go in here
        container: 'talkable-sa-container', // REQUIRED - Tell Talkable where to insert the iframe (the value represents an HTML id attribute of the container)
        width: '100%', // REQUIRED - width of the iframe
      },

      affiliate_member: {}
    }]);
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

`Example of the Standalone integration <http://jsbin.com/cepayesiza/1>`_

