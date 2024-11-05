.. _custom_integration/validity:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate Validity with your Talkable system for additional email validation within campaigns.

Validity
========

With this integration, Talkable performs additional validation on email addresses using the Validity service, helping to maintain accurate and clean customer data.

**Endpoint for Validity Integration:**
|br|
`POST <https://esp.talkable.com/validity>`_

**Params configuration for Validity integration**

.. code-block:: javascript

   const params = {
     email: "person-6ad487a3a0ccc1e7@talkable-sample.com", // required
     api_key: "6ad487a3a0ccc1e76ad487a3a0ccc1e7" // required
   };

Support
-------
- Custom app (click reward verification) - Returns true if email is valid

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.