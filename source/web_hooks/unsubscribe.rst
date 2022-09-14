.. _web_hooks/unsubscribe:
.. include:: /partials/common.rst

.. meta::
   :description: Unsubscribe Webhook notifies you that a user has unsubscribed from Talkable referral email.

Unsubscribe Webhook
===================

Talkable Unsubscribe Webhook provides notification of a user unsubscribing from
Talkable sent referral email.

Use cases for the Unsubscribe Webhook include:

* Unsubscribing users from in-house marketing newsletters when user unsubscribes
  from Talkable referral emails
* Any event that should be triggered when a user unsubscribes from Talkable
  referral emails

.. raw:: html

   <h2>When does Talkable call the Unsubscribe Webhook?</h2>

Talkable Unsubscribe Webhook is called any time a user unsubscribes from a
Talkable sent email.

.. raw:: html

   <h2>Payload parameters provided</h2>

* **person** — subhash of parameters describing the person

  .. include:: /partials/person_fields.rst
  .. |person| replace:: person

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "person": {
       "first_name": "Bob",
       "last_name": "Smith",
       "email": "referrer@example.com",
       "phone_number": "+12025551111",
       "username": "username",
       "unsubscribed_at": null,
       "subscribed_at": "2018-09-27T22:55:13.860+03:00",
       "opted_in_at": "2018-09-27T22:55:13.860+03:00",
       "phone_opted_in_at": "2018-09-27T22:55:13.860+03:00",
       "sub_choice": true,
       "referral_counts": {
         "total": 0,
         "approved": 0,
         "pending": 0
       },
       "custom_properties": {},
       "is_loyalty_member": false,
       "loyalty_member": null
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl <url> \
        -d "key=<key>" \
        -d "site=<site>" \
        -d "type=unsubscribe_web_hook" \
        -d "extras={}" \
        -d 'payload={"person":{"first_name":"Bob","last_name":"Smith","email":"referrer@example.com","phone_number":"+12025551111","username":"username","unsubscribed_at":null,"subscribed_at":"2018-09-27T22:55:13.860+03:00","opted_in_at":"2018-09-27T22:55:13.860+03:00","phone_opted_in_at":"2018-09-27T22:55:13.860+03:00","sub_choice":true,"referral_counts":{"total":0,"approved":0,"pending":0},"custom_properties":{},"is_loyalty_member":false,"loyalty_member":null}}'

.. container:: hidden

   .. toctree::
