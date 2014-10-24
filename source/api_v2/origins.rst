.. _api_v2/origins:
.. include:: /partials/common.rst

Origins
=======

This API allows you to create origins. See examples below.

|br|

.. code-block:: url

   POST /origins

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   type              Type of origin to create (*"AffiliateMember"*, *"Purchase"* or *"Event"*)
   data              Hash or JSON object with following properties:

                     Common Fields:

                     * email
                     * customer_id (optional)
                     * first_name (optional)
                     * last_name (optional)
                     * person_custom_properties (optional)

                     For Purchase:

                     * subtotal
                     * order_number
                     * order_date (|iso8601| formatted datetime)
                     * items (optional)
                     * coupon_code (optional)

                     For Event:

                     * event_number
                     * event_category
                     * subtotal (optional)
                     * coupon_code (optional)

   interpolations    Optional: set to `true` to include origin interpolation
                     variables in response
   ================= ========================================================

Example
-------

Create a purchase
.................

.. code-block:: javascript

   {
     "api_key": "i9uil7nQgDjucCiTJu",
     "site_slug": "my-store",
     "type": "Purchase",
     "data": {
       "email": "customer@example.com",
       "order_number": 12,
       "order_date": "2014-03-14T05:49:54-07:00",
       "subtotal": 100,
       "items": [
         {
           "price": 25,
           "quantity": 4,
           "product_id": "TSHIRT"
         }
       ]
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","type":"Purchase","data":{"email":"customer@example.com","order_number":12,"order_date":"2014-03-14T05:49:54-07:00","subtotal":100,"items":[{"price":25,"quantity":4,"product_id":"TSHIRT"}]}}' \
        https://www.talkable.com/api/v2/origins

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "origin": {
         "id": 31386398,
         "order_number": 12,
         "subtotal": 100.0,
         "order_date": "2014-03-14T05:49:54.000-07:00",
         "customer_id": null,
         "type": "Purchase",
         "coupon_code": ""
       },
       "offer": {
         "short_url_code": "dZpBwd",
         "email": "customer@example.com",
         "show_url": "https://www.talkable.com/x/iXh4Je",
         "claim_url": "https://www.talkable.com/x/LSKEAX"
       }
     }
   }

Create an event
...............

.. code-block:: javascript

   {
     "api_key": "i9uil7nQgDjucCiTJu",
     "site_slug": "my-store",
     "type": "Event",
     "data": {
       "email": "customer@example.com",
       "event_category": "newsletter_subscription",
       "event_number": "42"
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","type":"Event","data":{"email":"customer@example.com","event_category":"newsletter_subscription","event_number":"42"}}' \
        https://www.talkable.com/api/v2/origins

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "origin": {
         "id": 46141478,
         "type": "Event",
         "event_number": "42",
         "event_category": "newsletter_subscription",
         "customer_id": null,
         "coupon_code": ""
       },
       "offer": {
         "short_url_code": "dZpBwd",
         "email": "customer@example.com",
         "show_url": "https://www.talkable.com/x/iXh4Je",
         "claim_url": "https://www.talkable.com/x/LSKEAX"
       }
     }
   }

Create an affiliate member
..........................

.. code-block:: javascript

   {
     "api_key": "i9uil7nQgDjucCiTJu",
     "site_slug": "my-store",
     "type": "AffiliateMember",
     "data": {
       "email": "affiliate@example.com"
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","type":"AffiliateMember","data":{"email":"affiliate@example.com"}}' \
        https://www.talkable.com/api/v2/origins

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "origin": {
         "id": 31386400,
         "email": "affiliate@example.com",
         "customer_id": null,
         "type": "AffiliateMember"
       },
       "offer": {
         "short_url_code": "Jp8qY9",
         "email": "affiliate@example.com",
         "show_url": "https://www.talkable.com/x/5BN5h7",
         "claim_url": "https://www.talkable.com/x/TM2OhR"
       }
     }
   }

.. container:: hidden

   .. toctree::
