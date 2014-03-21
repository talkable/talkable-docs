.. _web_hooks/referral:
.. include:: /partials/common.rst

Referral Web Hook
=================

Triggered when there is a new referral in Curebit.

.. raw:: html

   <h2>Payload parameters provided for Referral Web Hook</h2>

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign's tags

* **referrer** — subhash of parameters describing the reward received by a referrer person

  * **email** — email of the person that got reward
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

* **referred** — subhash of parameters describing the reward received by referred person

  * **email** — email of the person that got reward
  * **amount** — amount of money to reward (null when non-monetary incentive is used)
  * **incentive** — type of incentive reward (rebate, discount_coupon, other)
  * **incentive_description** — verbal reward explanation
  * **reward_coupon_code** — Coupon code received by person as a reward. Only in case when incetive equals discount_coupon.
  * **origin** — contains a data about Purchase that issued a referral

.. raw:: html

   <h2>Coupon codes as a reward</h2>

.. important::

   Any code sent via this web hook doesn't need to be created on merchant site.
   When Curebit needs more coupons — it always calls
   :ref:`Create Coupon Web Hook <web_hooks/create_coupon>`.
   In this web hook Curebit just sends the information to merchant that coupon
   was given as the reward in case merchant want to store this infomation in
   its own database.

.. raw:: html

   <h2>Incentive types</h2>

Incentives can be of 3 following general types.

* **rebate** — monetary reward, certain amount of money that should be paid out
  to a customer with a given email. Payment should be handled by the merchants'
  payment systems. In the case of automatic rebate payment, the merchant can
  connect their PayPal account to Curebit.
* **discount_coupon** — discount coupon is issued to customer. This type of
  incentives is handled by Curebit.
* **other** — used when a campaign has a non-monetary rebate like *"Free T-shirt"*
  or *"One Month Free"*. This should be handled on the merchant's side. More
  information on the reward is specified in *incentive_description*.

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

  {
    "campaign": {
      "id": 970078549,
      "type": "StandaloneCampaign",
      "cached_slug": "affiliate-campaign-test",
      "tag_names": ["default"]
    },
    "offer": {
      "email": "referrer@example.com",
      "short_url_code": "1a2PV"
    },
    "referrer": {
      "id": 384532015,
      "email": "referrer@example.com",
      "amount": "5.00",
      "incentive": "rebate",
      "incentive_description": "$5.00 back",
      "origin": {
        "id": 33810209,
        "type": "AffiliateMember",
        "email": "referrer@example.com"
      }
    },
    "referred": {
      "id": 648889141,
      "email": "referred@example.com",
      "amount": "0.00",
      "incentive": "other",
      "incentive_description": "First Month Free",
      "origin": {
        "id": 404180964,
        "type": "Purchase",
        "order_number": 605022930,
        "order_date": "2014-03-19T04:25:34.517-07:00",
        "customer_id": "50090390",
        "coupon_code": "WHT85956"
      }
    }
  }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"campaign":{"id":338380516,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV"},"referrer":{"id":320756779,"email":"referrer@example.com","amount":"5.00","incentive":"rebate","incentive_description":"$5.00 back","origin":{"id":599664225,"type":"AffiliateMember","email":"referrer@example.com"}},"referred":{"id":695132735,"email":"referred@example.com","amount":"0.00","incentive":"other","incentive_description":"First Month Free","origin":{"id":724069220,"type":"Purchase","order_number":580672632,"order_date":"2014-03-19T04:26:42.315-07:00","customer_id":"322031219","coupon_code":"WHT46606"}}}' <url>

.. container:: hidden

   .. toctree::
