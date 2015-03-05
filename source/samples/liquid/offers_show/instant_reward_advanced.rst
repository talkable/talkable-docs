**HTML:**

.. code-block:: html

  <!-- Prompt user to share -->
  <div class="js-not-shared">
    <a href="#" class="js-share-offer-via-facebook">Share on Facebook</a>
  </div>

  <!-- Show coupon code after successful share. Hidden by default. -->
  <div class="js-shared" style="display: none;">
    <div class="js-coupon-code">...</div>
  </div>

**JS:**

.. code-block:: javascript

  Talkable.subscribe('facebook_share_succeeded', function(data) {
    if (data.coupon_code) {
      $('.js-coupon-code').text(data.coupon_code); // Insert coupon code as a text
      $('.js-coupon-code').attr('data-clipboard-text', data.coupon_code); // Copy coupon code on click
      $('.js-not-shared').hide(); // Hide everything with class `.js-not-shared`
      $('.js-shared').show(); // Show everything with class `.js-shared`
      bindClipToCopy('.js-coupon-code'); // Initiate click to copy functionality
    } else {
      $('.js-coupon-code').text('No coupon code provided'); // Show error that coupon code wasn't provided.
    }
  });
