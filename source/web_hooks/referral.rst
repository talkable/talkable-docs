.. _web_hooks/referral:
.. include:: /partials/common.rst

Referral Web Hook
=================

Triggered whenever a referral status becomes “Approved” or “Unblocked”.

.. raw:: html

   <h2>Payload parameters provided for Referral Web Hook</h2>

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign’s tags

* **offer** — subhash of parameters describing the offer

  * **email** — referrer’s email address
  * **short_url_code**

* **referred_origin** - subhash with referred origin made by friend that created a referral

* **advocate_rewards** — array of hashes describing the rewards received by referrer person, where each hash contains parameters:

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
  * **reward_coupon_code** — Coupon code received by person as a reward. Only in case when incetive equals discount_coupon.
  * **origin** — contains data about the event that issued an offer:

    * **type**

      * *"Purchase"* for post-purchase campaign
      * *"AffiliateMember"* for standalone campaign

    * **id** — unique identifier of the origin event
    * **email** — e-mail address of the referrer person

* **friend_rewards** — array of hashes describing the rewards received by referred person, where each hash contains parameters:

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
  * **reward_coupon_code** — Coupon code received by person as a reward. Only in case when incetive equals discount_coupon.
  * **origin** — contains a data about Purchase that issued a referral

.. include:: /partials/coupon_as_reward.rst

.. include:: /partials/incentive_types.rst

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "campaign": {
       "id": 836929610,
       "type": "StandaloneCampaign",
       "cached_slug": "affiliate-campaign-test",
       "tag_names": ["default"]
     },
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV"
     },
     "referred_origin": {
       "id": 543208538,
       "type": "Purchase",
       "order_number": 381177444,
       "subtotal": 13.43,
       "customer_id": "22726076",
       "coupon_code": "WHT60000"
     },
     "advocate_rewards": [
       {
         "id": 316145153,
         "email": "referrer@example.com",
         "person": {
           "email": "referrer@example.com",
           "first_name": "Bob",
           "last_name": "Crane",
           "sub_choice": false,
           "subscribed_at": null,
           "unsubscribed_at": null
         },
         "amount": "5.00",
         "incentive": "rebate",
         "incentive_description": "$5.00 back",
         "origin": {
           "id": 667277390,
           "type": "AffiliateMember",
           "email": "referrer@example.com"
         }
       }
     ],
     "friend_rewards": [
       {
         "id": 884178819,
         "email": "referred@example.com",
         "person": {
           "email": "referred@example.com",
           "first_name": "Alice",
           "last_name": "Smith",
           "sub_choice": true,
           "subscribed_at": "2014-08-14T02:01:16.823-07:00",
           "unsubscribed_at": null
         },
         "amount": "0.00",
         "incentive": "other",
         "incentive_description": "First Month Free",
         "origin": {
           "id": 543208538,
           "type": "Purchase",
           "order_number": 381177444,
           "subtotal": 13.43,
           "order_date": "2014-08-14T02:01:16.824-07:00",
           "coupon_code": "WHT60000"
         }
       }
     ]
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl <url> \
     -d 'key=<key>&payload={
     "campaign": {
       "id": 836929610, "type": "StandaloneCampaign", "cached_slug": "affiliate-campaign-test", "tag_names": ["default"]
     },
     "offer": {
       "email": "referrer@example.com", "short_url_code": "1a2PV"
     },
     "referred_origin": {
       "id": 543208538, "type": "Purchase", "order_number": 381177444, "subtotal": 13.43, "customer_id": "22726076", "coupon_code": "WHT60000"
     },
     "advocate_rewards": [
       {
         "id": 316145153,
         "email": "referrer@example.com",
         "person": { "email": "referrer@example.com", "first_name": "Bob", "last_name": "Crane", "sub_choice": false, "subscribed_at": null, "unsubscribed_at": null },
         "amount": "5.00",
         "incentive": "rebate",
         "incentive_description": "$5.00 back",
         "origin": { "id": 667277390, "type": "AffiliateMember", "email": "referrer@example.com" }
       }
     ],
   }'

.. container:: hidden

   .. toctree::
