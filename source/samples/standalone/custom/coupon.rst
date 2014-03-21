.. code-block:: javascript

  var offer_code = 'OFFER-CODE';
  $.get('https://www.curebit.com/o/' + offer_code + '/fire_event.json', {
    event_name: 'share', // REQUIRED
    event_sharing_channel: 'email' // REQUIRED - may be email, facebook, twitter
  }).done(function(data) {
    if (data.success) {
      // Save coupon_code
      console.log(data.coupon_code);
    } else {
      // Check for errors
      console.log(data.errors);
    }
  }).fail(function() {
    // Something went wrong
  });
