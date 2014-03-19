.. _liquid/sharing:
.. include:: /partials/common.rst

Sharing
==============

Instant Reward
--------------

Instant reward campaign is used when we need to reward RR immediately
after he shares. If RR redemption email is turned on it will be sent
right after successful share. The most popular share channel is
Facebook.

To make instant reward work you need to use FB App share instead of a
default sharer.php.
Also make sure **RR social sharing incentive** is set.

After that we need to setup our offer page with the following markup:

**HTML:**

.. code-block:: html

    <!-- Prompt user to share -->
    <a href="#" class="js-share-offer-via-facebook">Share on Facebook</a>
    <!-- Insert coupon code after successful share -->
    <div class="js-coupon-code"></div>

**JS:**

.. code-block:: javascript

    Curebit.subscribe('facebook_share_succeeded', function(data) {
      if (data.coupon_code) {
        $('.js-coupon-code').text(data.coupon_code); // Insert coupon code as a text
      } else {
        $('.js-coupon-code').text("No coupon code provided"); // Show error that coupon code wasn't provided.
      }
    });

--------------

If you need to hide/show some information when shared and copy code on
click here is more advanced setup:

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

    Curebit.subscribe('facebook_share_succeeded', function(data) {
      if (data.coupon_code) {
        $('.js-coupon-code').text(data.coupon_code); // Insert coupon code as a text
        $('.js-coupon-code').attr('data-clipboard-text', data.coupon_code); // Copy coupon code on click
        $('.js-not-shared').hide(); // Hide everything with class `.js-not-shared`
        $('.js-shared').show(); // Show everything with class `.js-shared`
        bindClipToCopy('.js-coupon-code'); // Initiate click to copy functionality
      } else {
        $('.js-coupon-code').text("No coupon code provided"); // Show error that coupon code wasn't provided.
      }
    });

CloudSponge Integration
-----------------------

**HTML:**

.. code-block:: html

    <a class="cs_import" href="#">Import contacts</a>
    <script type="text/javascript" src="//api.cloudsponge.com/address_books.js"></script>
    <script type="text/javascript">
      var csPageOptions = {
        "include": ["email"],
        "locale": "english",
        "domain_key": "PHAUB8N7PNYWP555F7YB",
        "textarea_id": "email_recipients_list"
      };
    </script>

1. ``domain_key`` — CloudSponge account (Curebit by default)
2. ``textarea_id`` — ID attribute to populate data to

Multiple Email Fields
---------------------

.. code-block:: html

    <form action="#" class="js-share-via-email-form share-via-email">
      <input type="email" name="email_recipient_list[]" />
      <input type="email" name="email_recipient_list[]" />
      <input type="email" name="email_recipient_list[]" />
    </form>

LinkedIn
--------

Separate Wording
****************

Enable separate Linkedin share wording (Open Graph title and message)

.. code-block:: html

    {% if user_agent contains "LinkedInBot" %}
    Special offer title for Linkedin friends
    {% else %}
    Special offer title for Facebook friends
    {% endif %}

Basic Setup
***********

**HTML:**

.. code-block:: html

    <script src="//platform.linkedin.com/in.js" type="text/javascript"></script>
    <script type="IN/Share" data-url="{{ short_url_linkedin }}" data-onsuccess="fireOnLinkedInShare"></script>

**JS:**

.. code-block:: javascript

    function fireOnLinkedInShare() {
      Curebit.share_succeeded('linkedin');
    }

Advanced Setup
**************

**HTML:**

.. code-block:: html

    <span class="js-linkedin-button-holder" style="display: none;">
      <script src="//platform.linkedin.com/in.js" type="text/javascript"></script>
      <script type="IN/Share" data-url="{{ short_url_linkedin }}" data-onsuccess="fireOnLinkedInShare"></script>
    </span>

Remember to wrap LI scripts into an ``js-linkedin-button-holder``
container which is hidden by default not to show LinkedIn custom button
until it is loaded.

**JS:**

.. code-block:: javascript

    function fireOnLinkedInShare() {
      Curebit.share_succeeded('linkedin');
    }

    function configureShareOnLinkedIn(params) {
      $('.IN-widget').attr('style', '').find('a').addClass(params.className);
      $('.IN-widget').find('span').each(function(i, element) {
        $(element).attr({style: '', id: ''});
        if ($(element).text() == "in") {
          $(element).remove();
        } else if ($(element).text() == "Share") {
          $(element).text(params.text);
        }
      });
    }

    var initLinkedInShareButton = setInterval(function() {
      if ($('span').hasClass('IN-widget')) {
        clearInterval(initLinkedInShareButton);
        $('.js-linkedin-button-holder').fadeIn(300);
        configureShareOnLinkedIn({
          className: 'btn btn-linkedin',
          text: 'LinkedIn'
        });
      }
    }, 500);

1. ``fireOnLinkedInShare`` — triggering this method is required to make
   Curebit visits tracking work.
2. ``initLinkedInShareButton`` — checks for LI button to load and then
   show its container ``js-linkedin-button-holder`` and trigger
   ``configureShareOnLinkedIn``.
3. ``configureShareOnLinkedIn`` — strips all unnecessary styles and
   ``id`` attributes from all LI button children nodes and allows to
   change ``class`` attribute and button text by passing an object like
   following:

.. code-block:: javascript

    configureShareOnLinkedIn({
      className: 'btn btn-linkedin', // Button class
      text: 'LinkedIn' // Button text
    });
