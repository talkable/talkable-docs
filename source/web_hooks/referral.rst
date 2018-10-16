.. _web_hooks/referral:
.. include:: /partials/common.rst

Referral Webhook
================

The Talkable Referral Webhook notifies your endpoint that an |advocate| referral
status has become “Approved” or “Unblocked” specifically for a |friend| purchase
or event.

Use cases for the Referral Webhook include:

* Providing account credit or account upgrades to an Advocate as a reward
* Giving non-monetary rewards such as physical gifts to an Advocate
* Sending automated ‘Thank You’ emails after a reward is given to an Advocate
* Data for business intelligence or analytics systems to track when Advocates receive rewards

.. raw:: html

   <h2>When does Talkable call the Referral Webhook?</h2>

Talkable Referral Webhook is triggered any time an Advocate referral status has become
“Approved” or “Unblocked” specifically for a Friend purchase or event.

**Note:** Referral Webhook triggers only for Advocate rewards specifically from a Friend
Purchase or Friend Event (such as signup event or subscription purchase event).
To receive notification of both Advocate and Friend rewards use the Rewards Webhook.

.. raw:: html

   <h2>Payload parameters provided for Referral Webhook</h2>

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign’s tags

* **offer** — subhash of parameters describing the offer

  * **email** — |advocate| email address
  * **short_url_code** – unique offer ID
  * **ip_address**

* **referred_origin** - subhash with referred origin made by friend that created a referral

* **advocate_rewards** — array of hashes describing the rewards received by |advocate|
  person, where each hash contains parameters:

  * **email** — email of the person that got reward
  * **person** — subhash of parameters describing the person that got reward

    * **email**
    * **first_name**
    * **last_name**
    * **sub_choice**
    * **subscribed_at**
    * **unsubscribed_at**

  * **amount** — amount of money to reward (null when non-monetary incentive is used)
  * **incentive** — type of incentive reward (`rebate`, `discount_coupon`, `other`)
  * **incentive_description** — verbal reward explanation
  * **reward_coupon_code** — Coupon code received by person as a reward. Only in case when
    incentive equals `discount_coupon`.
  * **origin** — contains data about the event that issued an offer:

    * **type**

      * *"Purchase"* for post-purchase placement
      * *"AffiliateMember"* for standalone, floating widget, or gleam placements
      * *"Event"* for post-event placement

    * **id** — unique identifier of the origin event
    * **email** — email address of the |advocate| person

* **friend_rewards** — array of hashes describing the rewards received by referred person,
  where each hash contains parameters:

  * **email** — email of the person that got reward
  * **person** — subhash of parameters describing the person that got reward

    * **email**
    * **first_name**
    * **last_name**
    * **sub_choice**
    * **subscribed_at**
    * **unsubscribed_at**

  * **amount** — amount of money to reward (null when non-monetary incentive is used)
  * **incentive** — type of incentive reward (rebate, discount_coupon, other)
  * **incentive_description** — verbal reward explanation
  * **reward_coupon_code** — Coupon code received by person as a reward. Only in case when
    incetive equals discount_coupon.
  * **origin** — contains a data about Purchase that issued a referral

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
         "unsubscribed_at": null
       },
       "amount": "5.00",
       "incentive": "rebate",
       "incentive_description": "$5.00 back",
       "origin": {
         "id": 159843498,
         "type": "AffiliateMember",
         "email": "referrer@example.com",
         "customer_id": "64227025",
         "ip_address": "127.0.0.1"
       }
     },
     "referred": {
       "id": 11192772,
       "email": "referred@example.com",
       "person": {
         "email": "referred@example.com",
         "first_name": "Alice",
         "last_name": "Smith",
         "sub_choice": true,
         "subscribed_at": "2018-09-14T23:57:18.734+03:00",
         "opted_in_at": "2018-09-14T23:57:18.734+03:00",
         "unsubscribed_at": null
       },
       "amount": "0.00",
       "incentive": "other",
       "incentive_description": "First Month Free",
       "origin": {
         "id": 147886587,
         "type": "Purchase",
         "order_number": "450901776",
         "subtotal": 35.03,
         "customer_id": "565659001",
         "ip_address": "127.0.0.1",
         "coupon_code": "WHT29123"
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
           "gender": null,
           "sub_choice": false,
           "subscribed_at": null,
           "opted_in_at": null,
           "unsubscribed_at": null
         },
         "amount": "5.00",
         "incentive": "rebate",
         "incentive_description": "$5.00 back",
         "origin": {
           "id": 159843498,
           "type": "AffiliateMember",
           "email": "referrer@example.com",
           "customer_id": "64227025",
           "ip_address": "127.0.0.1"
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
           "sub_choice": true,
           "subscribed_at": "2018-09-14T23:57:18.734+03:00",
           "opted_in_at": "2018-09-14T23:57:18.734+03:00",
           "unsubscribed_at": null
         },
         "amount": "0.00",
         "incentive": "other",
         "incentive_description": "First Month Free",
         "origin": {
           "id": 147886587,
           "type": "Purchase",
           "order_number": "450901776",
           "subtotal": 35.03,
           "customer_id": "565659001",
           "ip_address": "127.0.0.1",
           "coupon_code": "WHT29123"
         }
       }
     ],
     "referred_origin": {
       "id": 6400368,
       "type": "Purchase",
       "order_number": "459179054",
       "subtotal": 11.39,
       "customer_id": "376990942",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT59688"
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"campaign":{"id":593427266,"type":"StandaloneCampaign","cached_slug":593427266,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"referrer":{"id":715729561,"email":"referrer@example.com","person":{"email":"referrer@example.com","first_name":"Bob","last_name":"Crane","sub_choice":false,"subscribed_at":null,"opted_in_at":null,"unsubscribed_at":null},"amount":"5.00","incentive":"rebate","incentive_description":"$5.00 back","origin":{"id":159843498,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"64227025","ip_address":"127.0.0.1"}},"referred":{"id":11192772,"email":"referred@example.com","person":{"email":"referred@example.com","first_name":"Alice","last_name":"Smith","sub_choice":true,"subscribed_at":"2018-09-14T23:57:18.734+03:00","opted_in_at":"2018-09-14T23:57:18.734+03:00","unsubscribed_at":null},"amount":"0.00","incentive":"other","incentive_description":"First Month Free","origin":{"id":147886587,"type":"Purchase","order_number":"450901776","subtotal":35.03,"customer_id":"565659001","ip_address":"127.0.0.1","coupon_code":"WHT29123"}},"advocate_rewards":[{"id":715729561,"email":"referrer@example.com","person":{"email":"referrer@example.com","first_name":"Bob","last_name":"Crane","gender":null,"sub_choice":false,"subscribed_at":null,"opted_in_at":null,"unsubscribed_at":null},"amount":"5.00","incentive":"rebate","incentive_description":"$5.00 back","origin":{"id":159843498,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"64227025","ip_address": "127.0.0.1"}}],"friend_rewards":[{"id":11192772,"email":"referred@example.com","person":{"email":"referred@example.com","first_name":"Alice","last_name":"Smith","sub_choice":true,"subscribed_at":"2018-09-14T23:57:18.734+03:00","opted_in_at":"2018-09-14T23:57:18.734+03:00","unsubscribed_at":null},"amount":"0.00","incentive":"other","incentive_description":"First Month Free","origin":{"id":147886587,"type":"Purchase","order_number":"450901776","subtotal":35.03,"customer_id":"565659001","ip_address":"127.0.0.1","coupon_code":"WHT29123"}}],"referred_origin":{"id":6400368,"type":"Purchase","order_number":"459179054","subtotal":11.39,"customer_id":"376990942","ip_address":"127.0.0.1","coupon_code":"WHT59688"}}' <url>

.. container:: hidden

   .. toctree::
