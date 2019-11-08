.. _web_hooks/check_unsubscribe:
.. include:: /partials/common.rst

.. meta::
   :description: Talkable Check Unsubscribe Webhook ensures that emails are not sent to unsubscribed users.

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

* **campaign** — subhash of parameters describing the campaign

  .. include:: /partials/campaign_fields.rst

* **recipient** — subhash of parameters describing the recipient

  * **first_name** — recipient’s first name
  * **last_name** — recipient’s last name
  * **email** — recipient’s email address
  * **username** — recipient’s username
  * **unsubscribed_at** — date recipient has unsubscribed
  * **subscribed_at** — date person has subscribed (deprecated; use opted_in_at instead)
  * **opted_in_at** — date recipient has subscribed
  * **sub_choice** — subscription choice
  * **custom_properties** — hash of recipient’s custom properties (optional)
  * **referral_counts** - subhash of |advocate|'s referral counts

    * **total** — created referrals count
    * **approved** — approved referrals count
    * **pending** — count of waiting for approval referrals

* **email_type** — described view category

.. raw:: html

   <h3>View categories</h3>

View category can be one of the following:

* notifier_offers_email
* notifier_offers_share_via_email
* notifier_offers_share_via_email_reminder
* advocate_rewards_confirmation
* advocate_rewards_paid
* friend_rewards_paid

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "campaign": {
       "id": 509365458,
       "type": "StandaloneCampaign",
       "cached_slug": 509365458,
       "tag_names": ["default"],
       "origin_min_age": null,
       "origin_max_age": null,
       "new_customer": null
     },
     "recipient": {
       "first_name": "Bob",
       "last_name": "Smith",
       "email": "referrer@example.com",
       "username": "username",
       "unsubscribed_at": null,
       "subscribed_at": "2018-09-27T22:55:40.610+03:00",
       "opted_in_at": "2018-09-27T22:55:40.610+03:00",
       "sub_choice": true,
       "referral_counts": {
         "total": 0,
         "approved": 0,
         "pending": 0
       }
     },
     "email_type": "notifier_offers_email"
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&site=<site>&type=check_unsubscribe_web_hook&payload={"campaign":{"id":509365458,"type":"StandaloneCampaign","cached_slug":509365458,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"recipient":{"first_name":"Bob","last_name":"Smith","email":"referrer@example.com","username":"username","unsubscribed_at":null,"subscribed_at":"2018-09-27T22:55:40.610+03:00","opted_in_at":"2018-09-27T22:55:40.610+03:00","sub_choice":true,"referral_counts":{"total":0,"approved":0,"pending":0}},"email_type":"notifier_offers_email"}' <url>

.. container:: hidden

   .. toctree::
