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
       "id": 323228316,
       "type": "StandaloneCampaign",
       "cached_slug": "affiliate-campaign-test",
       "tag_names": ["default"]
     },
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV"
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"campaign":{"id":323228316,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"offer":{"email":"referrer@example.com","short_url_code":"1a2PV"}}' <url>

.. container:: hidden

   .. toctree::
