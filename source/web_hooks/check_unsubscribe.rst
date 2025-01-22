.. _web_hooks/check_unsubscribe:
.. include:: /partials/common.rst

.. meta::
  :description: Check Unsubscribe Webhook ensures that emails are not sent to unsubscribed users.

Check Unsubscribe Webhook
=========================

Talkable Check Unsubscribe Webhook is used to ensure emails are not sent from
Talkable to user email addresses who have unsubscribed from the client side.
This is an optional functionality. Note: users do have the ability to unsubscribe
from Talkable referral related emails at any time from those emails directly.

.. raw:: html

  <h2>When does Talkable call the Check Unsubscribe Webhook?</h2>

Talkable Check Unsubscribe Webhook is triggered on every attempt to send an
otherwise valid customer email, aimed at checking if the email is also valid on
merchant side.

.. important::

  If this Check Unsubscribe Webhook is used, the response JSON returned by
  merchant must contain the following fields:

   .. code-block:: javascript

     { "result": { "unsubscribed": true } }

   The 'unsubscribed' field should have a boolean value,
   representing unsubscribed status according to the merchant info.

.. raw:: html

  <h2>Payload parameters provided</h2>

The sample payload with parameters for Check Unsubscribe Webhook is available here: `Check Unsubscribe Webhook Payload <https://www.talkable.com/api-docs/index.html?urls.primaryname=webhooks%20api&urls.primaryName=Webhooks#/Check%20Unsubscribe/post_your_api_check_unsubscribe_web_hook_path>`_.

.. raw:: html

  <h3>View categories</h3>

View category can be one of the following:

* notifier_offers_email
* notifier_offers_share_via_email
* notifier_offers_share_via_email_reminder
* advocate_rewards_confirmation
* advocate_rewards_paid
* friend_rewards_paid

.. container:: hidden

  .. toctree::
