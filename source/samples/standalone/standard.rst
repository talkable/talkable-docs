.. code-block:: html

  <!-- Talkable iframe container, you are free to control its place in the DOM -->
  <div id="talkable-sa-container"></div>

  <!-- Begin Talkable integration code -->
  <script>
    var _talkableq = _talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // REQUIRED - Talkable Site ID
      // , server: 'https://www.talkable.com' // OPTIONAL - use your own domain, that suppose to be setup as alias to talkable.com (this option is only possible for Enterprise client)
    }]);

    _talkableq.push(['register_affiliate', {
      campaign_tags: ['default'], // REQUIRED - campaign tags for offer targeting

      iframe: { // REQUIRED - any valid HTML attributes can go in here
        container: 'talkable-sa-container', // OPTIONAL - Tell Talkable where to insert the iframe (the value represents an HTML id attribute of a container)
        width: '100%', // REQUIRED - width of the iframe
        height: 960, // REQUIRED - initial height of the iframe. Will be automatically updated if responsive option is set to true.
        id: 'new_talkable_affiliate_member' // OPTIONAL - any other HTML attribute
      },

      affiliate_member: { // OPTIONAL - Talkable will ask person to signup in case when their email is not given by merchant
        email: 'customer@example.com', // OPTIONAL - customer email
        first_name: 'John', // OPTIONAL - customer first name
        last_name: 'Smith', // OPTIONAL - customer last name
        customer_id: '...' // OPTIONAL - customer ID from your site
        // , person_custom_properties: { // OPTIONAL - additional customer properties
        //     key1: 'value1', // String value
        //     key2: '123.2' // Numeric value
        // }
        // , traffic_source: 'Signup Page' // OPTIONAL - indicate person traffic source. Can be used as segmentation parameter in reporting.
      }
      // , responsive: false // OPTIONAL - fit iframe into any viewport (iframe height will be changed on window resize as well) which allows Talkable to make web pages responsive. 'false' disables it.
    }]);
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

`Example standalone integration <http://jsbin.com/cepayesiza/1>`_

`Source for standalone integration <http://jsbin.com/cepayesiza/1/edit?html,js,output>`_
