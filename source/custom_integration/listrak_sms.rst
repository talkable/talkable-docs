.. _custom_integration/listrak_sms:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate Listrak SMS with your Talkable system to sync phone numbers and send reward SMS messages.

Listrak SMS
===========

With this integration, Talkable syncs phone numbers to Listrak and allows the setup of reward SMS messages for campaigns, enhancing customer engagement through direct messaging.

**Endpoint for Listrak SMS Integration:**
|br|
`<https://esp.talkable.com/listrak/sms>`_

**Params configuration for Listrak SMS**

.. code-block:: javascript

   const params = {
     client_id: "xxxxxx",
     client_secret: "xxxxx",
     short_code_id: "704", // can only be obtained via Listrak Support
     email: "", // Email of the customer
     phone_list_id: "32Jsds",
     phone_number: "xxxx",
     message_id: "3760",
     message: "HERE IS YOUR COUPON WITH REWARD" // SMS text
   };

Support
-------
- Reward webhook for sending SMS rewards.

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.