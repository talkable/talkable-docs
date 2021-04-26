.. _web_hooks/referral:
.. include:: /partials/common.rst

.. meta::
   :description: Referral Webhook notifies your endpoint that your brand Advocate’s referral status has become “Approved”.

Referral Webhook
================

The Talkable Referral Webhook notifies your endpoint that an |advocate| referral
status has become “Approved” specifically for a |friend| purchase
or event.

“Approved” referral status signifies the following:

* Neither Advocate nor Friend are blocked by email or IP
* Advocate passed enabled fraud checks and is considered non-fraudulent

Use cases for the Referral Webhook include:

* Providing account credit or account upgrades to an Advocate as a reward
* Giving non-monetary rewards such as physical gifts to an Advocate
* Sending automated ‘Thank You’ emails after a reward is given to an Advocate
* Data for business intelligence or analytics systems to track when Advocates receive rewards

.. note::

   “Approved” referral status does not guarantee that Advocate will receive a reward.

Things that can prevent Advocate or Friend from being rewarded:

* Share wasn't active at the moment of referral event creation
* Advocate Referral Incentive rewards limit (per month or in total) has been reached
* Coupon cycling has been detected (when Friend uses Advocate's coupon in referred event)
* Incentive criteria does not match
* Rewards issuing is not allowed for auto-approved referrals

.. important::

   Referral Webhook keeps retrying until it gets 2xx HTTP status in response.
   Only after that rewards associated with the referral can be paid.

.. raw:: html

   <h2>When does Talkable call the Referral Webhook?</h2>

Talkable Referral Webhook is triggered any time an Advocate referral status has become
“Approved” specifically for a Friend purchase or event.

.. note::

   Referral Webhook triggers only for Advocate rewards specifically from a Friend
   Purchase or Friend Event (such as signup event or subscription purchase event).
   To receive notification of both Advocate and Friend rewards use the Rewards Webhook.

.. raw:: html

   <h2>Payload parameters provided for Referral Webhook</h2>

* **campaign** — subhash of parameters describing the campaign

  .. include:: /partials/campaign_fields.rst

* **offer** — subhash of parameters describing the offer

  * **email** — |advocate| email address
  * **short_url_code** – unique offer ID
  * **ip_address**

* **referred_origin** - subhash with referred origin made by friend that created a referral

  .. include:: /partials/origin_fields.rst

* **advocate_rewards** — array of hashes describing the rewards received by |advocate|
  person (except for rewards paid in loyalty points), where each hash contains parameters:

  .. include:: /partials/reward_fields.rst

* **friend_rewards** — array of hashes describing the rewards received by referred person
  (except for rewards paid in loyalty points), where each hash contains parameters:

  .. include:: /partials/reward_fields.rst

* **share** — details about share:

  * **channel** — sharing channel involved in the referral

* **referrer** — Advocate referral incentive reward details (optional, absent if reward was paid in loyalty points)

  .. include:: /partials/reward_fields.rst

* **referred** — Friend referred incentive reward details (optional, absent if reward was paid in loyalty points)

  .. include:: /partials/reward_fields.rst

.. include:: /partials/coupon_as_reward.rst

.. include:: /partials/incentive_types.rst

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "campaign": {
       "id": 593427266,
       "type": "StandaloneCampaign",
       "cached_slug": 593427266,
       "tag_names": ["default"],
       "origin_min_age": null,
       "origin_max_age": null,
       "new_customer": null
       "joinable_category_names": ["affiliate_member"],
     },
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV",
       "ip_address": "127.0.0.1"
     },
     "referrer": {
       "id": 715729561,
       "email": "referrer@example.com",
       "person": {
         "email": "referrer@example.com",
         "first_name": "Bob",
         "last_name": "Crane",
         "sub_choice": false,
         "subscribed_at": null,
         "opted_in_at": null,
         "unsubscribed_at": null,
         "referral_counts": {
           "total": 0,
           "approved": 0,
           "pending": 0
         }
       },
       "amount": "5.00",
       "incentive": "rebate",
       "incentive_description": "$5.00 back",
       "origin": {
         "id": 159843498,
         "type": "AffiliateMember",
         "email": "referrer@example.com",
         "customer_id": "64227025",
         "ip_address": "127.0.0.1",
         "traffic_source": "unknown"
       }
     },
     "referred": {
       "id": 11192772,
       "email": "referred@example.com",
       "person": {
         "email": "referred@example.com",
         "first_name": "Alice",
         "last_name": "Smith",
         "username": null,
         "sub_choice": true,
         "subscribed_at": "2018-09-14T23:57:18.734+03:00",
         "opted_in_at": "2018-09-14T23:57:18.734+03:00",
         "unsubscribed_at": null,
         "referral_counts": {
           "total": 0,
           "approved": 0,
           "pending": 0
         },
         "custom_properties": {}
       },
       "amount": "0.00",
       "incentive": "other",
       "incentive_description": "First Month Free",
       "reward_coupon_code": null,
       "origin": {
         "id": 147886587,
         "type": "Purchase",
         "order_number": "450901776",
         "subtotal": 35.03,
         "customer_id": "565659001",
         "ip_address": "127.0.0.1",
         "coupon_code": "WHT29123",
         "traffic_source": "post-checkout"
       }
     },
     "advocate_rewards": [
       {
         "id": 715729561,
         "email": "referrer@example.com",
         "person": {
           "email": "referrer@example.com",
           "first_name": "Bob",
           "last_name": "Crane",
           "username": null,
           "sub_choice": false,
           "subscribed_at": null,
           "opted_in_at": null,
           "unsubscribed_at": null,
           "referral_counts": {
             "total": 0,
             "approved": 0,
             "pending": 0
           },
           "custom_properties": {}
         },
         "amount": "5.00",
         "incentive": "rebate",
         "incentive_description": "$5.00 back",
         "reward_coupon_code": null,
         "origin": {
           "id": 6400368,
           "type": "Purchase",
           "order_number": "459179054",
           "order_date": "2021-04-23T19:08:17.000-08:00"
           "subtotal": 11.39,
           "email": "referred@example.com"
           "customer_id": "376990942",
           "ip_address": "127.0.0.1",
           "coupon_code": "WHT59688",
           "traffic_source": "post-checkout"
         }
       }
     ],
     "friend_rewards": [
       {
         "id": 11192772,
         "email": "referred@example.com",
         "person": {
           "email": "referred@example.com",
           "first_name": "Alice",
           "last_name": "Smith",
           "username": null,
           "sub_choice": true,
           "subscribed_at": "2018-09-14T23:57:18.734+03:00",
           "opted_in_at": "2018-09-14T23:57:18.734+03:00",
           "unsubscribed_at": null,
           "referral_counts": {
             "total": 0,
             "approved": 0,
             "pending": 0
           },
           "custom_properties": {}
         },
         "amount": "0.00",
         "incentive": "other",
         "incentive_description": "First Month Free",
         "reward_coupon_code": null,
         "origin": {
           "id": 147886587,
           "type": "Purchase",
           "order_number": "450901776",
           "subtotal": 35.03,
           "customer_id": "565659001",
           "ip_address": "127.0.0.1",
           "coupon_code": "WHT29123",
           "traffic_source": "post-checkout"
         }
       }
     ],
     "referred_origin": {
       "id": 6400368,
       "type": "Purchase",
       "order_number": "459179054",
       "order_date": "2021-04-23T19:08:17.000-08:00"
       "subtotal": 11.39,
       "email": "referred@example.com"
       "customer_id": "376990942",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT59688",
       "traffic_source": "post-checkout"
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&site=<site>&type=referral_web_hook&payload={"campaign":{"id":593427266,"type":"StandaloneCampaign","cached_slug":593427266,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"referrer":{"id":715729561,"email":"referrer@example.com","person":{"email":"referrer@example.com","first_name":"Bob","last_name":"Crane","sub_choice":false,"subscribed_at":null,"opted_in_at":null,"unsubscribed_at":null,"referral_counts":{"total":0,"approved":0,"pending":0}},"amount":"5.00","incentive":"rebate","incentive_description":"$5.00 back","origin":{"id":159843498,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"64227025","ip_address":"127.0.0.1","traffic_source":"unknown"}},"referred":{"id":11192772,"email":"referred@example.com","person":{"email":"referred@example.com","first_name":"Alice","last_name":"Smith","sub_choice":true,"subscribed_at":"2018-09-14T23:57:18.734+03:00","opted_in_at":"2018-09-14T23:57:18.734+03:00","unsubscribed_at":null,"referral_counts":{"total":0,"approved":0,"pending":0}},"amount":"0.00","incentive":"other","incentive_description":"First Month Free","origin":{"id":147886587,"type":"Purchase","order_number":"450901776","subtotal":35.03,"customer_id":"565659001","ip_address":"127.0.0.1","coupon_code":"WHT29123","traffic_source":"post-checkout"}},"advocate_rewards":[{"id":715729561,"email":"referrer@example.com","person":{"email":"referrer@example.com","first_name":"Bob","last_name":"Crane","gender":null,"sub_choice":false,"subscribed_at":null,"opted_in_at":null,"unsubscribed_at":null,"referral_counts":{"total":0,"approved":0,"pending":0}},"amount":"5.00","incentive":"rebate","incentive_description":"$5.00 back","origin":{"id":159843498,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"64227025","ip_address": "127.0.0.1","traffic_source":"unknown"}}],"friend_rewards":[{"id":11192772,"email":"referred@example.com","person":{"email":"referred@example.com","first_name":"Alice","last_name":"Smith","sub_choice":true,"subscribed_at":"2018-09-14T23:57:18.734+03:00","opted_in_at":"2018-09-14T23:57:18.734+03:00","unsubscribed_at":null,"referral_counts":{"total":0,"approved":0,"pending":0}},"amount":"0.00","incentive":"other","incentive_description":"First Month Free","origin":{"id":147886587,"type":"Purchase","order_number":"450901776","subtotal":35.03,"customer_id":"565659001","ip_address":"127.0.0.1","coupon_code":"WHT29123","traffic_source":"post-checkout"}}],"referred_origin":{"id":6400368,"type":"Purchase","order_number":"459179054","subtotal":11.39,"customer_id":"376990942","ip_address":"127.0.0.1","coupon_code":"WHT59688","traffic_source":"post-checkout"}}' <url>

.. container:: hidden

   .. toctree::
