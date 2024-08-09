**HTML:**

.. code-block:: html

  {% if gated_email != blank %}
    <div class="js-coupon-code">{{ coupon_code }}</div>
    <a class="js-proceed-link" href="{{ proceed_to_merchant_path }}">Shop using this code</a>
  {% else %}
    <div class="js-hide">
      <form action="#" class="js-gating-unlock">
        <input type="email" class="js-gating-email" placeholder="myname@example.com"/>
        <label for="email-subscription">
          <input type="checkbox" checked="checked" id="email-subscription" class="js-gating-checkbox" />
          Sign me up for the latest news
        </label>
        <button>Claim your coupon code</button>
      </form>
    </div>

    <!-- What to show after submitting email. Hidden by default! -->
    <div class="js-show" style="display: none;">
      <div class="js-coupon-code">...</div>
      <a class="js-proceed-link" href="{{ proceed_to_merchant_path }}">Shop using this code</a>
    </div>

    <!-- Show errors in case something's wrong with the email. Hidden by default! -->
    <div class="js-validation" style="display: none;"></div>
  {% endif %}

**JS:**

.. code-block:: javascript

  $(document).ready(function() {
    var $proceedLink    = $('.js-proceed-link'),
        $gatingEmail    = $('.js-gating-email'),
        $contentGating  = $('.js-hide'),
        $gatingUnlock   = $('.js-gating-unlock'),
        $gatingCheckbox = $('.js-gating-checkbox'),
        $contentHidden  = $('.js-show'),
        $notice         = $('.js-validation'),
        $couponCode     = $('.js-coupon-code');

    function displayNotice(data) {
      $notice.html(data);
      $notice.fadeIn(300);
      setTimeout(function() {
        $notice.fadeOut(300);
      }, 3000);
    }

    Talkable.subscribe('email_gating_passed', function(data) {
      $contentGating.slideUp(300);
      setTimeout(function() {
        $contentHidden.slideDown(300);
        $couponCode.text(data.coupon_code); // Insert coupon code
        bindClipToCopy('.js-coupon-code');
      }, 300);
    });

    function unlockGating(e) {
      var email, subChoice, emailValid, proxyParams, query;
      e.preventDefault();

      proxyParams = {};
      email = $.trim($gatingEmail.val());
      proxyParams.sub_choice = $gatingCheckbox.is(':checked') ? 'yes' : 'no';
      emailValid = /^[^@]+@([^@\.]+\.)+[^@\.]+$/.test(email);

      if (email.length && emailValid) {
        query = $.param({proxy_params: $.extend(proxyParams, {email: email})});
        Talkable.passEmailGating(query);
      } else {
        displayNotice("Something isn't right. Please try again");
      }
    }

    $gatingUnlock.submit(function(e) {
      unlockGating(e);
    });
  });
