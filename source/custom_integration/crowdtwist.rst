.. _custom_integration/crowdtwist:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate store credit rewards using CrowdTwist API with Talkable.

CrowdTwist - Store Credit API
=============================

With this integration, Talkable enables store credit rewards through the CrowdTwist platform, allowing for custom incentives and campaign tagging.

**Endpoint for Store Credit API Integration:**
|br|
`<https://esp.talkable.com/crowdtwist/reward>`_

**Extras configuration for CrowdTwist store credit**

.. code-block:: javascript

   const extras = {
     api_key: "xxxxxx",
     api_url: "https://xxxxxx.crowdtwist.com",
     activity_id: "123456789",
     campaign_tags: "tag1,tag2"
   };

**Endpoint for User Check Integration:**
|br|
`<https://esp.talkable.com/crowdtwist/check_user>`_

**Extras configuration for CrowdTwist user check**

.. code-block:: javascript

   const extras = {
     api_key: "xxxxxx",
     api_url: "https://xxxxxx.crowdtwist.com",
     talkable_api_key: "xxxxxx"
   };

Webhook Support
---------------
- Reward (referrer incentive only)
- Referral

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.