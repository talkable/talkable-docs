.. _email_marketing_and_automation/what_counts:
.. include:: /partials/common.rst

.. meta::
   :description: Synchronize emails Talkable collected with What Counts PRO integration.

What Counts PRO
===============

With this integration, Talkable synchronizes all people who opt in for Talkable email marketing during sign up. This way, you will keep all your emails in one place in an automated way.

**Endpoint for What Counts PRO Integration:**
|br|
`<https://esp.talkable.com/what-counts>`_

**Extras configuration for What Counts PRO integration**

.. code-block:: javascript

   const extras = {
     username: "realm",
     password: "lad2e30",
     list_id: "245",
     fields: {} // optional, custom fields, need to be pre-created in the ESP first
   };

Webhook Support
---------------
- Offer signup
- Claim signup
- Unsubscribe

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.
