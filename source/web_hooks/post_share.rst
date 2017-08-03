.. _web_hooks/post_share:
.. include:: /partials/common.rst

Post Share Web Hook
===================

Triggered when a |advocate| person shares offer details with referred persons via
corresponding form provided by campaign workflow.

.. raw:: html

   <h2>Payload parameters provided for Post Share Web Hook</h2>

* **campaign** — subhash of parameters describing the campaign

  * **id** — unique campaign ID
  * **cached_slug** — unique SEO friendly ID
  * **type** — either *"StandaloneCampaign"* or *"DoubleSidedDealCampaign"*
  * **tag_names** — array of campaign’s tags

* **share_type** — *"email"*, *"facebook"*, or *"twitter"*
* **share_info** — share-specific information

  * For Facebook share:

    * **facebook_share_post_id** — Facebook post ID
    * **facebook_share_user_id** — Facebook user ID

  * For email share:

    * **recipients** — array of email addresses

* **share_link** — link sent in share message (optional, present only for Facebook and Twitter shares)
* **origin** — contains data about the event that issued an offer:

  * **type**

    * *"Purchase"* for post-purchase campaign
    * *"AffiliateMember"* for standalone campaign

  * **id** — unique identifier of the origin event
  * **email** — e-mail address of the referrer person

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "campaign": {
       "id": 556735918,
       "type": "StandaloneCampaign",
       "cached_slug": "affiliate-campaign-test",
       "tag_names": ["default"]
     },
     "share_type": "email",
     "share_info": {
       "recipients": ["john@example.com"]
     },
     "origin": {
       "id": 199948681,
       "email": "sam@example.com",
       "type": "Purchase"
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"campaign":{"id":556735918,"type":"StandaloneCampaign","cached_slug":"affiliate-campaign-test","tag_names":["default"]},"share_type":"email","share_info":{"recipients":["john@example.com"]},"origin":{"id":199948681,"email":"sam@example.com","type":"Purchase"}}' <url>

.. container:: hidden

   .. toctree::
