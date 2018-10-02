.. _api_v2/origins:
.. include:: /partials/common.rst

Origins
=======

This API allows you to create origins. See examples below.

|br|

.. code-block:: text

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
                     * uuid (optional) - uuid given to a visitor on a claim page. See :ref:`Referral Program via API <api_v2/flow>`
                     * ip_address (optional) - IP address of client who is making the request. You might pass `current` string as a value so remote IP will be used
                     * traffic_source (optional) - specific :ref:`Traffic Source <advanced_features/traffic_source>` value that helps to distinguish different points of integration
                     * campaign_tags (optional) - campaign tags for offer targeting
                     * sharing_channels (optional) - array of social sharing channels
                       for which will be generated sharing links

                     For Purchase:

                     * subtotal
                     * order_number
                     * items (optional)
                     * coupon_code (optional)

                     For Event:

                     * event_number
                     * event_category
                     * subtotal (optional)
                     * coupon_code (optional)
   ================= ========================================================

Example
-------

Create a purchase
.................

.. code-block:: javascript

   {
     "site_slug": "my-store",
     "type": "Purchase",
     "data": {
       "email": "customer@example.com",
       "order_number": 12,
       "subtotal": 100,
       "uuid": "b3967d36-4e7f-46bc-92b3-57344347cd6a",
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
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","type":"Purchase","data":{"email":"customer@example.com","order_number":12,"subtotal":100,"items":[{"price":25,"quantity":4,"product_id":"TSHIRT"}]}}' \
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
         "customer_id": null,
         "ip_address": "127.0.0.1",
         "type": "Purchase",
         "coupon_code": ""
       },
       "offer": null
     }
   }

Create an event
...............

.. code-block:: javascript

   {
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
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","type":"Event","data":{"email":"customer@example.com","event_category":"newsletter_subscription","event_number":"42"}}' \
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
         "ip_address": "127.0.0.1",
         "coupon_code": ""
       },
       "offer": null
     }
   }

Create an affiliate member and target a campaign
................................................

.. code-block:: javascript

   {
     "site_slug": "my-store",
     "type": "AffiliateMember",
     "data": {
       "email": "affiliate@example.com",
       "campaign_tags": ["invite"]
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","type":"AffiliateMember","data":{"email":"affiliate@example.com","campaign_tags":["invite"]}}' \
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
         "ip_address": "127.0.0.1",
         "type": "AffiliateMember"
       },
       "offer": {
         "id": 89238912,
         "short_url_code": "Jp8qY9",
         "email": "affiliate@example.com",
         "show_url": "https://www.talkable.com/x/5BN5h7",
         "claim_url": "https://www.talkable.com/x/TM2OhR"
       }
     }
   }

With sharing links
..................

.. code-block:: javascript

   {
     "site_slug": "my-store",
     "type": "AffiliateMember",
     "data": {
       "email": "affiliate@example.com",
       "campaign_tags": ["invite"],
       "sharing_channels": ["facebook", "twitter", "custom"]
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","type":"AffiliateMember","data":{"email":"affiliate@example.com","campaign_tags":["invite"],"sharing_channels":["facebook","twitter","custom"]}}' \
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
         "ip_address": "127.0.0.1",
         "type": "AffiliateMember"
       },
       "offer": {
         "short_url_code": "Jp8qY9",
         "email": "affiliate@example.com",
         "show_url": "https://www.talkable.com/x/5BN5h7",
         "claim_url": "https://www.talkable.com/x/TM2OhR"
       },
       "claim_links": {
         "facebook": "https://www.talkable.com/x/8L6xO2",
         "twitter": "https://www.talkable.com/x/KB89fO",
         "custom": "https://www.talkable.com/x/Yf794w"
       }
     }
   }

.. container:: hidden

   .. toctree::
