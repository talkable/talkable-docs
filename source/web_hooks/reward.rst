.. _web_hooks/reward:
.. include:: /partials/common.rst

.. meta::
  :description: Reward Webhook notifies your endpoint that a reward is ready to be given, or it has been already given.

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

* Advocate Signup Form submitted (Reason = **signup**)
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

The sample payload with parameters for Reward Webhook is available here: `Reward Webhook Payload <https://www.talkable.com/api-docs/index.html?urls.primaryname=webhooks%20api&urls.primaryName=Webhooks#/Reward/post_your_api_reward_web_hook_path>`_.

.. raw:: html

  <h2>Reasons</h2>

Reward reason can be of 5 following general types.

* **signup** — Advocate reward for sign-up (Advocate Signup Form submitted)
* **shared** — Advocate reward for sharing an offer with Friend(s)
* **click** — Friend reward for visiting claim page (and optionally passing gating)
* **referrer** — Advocate reward for eligible referral purchase by Friend
* **referred** — Friend reward for eligible referral purchase by themselves

.. include:: /partials/incentive_types.rst

.. include:: /partials/coupon_as_reward.rst
