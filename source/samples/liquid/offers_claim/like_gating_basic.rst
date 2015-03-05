**HTML:**

.. code-block:: html

  <div class="container">
    {% if gated_like == blank %}
      <div class="content">
        <div class="js-before">
          <div class="like-button fb_like">
            <div id="fb-root"></div>
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
        <h2 data-clipboard-text="{{ coupon_code }}" title="Click to Copy" data-copied-label="Copied!" class="promo-code js-promo-code">
          <span class="code">{{ coupon_code }}</span>
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

    Talkable.subscribe('like_gating_succeeded', function (data) {
      Talkable.passLikeGating();
    });

    Talkable.subscribe('like_gating_passed', function (data) {
      if (data.coupon_code) {
        populateCouponCode(data.coupon_code);
        $('.js-before').slideUp(300);
        setTimeout(function() {
          $('.js-after').slideDown(300);
        }, 300);
      } else {
        console.log('No coupon provided.');
        displayNotice('No coupon provided.');
      }
    });
  });

.. code-block:: css

  .js-after {
    display: none;
  }
