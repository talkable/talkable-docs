.. code-block:: html

  <!-- Begin Curebit integration code -->
  <script>
    //<![CDATA[
      var _curebitq = _curebitq || [];
      _curebitq.push(['init', {
        site_id: 'YOUR-CUREBIT-SITE-ID', // REQUIRED - Curebit Site ID
        //server: 'https://www.curebit.com' // OPTIONAL - use your own domain, that suppose to be setup as alias to curebit.com (this option is only possible for Enterprise client)
      }]);

      _curebitq.push(['register_affiliate', {
        iframe: { // REQUIRED - html attributes for iframe tag to fit page design
          width: '100%', // REQUIRED - width of the iframe
          height: 480, // REQUIRED - initial height of the iframe. Will be automatically updated if responsive option is set to true.
          id: 'new_curebit_affiliate_member', // OPTIONAL - any other HTML attribute
          frameborder: 0 // OPTIONAL - removes border from IE
        },

        affiliate_member: { // OPTIONAL - curebit will ask person to signup
                            // in case when his email is not given by merchant
          email: 'customer@example.com', // OPTIONAL - customer email
          first_name: 'John', // OPTIONAL - customer first name
          last_name: 'Smith', // OPTIONAL - customer last name
          customer_id: '', // OPTIONAL - customer ID from your site
          traffic_source: '' // OPTIONAL - indicate person traffic source. Can be used as segmentation parameter in reporting.
        },
        responsive: true, // OPTIONAL - fit iframe into viewport (also on resize) and allow Curebit display mobile templates
        // device: 'desktop', // OPTIONAL - enforce mobile/tablet/desktop view or skip this to allow Curebit choose corresponding template
        campaign_tags: ['default'] // OPTIONAL - campaign tags for offer targeting
      }]);
    //]]>
  </script>
  <script src="//d2jjzw81hqbuqv.cloudfront.net/integration/curebit-1.0.min.js" type="text/javascript"></script>
  <!-- End Curebit integration code -->
