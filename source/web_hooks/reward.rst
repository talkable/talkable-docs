.. _web_hooks/reward:
.. include:: /partials/common.rst

Reward Web Hook
===============

Triggered when there is a new paid reward in Talkable.

Rewards are considered as paid just after they are created, except Referrer:
it is getting paid after Referral is approved.

.. raw:: html

   <h2>Payload parameters provided for Reward Web Hook</h2>

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign’s tags

* **person** — subhash of parameters describing the person that got reward (note: might be **null**)

  * **email**
  * **first_name**
  * **last_name**
  * **sub_choice**
  * **subscribed_at**
  * **unsubscribed_at**

* **origin** — subhash of data related to the event that issued an offer

  * **type**

    * *"Purchase"* for post-purchase campaign
    * *"AffiliateMember"* for standalone campaign

  * **id** — unique identifier of the origin event
  * **email** — e-mail address of the referrer person

* **reward** — subhash of parameters describing the reward itself

  * **reason** — reason why this reward was given
  * **incentive_type** — type of incentive (rebate, discount_coupon, other)
  * **incentive_description** — description of incentive (human readable, equals to non monetary description if **incentive_type** is other)
  * **amount** — amount of money to reward (null when **incentive_type** is
    discount_coupon or other)
  * **coupon_code** — coupon code received by person as a reward (null when
    **incentive_type** is rebate or other)

* **advocate_origin** - subhash of data related to the advocate event

  * **type**

    * *"Purchase"* for post-purchase campaign
    * *"AffiliateMember"* for standalone campaign

  * **id** — unique identifier of the advocate’s origin event

   *For Affiliate Member:*

  * **email** — e-mail address of the referrer person

   *For Purchase:*

  * **order_number** - unique identifier of advocate’s order
  * **subtotal** - advocate’s order subtotal
  * **customer_id** - unique identifier of advocate
  * **order_date** - advocate’s order date in ISO 8601 format

* **friend_origin** - subhash of data related to the friend event

  * **type**

    * *"Purchase"* for post-purchase campaign
    * *"Event"* for custom campaign

  * **id** — unique identifier of the friend’s origin
  * **order_number** - unique identifier of friend’s order
  * **subtotal** - friend’s order subtotal
  * **customer_id** - unique identifier of friend
  * **order_date** - friend’s order date in ISO 8601 format

.. raw:: html

   <h2>Reasons</h2>

Reward reason can be of 6 following general types.

* **referrer** — advocate reward for referral
* **referred** — |friend| reward for referral
* **shared** — advocate reward for social sharing
* **email_shared** — advocate reward for email sharing
* **signup** — advocate reward for signup
* **click** — |friend| reward for visiting claim page (and optionally passing gating)

.. include:: /partials/incentive_types.rst

.. include:: /partials/coupon_as_reward.rst

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "person": {
       "email": "referrer@example.com",
       "first_name": "Bob",
       "last_name": "Smith",
       "sub_choice": true,
       "subscribed_at": "2014-08-13T11:14:08.835-07:00",
       "unsubscribed_at": null
     },
     "origin": {
       "id": 736588136,
       "type": "Purchase",
       "order_number": "698175656",
       "subtotal": 18.76,
       "customer_id": "222388260",
       "order_date": "2016-11-11T07:33:03.968-08:00",
       "coupon_code": "WHT86000"
     },
     "campaign": {
       "id": 146331555,
       "type": "StandaloneCampaign",
       "cached_slug": "affiliate-campaign-test",
       "tag_names": ["default"]
     },
     "reward": {
       "id": 44089,
       "reason": "referrer",
       "incentive_type": "rebate",
       "incentive_description": "$10.00 back",
       "amount": 10.0,
       "coupon_code": null,
       "status": "Paid"
     },
     "advocate_origin": {
       "id": 736588136,
       "type": "Purchase",
       "order_number": "698175656",
       "subtotal": 18.76,
       "customer_id": "222388260",
       "order_date": "2016-11-11T07:33:03.968-08:00",
       "coupon_code": "WHT86000"
     },
     "friend_origin": {
       "id": 82271,
       "type": "Purchase",
       "order_number": "991701634",
       "subtotal": 25.39,
       "customer_id": "842273988",
       "order_date": "2016-11-11T07:33:50.625-08:00",
       "coupon_code": "WHT75815"
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":{"email":"referrer@example.com","first_name":"Bob","last_name":"Smith","sub_choice":true,"subscribed_at":"2014-08-13T11:14:08.835-07:00","unsubscribed_at":null},"origin":{"id":736588136,"type":"Purchase","order_number":"698175656","subtotal":18.76,"customer_id":"222388260","order_date":"2016-11-11T07:33:03.968-08:00","coupon_code":"WHT86000"},"campaign":{"id":146331555,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"reward":{"id":44089,"reason":"referrer","incentive_type":"rebate","incentive_description":"$10.00 back","amount":10.0,"coupon_code":null,"status":"Paid"},"advocate_origin":{"id":736588136,"type":"Purchase","order_number":"698175656","subtotal":18.76,"customer_id":"222388260","order_date":"2016-11-11T07:33:03.968-08:00","coupon_code":"WHT86000"},"friend_origin":{"id":82271,"type":"Purchase","order_number":"991701634","subtotal":25.39,"customer_id":"842273988","order_date":"2016-11-11T07:33:50.625-08:00","coupon_code":"WHT75815"}}' <url>

.. container:: hidden

   .. toctree::
