.. _advanced_features/subscribing_to_events:
.. include:: /partials/common.rst

.. meta::
   :description: Talkable JS integration script embeds Talkable campaign as an iframe with src attribute starting with www.talkable.com domain.

Subscribing To Iframe Events
============================

Talkable JS integration script embeds Talkable campaign as an iframe with `src` attribute starting with `www.talkable.com` domain (or custom domain if the :ref:`white-labeling <advanced_features/white_labeling>` is setup).

Due to same-origin_ policy it is not possible to pass/get any data to the iframe directly. Talkable JS integration library has a built-in subscription mechanism for that which is based on JS window.postmessage_ method.

.. _same-origin: https://en.wikipedia.org/wiki/Same-origin_policy
.. _window.postmessage: https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage

In order to subscribe to an iframe Event you need to know `id` HTML attribute of the Container DIV that holds it, and the Event name. Below is an example of subscription to `offer_loaded` Talkable iframe Event.

Given we have integrated Campaign for :ref:`Standalone <campaigns/campaign_placements/standalone>` Placement, its JS-generated HTML tag looks similar to the following:

.. code-block:: html

  <div id="talkable-offer">
    <iframe name="talkable-offer" src="https://www.talkable.com/..."></iframe>
  </div>

Knowing the container `id` attribute is `talkable-offer` the subscription JS will be:

.. code-block:: javascript

  talkable.subscribe("offer_loaded", "talkable-offer", function(data, iframe) {
    alert("Talkable campaign iframe is loaded!");
  });

Notice the callback function with two arguments:

  1. `data` object — this is the data which gets passed by the iframe upon firing the event. You can use it to receive data from Talkable.
  2. `iframe` object — this is iframe’s `HTML DOM reference`_

.. _HTML DOM reference: http://www.w3schools.com/jsref/dom_obj_frame.asp

Talkable Events
---------------

Talkable campaigns are equipped with the following set of events:

  1. `offer_loaded` — Talkable iframe DOM ready event which is in fact the very first event that you can use to determine if the iframe is loaded.
  2. `responsive_iframe_height` — fires every time iframe size gets changed. You can use it to detect changes in iframe size.
     You can read more :ref:`here <responsive-views>`. Previously named as ``curebit_offer_iframe_broadcast``.
  3. `offer_close` — fires when the close button is clicked. You can use this event to determine when user closes Talkable campaign, it then disappears from the screen.
  4. `offer_triggered` — Talkable Trigger Widget iframe fires this event when user clicks on it. You can use this event to detect when the main offer iframe is about to show up.
  5. `coupon_issued` — fires upon issuing coupon code as a reward for sharing. You can use it to determine when the user shares and receives their reward. `data.channel` tells which sharing channel was used and `data.coupon_code` stores the coupon code value.
  6. `share_succeeded` — fires each time |advocate| shares. `data.channel` tells which sharing channel was used for the share.
  7. `email_gating_passed` — fires when |friend| passes email gating on :ref:`Friend Claim Page <campaigns/views/offers_claim>`.
  8. `email_gating_failed` — fires when |friend| fails to pass email gating on :ref:`Friend Claim Page <campaigns/views/offers_claim>`.

.. container:: hidden

   .. toctree::
