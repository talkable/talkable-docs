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

The sample payload with parameters for Referral Webhook is available here: `Referral Webhook Payload <https://www.talkable.com/api-docs/index.html?urls.primaryname=webhooks%20api&urls.primaryName=Webhooks#/Referral/post_your_api_referral_web_hook_path>`_.

.. include:: /partials/coupon_as_reward.rst

.. include:: /partials/incentive_types.rst
