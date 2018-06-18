.. _web_hooks/check_unsubscribe:
.. include:: /partials/common.rst

Check Unsubscribe Web Hook
==========================

Triggered on every attempt to send an otherwise valid customer email,
aimed at checking if the email is also valid on merchant side.

.. important::

   If this web hook is used, the response returned by merchant
   must contain the following fields:

   .. code-block:: javascript

      { "result": { "unsubscribed": true } }

   The 'unsubscribed' field should have a boolean value,
   representing unsubscribed status according to the merchant info.

.. raw:: html

   <h2>Payload parameters provided </h2>

* **for_<view category>** — subhash of parameters describing the person

  * **campaign** — subhash of parameters describing the campaign

    * **id** — unique campaign ID
    * **cached_slug** — unique SEO friendly ID
    * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
    * **tag_names** — array of campaign’s tags

  * **recipient** — subhash of parameters describing the recipient

    * **first_name** — recipient's first name
    * **last_name** — recipient's last name
    * **email** — recipient's email address
    * **username** — recipient's username
    * **unsubscribed_at** — date recipient has unsubscribed
    * **opted_in_at** — date recipient has subscribed
    * **sub_choice** — subscription choice
    * **custom_properties** — hash of recipient’s custom properties (optional)

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
     "for_friend_rewards_paid": {
       "campaign": {
         "id": 350256053,
         "type": "StandaloneCampaign",
         "cached_slug": "affiliate-campaign-test",
         "tag_names": ["default"]
       },
       "recipient": {
         "first_name": "Bob",
         "last_name": "Smith",
         "email": "friend@example.com",
         "username": "username",
         "unsubscribed_at": null,
         "opted_in_at": "2014-08-13T11:14:08.835-07:00",
         "sub_choice": true
       },
       "email_type": "friend_rewards_paid"
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"for_friend_rewards_paid":{"campaign":{"id": 350256053,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"recipient":{"first_name":"Bob","last_name":"Smith","email":"friend@example.com","username":"username","unsubscribed_at":null,"opted_in_at":"2014-08-13T11:14:08.835-07:00","sub_choice":true},"email_type":"friend_rewards_paid"}}' <url>

.. container:: hidden

   .. toctree::
