.. _web_hooks/offer_signup:
.. include:: /partials/common.rst

Advocate Signup Web Hook
========================

Triggered when Advocate Signup form is submitted.

.. raw:: html

   <h2>Payload parameters provided for Advocate Signup Web Hook</h2>

* **offer** — subhash of parameters describing the offer

  * **email** — referrer’s email address
  * **short_url_code**

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign’s tags

* **email** — affiliate member’s email address

If the Signup form included first and last name fields or subscription checkbox,
additional parameters will be present:

* **first_name** — affiliate member’s first name
* **last_name** — affiliate member’s last name
* **sub_choice** — subscription choice
* **subscribed_at** — date affiliate member has subscribed
* **unsubscribed_at** — date affiliate member has unsubscribed

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "offer": {
       "email": "referrer@example.com",
       "short_url_code": "1a2PV"
     },
     "campaign": {
       "id": 361325654,
       "type": "StandaloneCampaign",
       "cached_slug": "affiliate-campaign-test",
       "tag_names": ["default"]
     },
     "email": "john@example.com",
     "first_name": "John",
     "last_name": "Doe",
     "gender": null,
     "sub_choice": false,
     "subscribed_at": "2014-08-14T02:01:16.824-07:00",
     "unsubscribed_at": null
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"offer":{"email":"referrer@example.com","short_url_code":"1a2PV"},"campaign":{"id":361325654,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"email":"john@example.com","first_name":"John","last_name":"Doe","gender":null,"sub_choice":false,"subscribed_at":"2014-08-14T02:01:16.824-07:00","unsubscribed_at":null}' <url>

.. container:: hidden

   .. toctree::
