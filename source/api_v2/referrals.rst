.. _api_v2/referrals:
.. include:: /partials/common.rst

Referrals
=========

This API allows you to approve/void referrals.

|br|

.. code-block:: text

   PUT /origins/<origin_slug>/referral

Updates referral’s status.

.. note:: Approved or voided referrals cannot be changed to the opposite state.

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

   data              JSON object with ``status`` property.

                     E.g. ``{"status": "approved"}`` or  ``{"status": "voided"}``

   ================= ========================================================

Example
-------

Approve a Referral
..................

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X PUT \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","data":{"status":"approved"}}' \
        https://www.talkable.com/api/v2/origins/B00K2EOONI/referral

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "referral": {
         "ad_rewarded": true,
         "campaign_id": 196,
         "created_at": "2019-05-27T15:41:31.000-07:00",
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
