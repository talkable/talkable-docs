.. _advanced_features/events:
.. include:: /partials/common.rst

.. meta::
   :description: In addition to regular referral campaigns, Talkable also supports custom events that can be split into multiple categories.

Integrating Events
==================

In addition to running a referral campaign around regular
:ref:`purchases <integration/standard_integration/integration_components/post_purchase_script>`,
Talkable also supports custom events that can be split into multiple categories and be used to set up advanced campaign rules.

An example of such integration can be a subscription-based business that also supports
one-time purchases. A referral campaign example can be: |advocate| and |friend| both get
$5 off discount on one-time purchases, and $15 off when purchasing a subscription plan.

In this case, the subscription purchases and the one-time purchases should be
integrated as separate events under different event categories: “subscription” and
“purchase”. All events should be passed to Talkable, including recurring events.
Talkable’s backend referral engine runs each event through several checks to identify
whether the event was associated with a referral or not. With both “subscription” and
“purchase” events being passed to Talkable, we are then able to set up referral campaigns
to report on and reward these events as desired. See some examples below.

Subscription payments should be registered under the “subscription” event category. All such events
can be found in the Reports → Events section of your Talkable Dashboard. Here is an example:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || []
    window._talkableq.push(['register_event', {
      event: {
        event_category: 'subscription',
        event_number: 'ev1938579813',
        subtotal: '89',
        coupon_code: 'SAVE20'
      },
      customer: {
        email: 'customer1@example.com'
      }
    }]);
  </script>
  <!-- End Talkable integration code -->

.. note::

   Please make sure you've added :ref:`Talkable Initialization Script <integration/standard_integration/integration_components/initialization_script>` to your header or any template spanning every page.

One-time purchases should go under the “purchase” event category. You can find all purchases
in the Reports → Purchases section of your Talkable Dashboard. Here is an example:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || []
    window._talkableq.push(['register_event', {
      event: {
        event_category: 'purchase',
        event_number: 'ev1938579814',
        subtotal: '34.5',
        coupon_code: null
      },
      customer: {
        email: 'customer2@example.com'
      }
    }]);
  </script>
  <!-- End Talkable integration code -->

.. note::

   All recurring subscription purchases should be passed to Talkable as well, to ensure
   data integrity. If recurring transactions occur on the backend, follow the
   |br|
   :ref:`Origin API <api_v2/origins>` (see “Create an event” section).

.. _advanced_features/events/available_properties:

Available properties
~~~~~~~~~~~~~~~~~~~~

.. note::

   All PII params support data encryption. Find more about :ref:`Params Encryption <advanced_features/params_encryption>`.

Here is a list of available properties each event can include:

.. container:: ptable

   ===================== =================================================================
   Property              Description
   ===================== =================================================================
   **event**             An event data:

                         * **event_category** (required) – a category under which the event should be
                           tracked. Only alpha-numeric characters and underscores are
                           allowed. Minimum length – 5 characters. |br|
                           Example: ``'subscription'``.
                         * **event_number** (required) – any alpha-numeric characters. Each event
                           should have a unique event number, duplicate events will not be
                           saved. |br|
                           Example: ``'18934671af'``.
                         * **subtotal** (optional) – event subtotal. Any valid positive number
                           (including floats) or 0 are allowed. Preferably it should be passed
                           as a string to avoid JavaScript issues with rounding floats. |br|
                           Example: ``'198.5'``.
                         * **coupon_code** (optional) – a coupon code that was applied to
                           this event. |br|
                           Example: ``'SAVE20'``. You can also pass multiple coupons as
                           an array: ``['SAVE20', 'SAVE5']`` if they were stacked.
                         * **currency_iso_code** (optional) - Currency ISO code is required
                           for multi-currency sites. |br|
                           Example: ``'USD'``.
                         * **shipping_address** (optional) – Shipping address in case an event is
                           shippable. It is used in fraud prevention. |br|
                           Example:
                           ``'475 Valencia St, 2nd Floor, San Francisco, 94103, USA'``.
                         * **shipping_zip** (optional) – Same as **shipping_address**. Include only
                           zip here. |br|
                           Example: ``94103``.

   **customer**          A person who issued an event:

                         * **email**. (required) |br|
                           Example: ``'customer@example.com'``.
                         * **first_name** (optional). |br|
                           Example: ``'John'``.
                         * **last_name** (optional) |br|
                           Example: ``'Smith'``.
                         * **traffic_source** (optional) - specific
                           :ref:`Traffic Source <advanced_features/segments>` value
                           that helps to distinguish different points of integration. |br|
                           Example: ``'facebook'``.

   **campaign_tags**     Campaign tags are used to manually choose which campaign to show
                         once the event has been tracked successfully (optional).

                         Each Talkable campaign supports multiple tags, you can list them
                         as an array: ``['tag1', 'tag2']``.

                         You can control campaign tags inside Campaign Rules. Each
                         Talkable campaign can have different tags.

                         Alternatively, you can use
                         :ref:`Campaign Placements <campaigns/campaign_placements>`
                         feature to set up routing in your Talkable Dashboard instead
                         of controlling it through the JS integration on your end. Campaign
                         Placements are easy to change, no code changes are needed on your
                         end.

   **custom_properties** Custom key-value data that can be attached to a person
                         (optional). It can be used for segmentation for example: you can
                         code up custom criteria to show relevant campaigns to
                         each segment. Alternatively, custom properties can be used for an
                         advanced referral reward logics. Any valid JS object is allowed.
                         Object value should always be a string.

                         Example: ``{ key1: 'value1', key2: 'true' }``.
                         :ref:`Learn more <advanced_features/passing_custom_data>`.

   ===================== =================================================================
