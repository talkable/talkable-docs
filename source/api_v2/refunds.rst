.. _api_v2/refunds:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to make refunds.

Refunds
=======

This API allows you to make refunds. See examples below.

|br|

.. code-block:: text

   POST /api/v2/origins/<origin_slug>/refund

Makes refund.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   origin_slug       If origin is a *Purchase*:

                     ``order_number``, e.g.:
                     ``"B00K2EOONI"``

                     If origin is an *Event*:

                     ``event_category``:``event_number``, e.g.:
                     ``"newsletter_subscription:42"``

   data              Optional: JSON object with ``refunded_at`` property.

                     E.g. ``{"refunded_at": "12345"}`` or  ``{"refunded_at": "12345"}``

   ================= ========================================================

Example
-------

Refund a Purchase
.................

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store"}' \
        https://www.talkable.com/api/v2/origins/B00K2EOONI/refund

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "referral": {
         "ad_rewarded": true,
         "advocate_person": {
            "id": 39198,
            "email": "customer@example.com",
            "first_name": null,
            "last_name": null
         },
         "campaign_id": 196,
         "created_at": "2019-05-27T15:41:31.000-07:00",
         "friend_person": {
            "id": 39202,
            "email": "friend@example.com",
            "first_name": null,
            "last_name": null
         },
         "id": 233,
         "offer_id": 867,
         "qa_generated": false,
         "referred_origin_id": 622,
         "referred_subtotal": 35.03,
         "status": "approved",
         "track_method": "coupon",
         "updated_at": "2019-05-27T15:41:31.000-07:00"
       }
     }
   }

.. container:: hidden

   .. toctree::
