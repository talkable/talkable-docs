.. _email_marketing_and_automation/iterable:
.. include:: /partials/common.rst

.. meta::
   :description: Synchronize emails Talkable collected with Iterable integration.

Iterable
========

With this integration, Talkable synchronizes all people who opt in for Talkable email marketing during sign up. This way, you will keep all your emails in one place in an automated way.

**Endpoint for Iterable Integration:**
|br|
`<https://esp.talkable.com/iterable>`_

**Extras configuration for Iterable integration**

.. code-block:: javascript

   const extras = {
     api_key: "pk_8fbab84677f38e2dbbdc1eca9dce2f6a0f",
     list_id: "HMuLqd",
     fields: {
       signupSource: "referral",
       locale: "en",
       country: "us"
     }
   };

Webhook Support
---------------
- Offer signup
- Claim signup
- Unsubscribe

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.
