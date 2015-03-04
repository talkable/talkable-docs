**HTML:**

.. code-block:: html

  <!-- Prompt user to share -->
  <a href="#" class="js-share-offer-via-facebook">Share on Facebook</a>
  <!-- Insert coupon code after successful share -->
  <div class="js-coupon-code"></div>

**JS:**

.. code-block:: javascript

  Talkable.subscribe('facebook_share_succeeded', function(data) {
    if (data.coupon_code) {
      $('.js-coupon-code').text(data.coupon_code); // Insert coupon code as a text
    } else {
      $('.js-coupon-code').text('No coupon code provided'); // Show error that coupon code wasn't provided.
    }
  });
