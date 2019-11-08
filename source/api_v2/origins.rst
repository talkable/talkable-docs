.. _api_v2/origins:
.. include:: /partials/common.rst

.. meta::
   :description: The Talkable Origins API allows the registration of ‘off-site’ or ‘backend’ purchases, or CRM events. That means they can be used in the referral flow.

Origins
=======

The Talkable Origins API allows the registration of ‘off-site’ or ‘backend’
purchases or CRM events so they can be used in the referral flow. This
functionality is generally utilized by businesses using subscription billing,
off-site transactions, or other off-site events.

.. note::

   The :ref:`standard front-end <integration/custom/overview>` Talkable
   integration will capture all one-time purchases happening on the client
   e-commerce site, but will not on its own capture purchases or CRM events
   happening on the backend. To do this, the Origins API must be utilized to
   feed ‘off-site’ or ‘backend’ purchases or CRM events to Talkable.

.. raw:: html

   <h2>Example use cases for the Origins API</h2>

**Subscription:**

* A company whose customers sign up for a monthly service by making an initial
  ‘on-site’ payment, then are charged monthly on the backend for subsequent
  subscription payments. This company would like to reward |advocate| users
  (referrers) with a reward after their |friend| has been a member for three
  billing cycles.

  * Talkable’s :ref:`standard front-end <integration/custom/overview>`
    integration captures the initial ‘on-site’ payment.

  * For Talkable to reward the |Advocate| after the third billing cycle of the
    |friend| subscription, the Company must pass the subsequent subscription
    data to Talkable’s Origins API using ``"type": "Event"``.

**Off-Site Events:**

* A company whose customers purchase product or perform events off-site. This
  company would like to reward |advocate| users (referrers) with a reward after
  their |friend| has purchased a product in the brick and mortar store, or
  attended an in-person appointment.

  * Talkable’s :ref:`standard front-end <integration/custom/overview>`
    integration captures an initial ‘on-site’ signup event if there is one.

  * For Talkable to reward the |advocate| after the in-person |friend| store
    purchase, or appointment attendance, the Company must pass the in store
    purchase, or appointment attendance data to Talkable’s Origins API with
    either ``"type": "Purchase"`` for a purchase or ``"type": "Event"`` for an
    appointment attendance.

**User Approval:**

* User approval use cases start with customers who need to submit an application
  by performing an initial ‘on-site’ sign-up event. This company would like to
  reward |advocate| users (referrers) with a reward after their |friend|
  application is approved.

  * Talkable’s :ref:`standard front-end <integration/custom/overview>`
    integration captures the initial ‘on-site’ application sign-up event.

  * In order for Talkable to reward the |advocate| after the |friend|
    application approval, the Company must pass the approval data to Talkable’s
    Origins API using ``"type": "Event"``.

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
