.. _advanced_features/shopify_coupons_auto_apply:

.. meta::
  :description: Talkable supports coupon auto-apply for Shopify. This feature allows to avoid manual coupon uploads and/or Shopify Price Rule management.

Shopify coupon auto-apply
=========================

Talkable supports coupon auto-apply for Shopify. This guide provides clear and easy-to-follow documentation on two methods of automatically applying Shopify coupons.

Method 1: Coupon application via destination URL
------------------------------------------------

This method involves including the discount code in the URL. This way, when a customer clicks the link, the coupon is automatically applied to their cart.

#. **Friend destination URL:**

   .. code-block:: liquid

      {{ site_setup.url }}
      {% if coupon.code %}
        /discount/{{ coupon.code }}?redirect=!!! YOUR CURRENT URL !!!
      {% endif %}

   Result example:

   .. code-block:: liquid

       {{ site_setup.url }}
       {% if coupon.code %}
         /discount/{{ coupon.code }}?redirect={{ site_setup.url }}&
       {% else %}
         ?
       {% endif %}
       utm_source=talkable
       &utm_medium={{ sharing_channel }}
       &utm_content={{ campaign_setup.name | encode_query_argument }}
       &utm_campaign={{ campaign_setup.id }}
       &tkbl_cvuuid={{ visitor_uuid }}
       &talkable_visitor_offer_id={{ friend_offer.id }}

   .. image:: /_static/img/shopify/auto_apply/friend_destination_url.png
      :alt: Friend destination url
      :class: is-minimal

   **Breakdown:**
    - `{{ site_setup.url }}/discount/{{ coupon.code }}`: This applies the coupon code to the cart.
    - `?redirect={{ site_setup.url }}`: This redirects the customer back to your store.
    - `&utm_source=talkable&utm_medium={{ sharing_channel }}&utm_content={{ campaign_setup.name | encode_query_argument }}&utm_campaign={{ campaign_setup.id }}`: These are default UTM parameters used for tracking.
    - `&tkbl_cvuuid={{ visitor_uuid }}&talkable_visitor_offer_id={{ friend_offer.id }}`: These parameters are specific to Talkable, to identify customer.
    - `{% if coupon.code %}{% endif %}` - condition to check if we have coupon.

#. **Advocate destination URL:**

   .. code-block:: liquid

       {{ site_setup.url }}
       {% if coupon.code %}
         /discount/{{ coupon.code }}?redirect={{ site_setup.url }}&
       {% else %}
         ?
       {% endif %}
       tkbl_cvuuid={{ visitor_uuid }}

   .. image:: /_static/img/shopify/auto_apply/advocate_destination_url.png
      :alt: Advocate destination url
      :class: is-minimal

   .. note::

      Advocate Reward Paid email should use `{{ proceed_to_advocate_destination_url }}` variable


Method 2: Coupon application via client-side library integration
----------------------------------------------------------------

The second method involves updating the per-client JS library with a code snippet that listens for a form submission event and appends the discount code to the form data.

Here's the code snippet to include:

.. code-block:: javascript

   //Auto apply coupon code
   _talkableq.push(['gleam_reward', {
     callback: function(coupon) {
       if (window.jQuery) {
         $("body").on("submit", "form[action='/cart']", function(data) {
             $('<input />').attr('type', 'hidden')
               .attr('name', "discount")
               .attr('value', coupon)
               .appendTo($("form[action='/cart']"));
             return true;
         });
       } else {
         var forms = document.getElementsByTagName('form'),
             discount = document.createElement('input');
         discount.type = 'hidden';
         discount.name = 'discount';
         discount.value = coupon;
         for (var i = 0; i < forms.length; i++) {
           if (forms[i].action.indexOf('/cart') !== -1) {
             forms[i].appendChild(discount);
           }
         }
       }
     }
   }]);

**Breakdown:**

This JavaScript code uses the Talkable `gleam_reward` event. When this event fires, it provides a callback function with the `coupon` argument, representing the coupon code.

If jQuery is available, it sets up an event listener for the form submission. When the form is submitted, it appends a hidden input field with the name "discount" and the value of the coupon code to the form.

If jQuery is not available, it does essentially the same thing using vanilla JavaScript. It loops through all forms in the document, and if it finds one with an action containing '/cart', it appends the hidden discount input field.

These methods will allow the coupon to be automatically applied when a customer adds a product to their cart and proceeds to checkout.