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

Marks origin as refunded.

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

                     E.g. ``{"refunded_at": "2020-04-27T00:00:00.000-07:00"}``

   ================= ========================================================

Example
-------

Mark Purchase as Refunded
.........................

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
       "customer_id": null,
       "email": "ad160654@gmail.com",
       "id": 5,
       "ip_address": "100.107.1.171",
       "order_number": "B00K2EOONI",
       "subtotal": 100.0,
       "type": "Purchase",
       "order_date": "2020-01-20T01:46:10.000-07:00",
       "refunded_at": "2020-04-27T00:00:00.000-07:00",
       "coupon_code": ""
     }
   }

.. container:: hidden

   .. toctree::
