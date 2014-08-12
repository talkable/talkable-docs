.. code-block:: javascript

  var site_id = 'YOUR-TALKABLE-SITE-ID';
  $.get('https://www.talkable.com/public/' + site_id + '/affiliate_members/create.json', {
    campaign_tag: 'default', // REQUIRED
    affiliate_member: {
      email: 'YOUR-USER-EMAIL', // REQUIRED - customer email
      first_name: '...', // OPTIONAL - customer first name
      last_name: '...', // OPTIONAL - customer last name
      customer_id: '...', // OPTIONAL - customer ID from your site
      gender: '...', // OPTIONAL - customer gender ('male' or 'female')
      person_custom_properties: { // OPTIONAL - additional customer properties
          key1: 'value1', // string value
          key2: '123.2' // numeric value
      }
    }
  }).done(function(data) {
    if (data.success) {
      // Save offer_code
      console.log(data.offer_code);
    } else {
      // Check for errors
      console.log(data.errors);
    }
  }).fail(function() {
    // Something went wrong
  });
