.. _web_hooks/reward:
.. include:: /partials/common.rst

Reward Web Hook
===============

Triggered when there is a new paid reward in Curebit.

Rewards are considered as paid just after they are created, except Referrer:
it is getting paid after Referral is approved.

.. raw:: html

   <h2>Payload parameters provided for Reward Web Hook</h2>

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign's tags

* **person** — subhash of parameters describing the person that got reward (note: might be **null**)

  * **email**
  * **first_name**
  * **last_name**
  * **gender**
  * **sub_choice**

* **reward** — subhash of parameters describing the reward itself

  * **reason** — reason why this reward was given
  * **incentive_type** — type of incentive (rebate, discount_coupon, other)
  * **amount** — amount of money to reward (null when **incentive_type** is
    discount_coupon or other)
  * **coupon_code** — coupon code received by person as a reward (null when
    **incentive_type** is rebate or other)

.. raw:: html

   <h2>Reasons</h2>

Reward reason can be of 6 following general types.

* **referrer** — advocate reward for referral
* **referred** — friend reward for referral
* **shared** — advocate reward for social sharing
* **email_shared** — advocate reward for email sharing
* **signup** — advocate reward for signup
* **click** — friend reward for visiting claim page (and optionally passing gating)

.. include:: /partials/incentive_types.rst

.. include:: /partials/coupon_as_reward.rst

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

  {
    "person": {
      "email": "referrer@example.com",
      "first_name": "Bob",
      "gender": null,
      "last_name": "Smith",
      "sub_choice": true
    },
    "campaign": {
      "id": 146331555,
      "type": "StandaloneCampaign",
      "cached_slug": "affiliate-campaign-test",
      "tag_names": [
        "default"
      ]
    },
    "reward": {
      "reason": "referrer",
      "incentive_type": "rebate",
      "amount": 10.0,
      "coupon_code": null
    }
  }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":{"email":"referrer@example.com","first_name":"Bob","gender":null,"last_name":"Smith","sub_choice":true},"campaign":{"id":146331555,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"reward":{"reason":"referrer","incentive_type":"rebate","amount":10,"coupon_code":null}}' <url>

.. container:: hidden

   .. toctree::
