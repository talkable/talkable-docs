.. _web_hooks/post_share:
.. include:: /partials/common.rst

Post Share Webhook
==================

Talkable Post Share Webhook provides notification of a share event performed
within a referral campaign workflow. Use cases for the Post Share Webhook include:

  * Sending automated 'Thank You' email to an Advocate for performing a share
  * Any event that should be triggered when a user shares
  * Data for Business Intelligence and analytics systems

.. raw:: html

   <h2>When does Talkable call the Post Share Webhook?</h2>

Talkable Post Share Webhook is triggered any time an |advocate| (referrer)
shares offer details with a |friend| (referee) via the corresponding form
provided by campaign workflow. Which includes any time:

  * An advocate shares with a Friend via Email or any other channel from inside
    a referral campaign workflow
  * An Advocate copies a share link from a referral campaign workflow share screen

Note: the Post Share Webhook triggers every time a share occurs. For example,
if an Advocate shares with a Friend via email (or any channel), then shares with
a second Friend via email (or any channel), the Post Share Webhook will be
triggered twice.

.. raw:: html

   <h2>Payload parameters provided for Post Share Webhook</h2>

* **campaign** — subhash of parameters describing the campaign

  .. include:: /partials/campaign_fields.rst
  * **origin_min_age** — timeframe from first site visit when an offer is
    available to Advocate
  * **origin_max_age** — timeframe from first site visit when an offer is
    available to Advocate
  * **new_customer** — “yes/no” whether offer requires Advocate to be a new
    customer

* **share_type** — *"email"*, *"facebook"*, *"twitter"*, *"facebook_message"*,
  *"facebook_sponsored"*, *"whatsapp"*, *"sms"*, *"linkedin"*, *"other"*

  * Note: custom share_type's can be created

* **share_info** — share-specific information

  * For Facebook share:

    * **facebook_share_post_id** — Facebook post ID
    * **facebook_share_user_id** — Facebook user ID

  * For email share:

    * **recipients** — an array of email addresses

* **share_link** — link sent in share message (optional, present only for
  Facebook and Twitter shares)
* **origin** — contains data about the event that issued an offer:

  .. include:: /partials/origin_fields.rst

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "campaign": {
       "id": 83587635,
       "type": "StandaloneCampaign",
       "cached_slug": 83587635,
       "tag_names": ["default"],
       "origin_min_age": null,
       "origin_max_age": null,
       "new_customer": null
     },
     "share_type": "email",
     "share_info": {
       "recipients": ["john@example.com"]
     },
     "origin": {
       "id": 273085748,
       "type": "Purchase",
       "email": "referrer@example.com"
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&site=<site>&type=post_share_web_hook&payload={"campaign":{"id":83587635,"type":"StandaloneCampaign","cached_slug":83587635,"tag_names":["default"],"origin_min_age":null,"origin_max_age":null,"new_customer":null},"share_type":"email","share_info":{"recipients":["john@example.com"]},"origin":{"id":273085748,"type":"Purchase","email":"referrer@example.com"}}' <url>

.. container:: hidden

   .. toctree::
