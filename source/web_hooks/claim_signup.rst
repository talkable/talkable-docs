.. _web_hooks/claim_signup:
.. include:: /partials/common.rst

Friend Email Gating Webhook
===========================

The Talkable Friend Email Gating Webhook notifies your endpoint that a Friend
Email Gating form was submitted (on Friend Claim Page).

Use cases for the Friend Email Gating Webhook include:

* Tracking when users select the checkbox to opt into your email newsletter
* Collection of data for Business Intelligence and analytics systems to track
  users who become Friends
* Sending automated ‘Thank You’ or 'Don’t forget to shop' emails after a Friend
  passes the email gating form

.. raw:: html

   <h2>When does Talkable call the Friend Email Gating Webhook?</h2>

Talkable Friend Email Gating Webhook is triggered any time an Friend Email
Gating form is submitted. This is the form a Friend completes after receiving
a share from an Advocate, and before receiving their discount code.

Friend Email Gating form example:

.. image:: /_static/img/friend_email_gating_form.png
   :alt: Friend Email Gating Form
   :class: is-minimal

.. raw:: html

   <h2>Payload parameters provided</h2>

* **offer** — subhash of parameters describing the offer

  .. include:: /partials/offer_fields.rst

* **campaign** — subhash of parameters describing the campaign

  .. include:: /partials/campaign_fields.rst
  * **origin_min_age** — The timeframe from first site visit when an offer is
    available to Advocate
  * **origin_max_age** — The timeframe from first site visit when an offer is
    available to Advocate
  * **new_customer** — either `null` - there is no criteria, `true` - only new
    customers could join into campaign and see advocate offer, or `false` -
    the same but for existing customers

* **email** — friend’s email address
* **first_name** — friend’s first name
* **last_name** — friend’s last name
* **ip_address** — friend’s IP address
* **sub_choice** — subscription choice (optional, present only if the form
  included subscription checkbox)
* **subscribed_at** — date friend has subscribed (deprecated; use opted_in_at instead)
* **opted_in_at** — date friend has subscribed (optional)
* **unsubscribed_at** — date friend has unsubscribed (optional)
* **referral_counts** - subhash of |advocate|'s referral counts

  * **total** — created referrals count
  * **approved** — approved referrals count
  * **pending** — count of waiting for approval referrals

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV",
       "ip_address": "127.0.0.1"
     },
     "campaign": {
       "id": 465427859,
       "type": "StandaloneCampaign",
       "cached_slug": 465427859,
       "tag_names": ["default"],
       "origin_min_age": null,
       "origin_max_age": null,
       "new_customer": null
     },
     "email": "john@example.com",
     "first_name": null,
     "last_name": null,
     "ip_address": "127.0.0.1",
     "sub_choice": true,
     "subscribed_at": "2018-09-27T22:54:28.345+03:00",
     "opted_in_at": "2018-09-27T22:54:28.345+03:00",
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

   curl --data 'key=<key>&site=<site>&type=claim_signup_web_hook&payload={"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"campaign":{"id":465427859,"type":"StandaloneCampaign","cached_slug":465427859,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"email":"john@example.com","first_name":null,"last_name":null,"ip_address":"127.0.0.1","sub_choice":true,"subscribed_at":"2018-09-27T22:54:28.345+03:00","opted_in_at":"2018-09-27T22:54:28.345+03:00","unsubscribed_at":null,"referral_counts":{"total":0,"approved":0,"pending":0}}' <url>

.. container:: hidden

   .. toctree::
