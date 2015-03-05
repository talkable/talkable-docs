**HTML:**

.. code-block:: html

  {% if gated_email != blank %}
    <div class="js-coupon-code">{{ coupon_code }}</div>
    <a class="js-proceed-link" href="{{ proceed_to_merchant_path }}">Shop using this code</a>
  {% else %}
    <div class="js-hide">
      <form action="#" class="js-gating-unlock">
        <input type="email" class="js-gating-email" placeholder="myname@example.com"/>
        <button>Claim your coupon code</button>
      </form>
    </div>

    <!-- What to show after submitting email. Hidden by default! -->
    <div class="js-show" style="display: none;">
      <div class="js-coupon-code">...</div>
      <a class="js-proceed-link" href="{{ proceed_to_merchant_path }}">Shop using this code</a>
    </div>
  {% endif %}

**JS:**

.. code-block:: javascript

  $(document).ready(function() {
    var $proceedLink    = $('.js-proceed-link'),
        $gatingEmail    = $('.js-gating-email'),
        $contentGating  = $('.js-hide'),
        $gatingUnlock   = $('.js-gating-unlock'),
        $contentHidden  = $('.js-show'),
        $couponCode     = $('.js-coupon-code');

    Talkable.subscribe('email_gating_passed', function(data) {
      $contentGating.hide();
      $contentHidden.show();
      $couponCode.text(data.coupon_code); // Insert coupon code
    });

    function unlockGating(e) {
      var email, emailValid, proxyParams, query;
      e.preventDefault();

      proxyParams = {};
      email = $.trim($gatingEmail.val());
      emailValid = /^[^@]+@([^@\.]+\.)+[^@\.]+$/.test(email);

      if (email.length && emailValid) {
        query = $.param({proxy_params: $.extend(proxyParams, {email: email})});
        Talkable.passEmailGating(query);
      } else {
        alert("Something isn’t right. Please try again");
      }
    }

    $gatingUnlock.submit(function(e) {
      unlockGating(e);
    });
  });
