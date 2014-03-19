.. _liquid/gating:
.. include:: /partials/common.rst

Gating
======

Email Gating
------------

Email gating is used when you need RD to provide an email to get a
reward. It is used on the landing page and looks like a popup with email
field, submit button, and "signup for latest news" checkbox.

First of all, turn on email gating in Restricted settings:

.. image:: /_static/img/liquid/gating/image1.png
   :alt:

Basic Setup
...........

**HTML:**

.. code-block:: html

    {% if gated_email != blank %}
        <div class="js-coupon-code">{{ coupon_code }}</div>
        <a class="js-proceed-link" href="{{ proceed_to_merchant_path }}">Shop using this code</a>
    {% else %}
      <div class="js-hide">
        <form action="#">
          <input type="email" class="js-gating-email" placeholder="myname@email.com"/>
          <button class="js-gating-unlock">Claim your coupon code</button>
        </form>
      </div>

      <!- What to show after submitting email. Hidden by default! ->
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

      Curebit.subscribe("email_gating_passed", function(data) {
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
          Curebit.passEmailGating(query);
        } else {
          alert("Something isn’t right. Please try again");
        }
      }

      $gatingUnlock.submit(function(e) {
        unlockGating(e);
      });
    });

Advanced Setup
..............

1. 'Click to copy' functionality for coupon code
2. 'Sign up for news' checkbox
3. Email validation messages

**HTML:**

.. code-block:: html

    {% if gated_email != blank %}
        <div class="js-coupon-code">{{ coupon_code }}</div>
        <a class="js-proceed-link" href="{{ proceed_to_merchant_path }}">Shop using this code</a>
    {% else %}
      <div class="js-hide">
        <form action="#" class="js-gating-unlock">
          <input type="email" class="js-gating-email" placeholder="myname@email.com"/>
          <label for="email-subscription">
            <input type="checkbox" checked="checked" id="email-subscription" class="js-gating-checkbox" />
            Sign me up for the latest news
          </label>
          <button class="js-gating-unlock">Claim your coupon code</button>
        </form>
      </div>

      <!- What to show after submitting email. Hidden by default! ->
      <div class="js-show" style="display: none;">
        <div class="js-coupon-code">...</div>
        <a class="js-proceed-link" href="{{ proceed_to_merchant_path }}">Shop using this code</a>
      </div>

      <!- Show errors in case something's wrong with the email. Hidden by default! ->
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

      Curebit.subscribe("email_gating_passed", function(data) {
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
          Curebit.passEmailGating(query);
        } else {
          displayNotice("Something isn’t right. Please try again");
        }
      }

      $gatingUnlock.submit(function(e) {
        unlockGating(e);
      });
    });

Like Gating
-----------

.. image:: /_static/img/liquid/gating/image2.png
   :alt:

Basic Setup
...........

**HTML:**

.. code-block:: html

    <div class="container">
      {% if gated_like == blank %}
        <div class="content">
          <div class="js-before">
            <div class='like-button fb_like'>
              <div id='fb-root'></div>
              <fb:like href="{{ short_url }}" action="like" layout="button" show_faces="false" share="false"></fb:like>
            </div>
          </div>
          <div class="js-after">
            <h2 data-clipboard-text="" title="Click to Copy" data-copied-label="Copied!" class="promo-code js-promo-code">
              <span class="code"></span>
            </h2>
            <a class="button" href="{{ proceed_to_merchant_path }}">Shop with this code</a>
          </div>
        </div>

      {% else %}
        <div class="content">
          <h2 data-clipboard-text="{{coupon_code}}" title="Click to Copy" data-copied-label="Copied!" class="promo-code js-promo-code">
            <span class="code">{{coupon_code}}</span>
          </h2>
          <a class="button" href="{{ proceed_to_merchant_path }}">Shop with this code</a>
        </div>

      {% endif %}
    </div>

    <div class="js-notice"></div>

**JS:**

.. code-block:: javascript

    var populateCouponCode = function(couponCode) {
      $('.js-promo-code').attr('data-clipboard-text', couponCode);
      $('.js-promo-code .code').html(couponCode);
      bindClipToCopy('.js-promo-code');
    };

    $(function() {
      var notice  = $('.js-notice'),
          timer;

      bindClipToCopy('.js-promo-code');

      var displayNotice = function(data, delay) {
        clearTimeout(timer);
        notice
          .html(data)
          .fadeIn(300);
        timer = setTimeout(function() {
          notice.fadeOut(300);
        }, delay ? delay : 5000);
      };

      Curebit.subscribe("like_gating_succeeded", function (data) {
        Curebit.passLikeGating();
      });

      Curebit.subscribe("like_gating_passed", function (data) {
        if (data.coupon_code) {
          populateCouponCode(data.coupon_code);
          $('.js-before').slideUp(300);
          setTimeout(function() {
            $('.js-after').slideDown(300);
          }, 300);
        } else {
          console.log("No coupon provided.");
          displayNotice("No coupon provided.");
        }
      });
    });

.. code-block:: css

    .js-after {
      display: none;
    }
