.. _web_hooks/claim_signup:
.. include:: /partials/common.rst

Friend Email Gating Web Hook
============================

Triggered when Friend Email Gating form is submitted (on Friend Claim Page).

.. raw:: html

   <h2>Payload parameters provided for Advocate Signup Web Hook</h2>

* **offer** — subhash of parameters describing the offer

  * **email** — referrer's email address
  * **short_url_code**

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign's tags

* **email** — affiliate member's email address
* **first_name** — affiliate member's first name
* **last_name** — affiliate member's last name
* **sub_choice** — subscription choice (optional, present only if the form included subscription checkbox)

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV"
     },
     "campaign": {
       "id": 350256053,
       "type": "StandaloneCampaign",
       "cached_slug": "affiliate-campaign-test",
       "tag_names": ["default"]
     },
     "email": "john@example.com",
     "first_name": null,
     "last_name": null,
     "gender": null,
     "sub_choice": true
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"offer":{"email":"referrer@example.com","short_url_code":"1a2PV"},"campaign":{"id":350256053,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"email":"john@example.com","first_name":null,"last_name":null,"gender":null,"sub_choice":true}' <url>

.. container:: hidden

   .. toctree::
