.. _advanced_features/subscribing_to_events:
.. include:: /partials/common.rst

.. meta::
   :description: Talkable JS integration script embeds Talkable campaign as an iframe.

Subscribing To Iframe Events
============================

Talkable integration embeds a referral campaign as an iframe with `src` attribute starting with `www.talkable.com` domain (or custom domain if the :ref:`white-labeling <advanced_features/white_labeling>` is setup).

In order to subscribe to an iframe Event you need to know `name` HTML attribute of the Talkable iframe and the Event name.
Iframe 'name' attribute may change depending on the campaign step opened. Thus, to use the right iframe name, open the campaign step you want to capture events from and copy the iframe name from the HTML of the page.

Below is an example of subscription to `offer_loaded` Talkable iframe Event.

Given we have integrated Campaign for :ref:`Standalone <campaigns/campaign_placements/standalone>` Placement, its HTML iframe reference looks like that:

.. code-block:: html

  <div id="talkable-offer">
    <iframe name="talkable-offer-iframe" src="https://www.talkable.com/..."></iframe>
  </div>

Knowing the container `name` attribute of the iframe is `talkable-offer-iframe` the subscription JS will be:

.. code-block:: javascript

  talkable.subscribe("offer_loaded", "talkable-offer-iframe", function(data, iframe) {
    alert("Talkable campaign iframe is loaded!");
  });

Notice two arguments passed in the callback:

  1. `data` object — the data passed by the iframe upon firing the event
  2. `iframe` object — iframe’s `HTML DOM reference`_

.. _HTML DOM reference: http://www.w3schools.com/jsref/dom_obj_frame.asp

Iframe Events List
------------------

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
