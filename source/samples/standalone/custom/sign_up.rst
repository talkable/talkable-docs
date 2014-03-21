.. code-block:: javascript

  var site_id = 'YOUR-CUREBIT-SITE-ID';
  $.get('https://www.curebit.com/public/' + site_id + '/affiliate_members/create.json', {
    campaign_tag: 'default', // REQUIRED
    affiliate_member: {
      email: 'YOUR-USER-EMAIL', // REQUIRED
      first_name: '...' // OPTIONAL
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
