.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    //<![CDATA[
      var _talkableq = _talkableq || [];
      _talkableq.push(['init', {
        site_id: 'YOUR-TALKABLE-SITE-ID', // REQUIRED - Talkable Site ID
        // server: 'https://www.talkable.com' // OPTIONAL - use your own domain, that suppose to be setup as alias to talkable.com (this option is only possible for Enterprise client)
      }]);

      _talkableq.push(['register_affiliate', {
        iframe: { // REQUIRED - html attributes for iframe tag to fit page design
          width: '100%', // REQUIRED - width of the iframe
          height: 960, // REQUIRED - initial height of the iframe. Will be automatically updated if responsive option is set to true.
          // container: "id-example", // OPTIONAL - Tell Talkable where to insert the iframe (ID attribute). See Asynchronous Integration for more details.
          id: 'new_curebit_affiliate_member' // OPTIONAL - any other HTML attribute
        },

        affiliate_member: { // OPTIONAL - Talkable will ask person to signup in case when his email is not given by merchant
          email: 'customer@example.com', // OPTIONAL - customer email
          first_name: 'John', // OPTIONAL - customer first name
          last_name: 'Smith', // OPTIONAL - customer last name
          customer_id: '...', // OPTIONAL - customer ID from your site
          gender: '...', // OPTIONAL - customer gender ('male' or 'female')
          // person_custom_properties: { // OPTIONAL - additional customer properties
          //     key1: 'value1', // String value
          //     key2: '123.2' // Numeric value
          // },
          traffic_source: '...' // OPTIONAL - indicate person traffic source. Can be used as segmentation parameter in reporting.
        },
        responsive: true, // OPTIONAL - fit iframe into viewport (also on resize) and allow Talkable display mobile templates
        campaign_tags: ['default'] // OPTIONAL - campaign tags for offer targeting
      }]);
    //]]>
  </script>
  <script src="//d2jjzw81hqbuqv.cloudfront.net/integration/talkable-1.0.min.js" type="text/javascript"></script>
  <!-- End Talkable integration code -->
