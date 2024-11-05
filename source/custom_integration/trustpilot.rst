.. _custom_integration/trustpilot:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate Trustpilot with your Talkable system to track reviews as events within campaigns.

Trustpilot
==========

With this integration, Talkable tracks reviews as events in campaigns using Trustpilot's webhook functionality, allowing reviews to be recorded and utilized in marketing efforts.

**Endpoint for Trustpilot Integration:**
|br|
https://esp.talkable.com/trustpilot/create_review

**Params configuration for Trustpilot integration**

The following parameters should be included in the webhook setup URL:

.. code-block:: javascript

   const params = {
     tkbl_api_key: "xEvK_ugGICqalZ6JU6_O",
     site: "maxim",
     username: "PVqoG8vbPGtbPVc0tQRYWANqp6u3vHkN",
     password: "PZAeAPy50JWuhghh",
     email: "alisa.zhernovska@talkable.com",
     account_pass: "QAZwsx11!!",
     business_unit_id: "6113fae6b264bb001d96576c"
   };

Support
-------
- Create a webhook in Trustpilot that points to the URL (endpoint + params).

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.