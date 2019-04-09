.. _web_hooks/offer_signup:
.. include:: /partials/common.rst

Advocate Signup Webhook
=======================

The Talkable Advocate Signup Webhook notifies your endpoint of an Advocate
Signup forms submission.

Use cases for the Advocate Signup Webhook include:

* Tracking when users select the checkbox to opt into your email newsletter
* Collection of data for Business Intelligence and analytics systems to track
  users who become Advocates
* Sending automated ‘Thank You’ emails after a user becomes an Advocate

.. raw:: html

   <h2>When does Talkable call the Advocate Signup Webhook?</h2>

Talkable Signup Webhook is triggered any time an Advocate Signup form is
submitted. The Advocate Signup form is the standard Name & Email (with optional
email subscription checkbox) fields a user submits before becoming an Advocate
and sharing an offer with Friends.

Advocate Signup Form example:

.. image:: /_static/img/advocate_signup_form_webhook.png
   :alt: Advocate Signup Form,
   :class: is-minimal

.. raw:: html

   <h2>Payload parameters provided for Advocate Signup Webhook</h2>

* **offer** — subhash of parameters describing the offer

  .. include:: /partials/offer_fields.rst

* **campaign** — subhash of parameters describing the campaign

  .. include:: /partials/campaign_fields.rst

* **email** — affiliate member’s email address

If the Signup form included first and last name fields or subscription checkbox,
additional parameters will be present:

* **first_name** — affiliate member’s first name
* **last_name** — affiliate member’s last name
* **username** — affiliate member’s username
* **sub_choice** — subscription choice
* **subscribed_at** — date affiliate member has subscribed
* **unsubscribed_at** — date affiliate member has unsubscribed
* **custom_properties** — hash of affiliate member’s custom properties (optional)
* **referral_counts** - subhash of |advocate|'s referral counts

  * **total** — created referrals count
  * **approved** — approved referrals count
  * **pending** — count of waiting for approval referrals

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "campaign": {
       "cached_slug": 615437538,
       "id": 615437538,
       "new_customer": null,
       "origin_max_age": null,
       "origin_min_age": null,
       "tag_names": ["default"],
       "type": "StandaloneCampaign"
     },
     "email": "john@example.com",
     "first_name": "John",
     "gender": null,
     "last_name": "Doe",
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV",
       "ip_address": "127.0.0.1"
     },
     "opted_in_at": null,
     "sub_choice": false,
     "subscribed_at": null,
     "unsubscribed_at": null,
     "referral_counts": {
       "total": 0,
       "approved": 0,
       "pending": 0
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"campaign":{"cached_slug":615437538,"id":615437538,"new_customer":null,"origin_max_age":null,"origin_min_age":null,"tag_names":["default"],"type":"StandaloneCampaign"},"email":"john@example.com","first_name":"John","gender":null,"last_name":"Doe","offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"opted_in_at":null,"sub_choice":false,"subscribed_at":null,"unsubscribed_at":null,"referral_counts":{"total":0,"approved":0,"pending":0}}' <url>

.. container:: hidden

   .. toctree::
