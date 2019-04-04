.. _web_hooks/reward:
.. include:: /partials/common.rst

Reward Webhook
==============

The Talkable Reward Webhook notifies your endpoint that a reward is ready to be,
or has been given. A reward can be for either an Advocate or for a Friend.
Talkable Reward Webhook notifications allow your application to know when to
reward users by means other than the standard ‘give them a coupon code’ method.

Use cases for the Reward Webhook include:

* Providing account credit or account upgrades to a user as a reward
* Giving non-monetary rewards such as physical gifts
* Sending automated ‘Thank You’ emails after a reward is given to a user
* Any event that should trigger at the moment a user has earned a reward

.. raw:: html

   <h2>When does Talkable call the Reward Webhook?</h2>

Talkable calls the Reward Webhook any time a reward is ready to be, or has been
given to either an Advocate or a Friend according to the logic set-up in a
Talkable referral campaign.

Possible events which will trigger the Reward Webhook are:

* Advocate Signup form submitted (Reason = **signup**)
* Advocate shares an offer with Friend(s) (Reason = **shared**)
* Friend passes email gating form (Reason = **click**)

  .. note::

     If campaign is setup without email gating form, Reward Webhook with
     Reason = click will trigger when Friend clicks through to site.

* Friend makes eligible purchase (Reason = **referrer**)
* Friend makes eligible purchase (Reason = **referred**)

  .. note::

     Reason = referrer indicates a reward should be given to an Advocate.
     Reason = referred indicates a reward should be given to a Friend.

.. raw:: html

   <h2>Set-Up</h2>

Because the Reward Webhook will trigger at various events depending on the
Incentive configuration for each referral campaign, to trigger the Reward
Webhook we first must ensure Incentives are correctly configured.
To configure incentives:

1. Navigate to **Campaigns** then select the campaign you would like to
   configure incentives for
2. Proceed to **Rules** then scroll down to **Incentives** section where
   incentives for both Advocates and Friends can be set-up

.. image:: /_static/img/advocate_referral_incentive.png
   :alt: Edit Referral Incentives,
   :class: is-minimal

3. Configure the incentives as desired inside the Referral Incentive Editor.
   To configure Incentive types other than Coupon Codes, please contact your
   Talkable Customer Success Manager; they will be able to set up “Rebate (store
   credit)” type incentives and “Non-Monetary” type incentives.

.. note::

   If there is a delay configured into when the Advocate reward is approved then
   the Reward Webhook trigger when the Advocate reward is ready to be, or has
   been given. For example, if campaigns are set to send an Advocate their reward
   three days after a Friend makes an eligible purchase, then the Reward Webhook
   will be called three days after the Friend makes the eligible purchase. You
   can select these delays under **Fraud Settings**, which is found under **Menu**.

Once incentives are configured for a referral campaign, Talkable will then call
the Reward Webhook any time either an Advocate or a Friend should receive a
reward. Now, the Reward  Webhook can be set-up. :ref:`Learn more about General
Webhook Set Up Steps <web_hooks>`

.. raw:: html

   <h2>Payload parameters provided by Reward Webhook</h2>

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign’s tags

* **offer** — subhash of parameters describing the offer

  * **email** — referrer’s (Advocate's) email address
  * **short_url_code**

* **person** — subhash of parameters describing the person that got reward (note: might be **null**)

  * **email**
  * **first_name**
  * **last_name**
  * **sub_choice**
  * **opted_in_at**
  * **unsubscribed_at**

* **origin** — subhash of data related to the event that issued an offer

  * **type**

    * *"Purchase"* for post-purchase campaign
    * *"AffiliateMember"* for standalone campaign

  * **id** — unique identifier of the origin event
  * **email** — email address of the referrer (Advocate) person

* **reward** — subhash of parameters describing the reward itself

  * **reason** — reason why this reward was given
  * **incentive_type** — type of incentive (rebate, discount_coupon, other)
  * **incentive_description** — description of incentive (human readable, equals
    to non monetary description if **incentive_type** is other)
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

  * **email** — email address of the referrer (Advocate) person

   *For Purchase:*

  * **order_number** - unique identifier of advocate’s order
  * **subtotal** - advocate’s order subtotal
  * **email** - advocate’s email address
  * **customer_id** - unique identifier of advocate

* **friend_origin** - subhash of data related to the friend event

  * **type**

    * *"Purchase"* for post-purchase campaign
    * *"Event"* for custom campaign

  * **id** — unique identifier of the friend’s origin
  * **order_number** - unique identifier of friend’s order
  * **subtotal** - friend’s order subtotal
  * **email** - friend’s email address
  * **customer_id** - unique identifier of friend

.. raw:: html

   <h2>Reasons</h2>

Reward reason can be of 5 following general types.

* **signup** — Advocate reward for sign-up (Advocate Signup form submitted)
* **shared** — Advocate reward for sharing an offer with Friend(s)
* **click** — Friend reward for visiting claim page (and optionally passing gating)
* **referrer** — Advocate reward for eligible referral purchase by Friend
* **referred** — Friend reward for eligible referral purchase by themselves

.. include:: /partials/incentive_types.rst

.. include:: /partials/coupon_as_reward.rst

.. raw:: html

   <h2>Sample payload | Reason = signup</h2>

.. code-block:: javascript

   {
     "person": null,
     "origin": {
       "id": 186742865,
       "type": "AffiliateMember",
       "email": "referrer@example.com",
       "customer_id": "910930418",
       "ip_address": "127.0.0.1"
     },
     "advocate_origin": {
       "id": 186742865,
       "type": "AffiliateMember",
       "email": "referrer@example.com",
       "customer_id": "910930418",
       "ip_address": "127.0.0.1"
     },
     "friend_origin": null,
     "campaign": {
       "id": 500548529,
       "type": "StandaloneCampaign",
       "cached_slug": 500548529,
       "tag_names": ["default"],
       "origin_min_age": null,
       "origin_max_age": null,
       "new_customer": null
     },
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV"
     },
     "reward": {
       "id": 8261257,
       "reason": "signup",
       "incentive_type": "discount_coupon",
       "incentive_description": "signup coupon \"SAMPLE-COUPON-CODE\" for $10.00 off",
       "incentive_custom_description": null,
       "amount": "10.0",
       "coupon": {
         "code": "SAMPLE-COUPON-CODE",
         "active": true,
         "valid_until": null,
         "single_use": false,
         "used": false,
         "usages": null,
         "amount": 10.0,
         "percentage_discount": null,
         "description": "$10",
         "id": 60477154,
         "expires_at": null
       },
       "coupon_code": "SAMPLE-COUPON-CODE",
       "status": "Paid"
     }
   }

.. raw:: html

   <h2>cURL example | Reason = signup</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":null,"origin":{"id":186742865,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"910930418","ip_address":"127.0.0.1"},"advocate_origin":{"id":186742865,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"910930418","ip_address":"127.0.0.1"},"friend_origin":null,"campaign":{"id":500548529,"type":"StandaloneCampaign","cached_slug":500548529,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"reward":{"id":8261257,"reason":"signup","incentive_type":"discount_coupon","incentive_description":"signup coupon \"SAMPLE-COUPON-CODE\" for $10.00 off","incentive_custom_description":null,"amount":"10.0","coupon":{"code":"SAMPLE-COUPON-CODE","active":true,"valid_until":null,"single_use":false,"used":false,"usages":null,"amount":10.0,"percentage_discount":null,"description":"$10","id":60477154,"expires_at":null},"coupon_code":"SAMPLE-COUPON-CODE","status":"Paid"}}' <url>

.. raw:: html

   <h2>Sample payload | Reason = shared</h2>

.. code-block:: javascript

   {
     "person": null,
     "origin": {
       "id": 186742865,
       "type": "AffiliateMember",
       "email": "referrer@example.com",
       "customer_id": "910930418",
       "ip_address": "127.0.0.1"
     },
     "advocate_origin": {
       "id": 186742865,
       "type": "AffiliateMember",
       "email": "referrer@example.com",
       "customer_id": "910930418",
       "ip_address": "127.0.0.1"
     },
     "friend_origin": null,
     "campaign": {
       "id": 500548529,
       "type": "StandaloneCampaign",
       "cached_slug": 500548529,
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
     "reward": {
       "id": 8260964,
       "reason": "shared",
       "incentive_type": "discount_coupon",
       "incentive_description": "shared coupon \"SAMPLE-COUPON-CODE\" for $10.00 off",
       "incentive_custom_description": null,
       "amount": "10.0",
       "coupon": {
         "code": "SAMPLE-COUPON-CODE",
         "active": true,
         "valid_until": null,
         "single_use": false,
         "used": false,
         "usages": null,
         "amount": 10.0,
         "percentage_discount": null,
         "description": "$10",
         "id": 60477154,
         "expires_at": null
       },
       "coupon_code": "SAMPLE-COUPON-CODE",
       "status": "Paid"
     }
   }

.. raw:: html

   <h2>cURL example | Reason = shared</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":null,"origin":{"id":186742865,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"910930418","ip_address":"127.0.0.1"},"advocate_origin":{"id":186742865,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"910930418","ip_address":"127.0.0.1"},"friend_origin":null,"campaign":{"id":500548529,"type":"StandaloneCampaign","cached_slug":500548529,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"reward":{"id":8260964,"reason":"shared","incentive_type":"discount_coupon","incentive_description":"shared coupon \"SAMPLE-COUPON-CODE\" for $10.00 off","incentive_custom_description":null,"amount":"10.0","coupon":{"code":"SAMPLE-COUPON-CODE","active":true,"valid_until":null,"single_use":false,"used":false,"usages":null,"amount":10.0,"percentage_discount":null,"description":"$10","id":60477154,"expires_at":null},"coupon_code":"SAMPLE-COUPON-CODE","status":"Paid"}}' <url>

.. raw:: html

   <h2>Sample payload | Reason = click</h2>

.. code-block:: javascript

   {
     "person": null,
     "origin": null,
     "advocate_origin": {
       "id": 395950177,
       "type": "AffiliateMember",
       "email": "referrer@example.com",
       "customer_id": "180484020",
       "ip_address": "127.0.0.1"
     },
     "friend_origin": null,
     "campaign": {
       "id": 312538309,
       "type": "StandaloneCampaign",
       "cached_slug": 312538309,
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
     "reward": {
       "id": 8261304,
       "reason": "click",
       "incentive_type": "discount_coupon",
       "incentive_description": "shared coupon \"SAMPLE-COUPON-CODE\" for $10 off",
       "incentive_custom_description": null,
       "amount": "10.0",
       "coupon": {
         "code": "SAMPLE-COUPON-CODE",
         "active": true,
         "valid_until": null,
         "single_use": false,
         "used": false,
         "usages": null,
         "amount": 10.0,
         "percentage_discount": null,
         "description": "$10",
         "id": 60477154,
         "expires_at": null
       },
       "coupon_code": "SAMPLE-COUPON-CODE",
       "status": "Paid"
     }
   }

.. raw:: html

   <h2>cURL example | Reason = click</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":null,"origin":null,"advocate_origin":{"id":395950177,"type":"AffiliateMember","email":"referrer@example.com","customer_id":"180484020","ip_address":"127.0.0.1"},"friend_origin":null,"campaign":{"id":312538309,"type":"StandaloneCampaign","cached_slug":312538309,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"reward":{"id":8261304,"reason":"click","incentive_type":"discount_coupon","incentive_description":"shared coupon \"SAMPLE-COUPON-CODE\" for $10 off","incentive_custom_description":null,"amount":"10.0","coupon":{"code":"SAMPLE-COUPON-CODE","active":true,"valid_until":null,"single_use":false,"used":false,"usages":null,"amount":10.0,"percentage_discount":null,"description":"$10","id":60477154,"expires_at":null},"coupon_code":"SAMPLE-COUPON-CODE","status":"Paid"}}' <url>

.. raw:: html

   <h2>Sample payload | Reason = referrer</h2>

.. code-block:: javascript

   {
     "person": {
       "first_name": "Bob",
       "last_name": "Smith",
       "email": "referrer@example.com",
       "username": "username",
       "unsubscribed_at": null,
       "subscribed_at": "2018-08-27T21:42:23.060+03:00",
       "opted_in_at": "2018-08-27T21:42:23.060+03:00",
       "sub_choice": true,
       "referral_counts": {
         "total": 0,
         "approved": 0,
         "pending": 0
       }
     },
     "origin": {
       "id": 280695079,
       "type": "Purchase",
       "order_number": "288015920",
       "subtotal": "6.31",
       "customer_id": "230652117",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT25279"
     },
     "advocate_origin": {
       "id": 280695079,
       "type": "Purchase",
       "order_number": "288015920",
       "subtotal": "6.31",
       "customer_id": "230652117",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT25279"
     },
     "friend_origin": {
       "id": 264084636,
       "type": "Purchase",
       "order_number": "4190583",
       "subtotal": "73.41",
       "email": "referred@example.com",
       "customer_id": "323518374",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT40052"
     },
     "campaign": {
       "id": 484002505,
       "type": "StandaloneCampaign",
       "cached_slug": 484002505,
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
     "reward": {
       "id": 8261305,
       "reason": "referrer",
       "incentive_type": "rebate",
       "incentive_description": "$10.00 back",
       "incentive_custom_description": null,
       "amount": "10.0",
       "coupon": {},
       "coupon_code": null,
       "status": "Paid"
     }
   }

.. raw:: html

   <h2>cURL example | Reason = referrer</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":{"first_name":"Bob","last_name":"Smith","email":"referrer@example.com","username":"username","unsubscribed_at":null,"subscribed_at":"2018-08-27T21:42:23.060+03:00","opted_in_at":"2018-08-27T21:42:23.060+03:00","sub_choice":true,"referral_counts":{"total":0,"approved":0,"pending":0}},"origin":{"id":280695079,"type":"Purchase","order_number":"288015920","subtotal":"6.31","customer_id":"230652117","ip_address":"127.0.0.1","coupon_code":"WHT25279"},"advocate_origin":{"id":280695079,"type":"Purchase","order_number":"288015920","subtotal":"6.31","customer_id":"230652117","ip_address":"127.0.0.1","coupon_code":"WHT25279"},"friend_origin":{"id":264084636,"type":"Purchase","order_number":"4190583","subtotal":"73.41","email":"referred@example.com","customer_id":"323518374","ip_address":"127.0.0.1","coupon_code":"WHT40052"},"campaign":{"id":484002505,"type":"StandaloneCampaign","cached_slug":484002505,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"reward":{"id":8261305,"reason":"referrer","incentive_type":"rebate","incentive_description":"$10.00 back","incentive_custom_description":null,"amount":"10.0","coupon":{},"coupon_code":null,"status":"Paid"}}' <url>

.. raw:: html

   <h2>Sample payload | Reason = referred</h2>

.. code-block:: javascript

   {
     "person": {
       "first_name": "Matt",
       "last_name": "Smith",
       "email": "friend@example.com",
       "username": "username",
       "unsubscribed_at": null,
       "subscribed_at": "2018-08-27T21:45:29.519+03:00",
       "opted_in_at": "2018-08-27T21:45:29.519+03:00",
       "sub_choice": true,
       "referral_counts": {
         "total": 0,
         "approved": 0,
         "pending": 0
       }
     },
     "origin": {
       "id": 818629076,
       "type": "Purchase",
       "order_number": "416466456",
       "subtotal": "48.39",
       "email": "referred@example.com",
       "customer_id": "401088820",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT862"
     },
     "advocate_origin": {
       "id": 77856467,
       "type": "Purchase",
       "order_number": "529868349",
       "subtotal": "25.76",
       "customer_id": "937735146",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT15105"
     },
     "friend_origin": {
       "id": 818629076,
       "type": "Purchase",
       "order_number": "416466456",
       "subtotal": "48.39",
       "email": "referred@example.com",
       "customer_id": "401088820",
       "ip_address": "127.0.0.1",
       "coupon_code": "WHT862"
     },
     "campaign": {
       "id": 944706822,
       "type": "StandaloneCampaign",
       "cached_slug": 944706822,
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
     "reward": {
       "id": 8261300,
       "reason": "referred",
       "incentive_type": "rebate",
       "incentive_description": "$10.00 back",
       "incentive_custom_description": null,
       "amount": "10.0",
       "coupon": {},
       "coupon_code": null,
       "status": "Paid"
     }
   }

.. raw:: html

   <h2>cURL example | Reason = referred</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":{"first_name":"Matt","last_name":"Smith","email":"friend@example.com","username":"username","unsubscribed_at":null,"subscribed_at":"2018-08-27T21:45:29.519+03:00","opted_in_at":"2018-08-27T21:45:29.519+03:00","sub_choice":true,"referral_counts":{"total":0,"approved":0,"pending":0}},"origin":{"id":818629076,"type":"Purchase","order_number":"416466456","subtotal":"48.39","email":"referred@example.com","customer_id":"401088820","ip_address":"127.0.0.1","coupon_code":"WHT862"},"advocate_origin":{"id":77856467,"type":"Purchase","order_number":"529868349","subtotal":"25.76","customer_id":"937735146","ip_address":"127.0.0.1","coupon_code":"WHT15105"},"friend_origin":{"id":818629076,"type":"Purchase","order_number":"416466456","subtotal":"48.39","email":"referred@example.com","customer_id":"401088820","ip_address":"127.0.0.1","coupon_code":"WHT862"},"campaign":{"id":944706822,"type":"StandaloneCampaign","cached_slug":944706822,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV","ip_address":"127.0.0.1"},"reward":{"id":8261300,"reason":"referred","incentive_type":"rebate","incentive_description":"$10.00 back","incentive_custom_description":null,"amount":"10.0","coupon":{},"coupon_code":null,"status":"Paid"}}' <url>

.. container:: hidden

   .. toctree::
