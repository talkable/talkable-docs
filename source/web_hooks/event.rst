.. _web_hooks/event:
.. include:: /partials/common.rst

.. meta::
   :description: Event Webhook lets you know when a purchase was made.

Event Webhook
=============

The Talkable Event Webhook notifies your endpoint that an :ref:`Event <advanced_features/events>`
or a :ref:`Purchase <integration/custom/integration_components/post_purchase_script>` has been
registered with Talkable.

Use cases for the Event Webhook include:

* Capturing purchases and custom referral events generated by the customer (e.g. added data to profile or renewed a subscription)
* Tracking coupon codes used for purchases
* Using Talkable events to trigger custom workflows (e.g. add a custom property to a customer who just cancelled a subscription)

.. raw:: html

   <h2>When does Talkable call the Event Webhook?</h2>

Talkable calls the Event Webhook any time an Event or a Purchase
is registered either via :ref:`the front-end Talkable integration <advanced_features/events>`
or using the :ref:`Talkable backend API <api_v2/origins>`.

.. raw:: html

   <h2>Payload parameters provided</h2>

* **origin** — subhash of data describing the event that triggered the webhook.

  * **type**

    * *"Purchase"* for purchases.
    * *"Event"* for custom events.

  *For Purchase:*

     * **email** - email address associated with the Purchase
     * **order_number** - unique identifier of the Purchase
     * **customer_id** - unique external identifier of a customer who made the purchase
     * **subtotal** - order subtotal for the purchase
     * **coupon_code** - coupon code used with the purchase
     * **traffic_source** - traffic source of the Purchase
     * **ip_address** - IP address of the Purchase

  *For Event:*

     * **email** - email address associated with the Event
     * **event_category** - identifier of an action that trigger the Event (e.g. ``app_installed``)
     * **event_number** - unique identifier of the Event within the associated **event_category**
     * **customer_id** - unique external identifier of a customer who triggered the event
     * **subtotal** - optional monetary attribute of the Event
     * **coupon_code** - optional coupon code associated with the Event
     * **traffic_source** - traffic source of the Event
     * **ip_address** - IP address of the Event

* **person** - subhash of data describing the person who triggered the event

    .. include:: /partials/person_fields.rst

.. raw:: html

   <h2>Sample payload | Event</h2>

.. code-block:: javascript

   {
     "origin": {
       "id": 289738874,
       "type": "Event",
       "event_number": "953205549",
       "event_category": "webhook-test",
       "subtotal": 91.52,
       "customer_id": "865955119",
       "order_date": "2019-04-11T07:26:17.272-07:00",
       "coupon_code": "WHT28499",
       "ip_address": "127.0.0.1",
       "traffic_source": "post-event"
     },
     "person": {
       "first_name": "Bob",
       "last_name": "Smith",
       "email": "referrer@example.com",
       "username": "username",
       "unsubscribed_at": null,
       "subscribed_at": "2019-04-11T07:25:17.272-07:00",
       "opted_in_at": "2019-04-11T07:25:17.272-07:00",
       "sub_choice": true,
       "referral_counts": {
         "total": 0,
         "approved": 0,
         "pending": 0
       },
       "is_loyalty_member": false,
       "loyalty_member": null
     }
   }

.. raw:: html

   <h2>cURL example | Event</h2>

.. code-block:: bash

   curl --data 'key=<key>&site=<site>&type=event_web_hook&payload={"origin":{"id":998181034,"type":"Event","event_number":"352670218","event_category":"webhook-test","subtotal":21.36,"customer_id":"472735863","order_date":"2019-04-16T06:20:47.079-07:00","coupon_code":"WHT65226","ip_address":"127.0.0.1","traffic_source":"post-event"},"person":{"first_name":"Bob","last_name":"Smith","email":"referrer@example.com","username":"username","unsubscribed_at":null,"subscribed_at":"2019-04-16T06:19:47.079-07:00","opted_in_at":"2019-04-16T06:19:47.079-07:00","sub_choice":true}}' <url>

.. raw:: html

   <h2>Sample payload | Purchase</h2>

.. code-block:: javascript

   {
     "origin": {
       "id": 654689661,
       "type": "Purchase",
       "order_number": "426692385",
       "subtotal": 29.39,
       "customer_id": "162638070",
       "order_date": "2019-04-11T07:28:31.258-07:00",
       "coupon_code": "WHT79679",
       "ip_address": "127.0.0.1",
       "traffic_source": "post-checkout"
     },
     "person": {
       "first_name": "Bob",
       "last_name": "Smith",
       "email": "referrer@example.com",
       "username": "username",
       "unsubscribed_at": null,
       "subscribed_at": "2019-04-11T07:27:31.258-07:00",
       "opted_in_at": "2019-04-11T07:27:31.258-07:00",
       "sub_choice": true,
       "referral_counts": {
         "total": 0,
         "approved": 0,
         "pending": 0
       },
       "is_loyalty_member": false,
       "loyalty_member": null
     }
   }

.. raw:: html

   <h2>cURL example | Purchase</h2>

.. code-block:: bash

   curl --data 'key=<key>&site=<site>&type=event_web_hook&payload={"origin":{"id":654689661,"type":"Purchase","order_number":"426692385","subtotal":29.39,"customer_id":"162638070","order_date":"2019-04-11T07:28:31.258-07:00","coupon_code":"WHT79679","ip_address":"127.0.0.1","traffic_source":"post-checkout"},"person":{"first_name":"Bob","last_name":"Smith","email":"referrer@example.com","username":"username","unsubscribed_at":null,"subscribed_at":"2019-04-11T07:27:31.258-07:00","opted_in_at":"2019-04-11T07:27:31.258-07:00","sub_choice":true}}' <url>

.. container:: hidden

   .. toctree::
