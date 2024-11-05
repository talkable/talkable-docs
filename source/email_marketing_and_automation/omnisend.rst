.. _email_marketing_and_automation/omnisend:
.. include:: /partials/common.rst

.. meta::
   :description: Synchronize email opt-ins collected with Talkable to Omnisend for email marketing and automation.

Omnisend
========

With this integration, Talkable syncs email opt-ins to Omnisend, enabling streamlined customer data management for email marketing.

**Endpoint for Omnisend Integration:**
|br|
`POST <https://esp.talkable.com/omnisend>`_

**Params configuration for Omnisend integration**

.. code-block:: javascript

   const params = {
     email: "person-6ad487a3a0ccc1e7@talkable-sample.com", // required
     first_name: "John", // optional
     last_name: "Smith", // optional
     api_key: "NDMwDFdsdssEyMw==", // required
     opted_in_at: "{{ person.opted_in_at | format_date: format: \"%Y-%m-%mT%TZ\" }}" // specific format
   };

Support
-------
- Apps

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.