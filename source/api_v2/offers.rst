.. _api_v2/offers:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to access Advocate offers.

Advocate Offers
===============

This API allows you to access advocate offers.

|br|

.. code-block:: text

   GET /offers/<id>

Returns advocate offer.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   id                Offer ID obtained with :ref:`origin creation <api_v2/origins>`.
   sharing_channels  Optional: array of social sharing channels for which will be
                     generated sharing links.

                     Options: `facebook`, `twitter`, `linkedin`, `sms`,
                     `other` or custom, except `email`, `reminder`,
                     `facebook_sponsored` and `coupon`.
   ================= ========================================================

Example
-------

.. code-block:: text

   GET https://www.talkable.com/api/v2/offers/89238912?site_slug=my-store

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "offer": {
         "id": 89238912,
         "short_url_code": "dZpBwd",
         "email": "customer@example.com",
         "show_url": "https://www.talkable.com/x/iEov9g",
         "claim_url": "https://www.talkable.com/x/5B3xO1",
         "coupon_code": null,
         "incentives": [
           "referrer": {
             "action_type": "referrer",
             "description": "$5",
             "percentage": false,
             "amount": 5,
             "criteria_config": {
               "new_customer": true,
               "new_optin": false,
               "subtotal_min": null,
               "subtotal_max": null,
               "referrals_min": null,
               "referrals_max": null,
               "reward_uniqueness": "once_per_friend",
               "friend_event_category": "purchase",
               "has_liquid_criteria": false
             },
             "for_advocate": true,
             "for_friend": false,
             "highest_amount": true,
             "identifier": "referrer",
             "incentive_type": "discount_coupon",
             "coupon_expires_at": null
           },
           "friend_new_customer": {
             "action_type": "click",
             "description": "$5",
             "percentage": false,
             "amount": 5,
             "criteria_config": {
               "once_per_person": true,
               "new_customer": true,
               "new_optin": false,
               "allow_on_expired_offer": false,
               "allow_on_self_referral": false,
               "has_liquid_criteria": false
             },
             "for_advocate": false,
             "for_friend": true,
             "highest_amount": true,
             "identifier": "friend_new_customer",
             "incentive_type": "discount_coupon",
             "coupon_expires_at": null
           }
         ],
         "trigger_widget": false,
         "campaign_tags": ["invite"]
       }
     }
   }

With sharing links
..................

.. code-block:: text

   GET https://www.talkable.com/api/v2/offers/89238912?site_slug=my-store&sharing_channels[]=facebook&sharing_channels[]=twitter&sharing_channels[]=custom

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "offer": {
         "id": 89238912,
         "short_url_code": "dZpBwd",
         "email": "customer@example.com",
         "show_url": "https://www.talkable.com/x/iEov9g",
         "claim_url": "https://www.talkable.com/x/5B3xO1",
         "coupon_code": null,
         "incentives": [
           "referrer": {
             "action_type": "referrer",
             "description": "$5",
             "percentage": false,
             "amount": 5,
             "criteria_config": {
               "new_customer": true,
               "new_optin": false,
               "subtotal_min": null,
               "subtotal_max": null,
               "referrals_min": null,
               "referrals_max": null,
               "reward_uniqueness": "once_per_friend",
               "friend_event_category": "purchase",
               "has_liquid_criteria": false
             },
             "for_advocate": true,
             "for_friend": false,
             "highest_amount": true,
             "identifier": "referrer",
             "incentive_type": "discount_coupon",
             "coupon_expires_at": null
           },
           "friend_new_customer": {
             "action_type": "click",
             "description": "$5",
             "percentage": false,
             "amount": 5,
             "criteria_config": {
               "once_per_person": true,
               "new_customer": true,
               "new_optin": false,
               "allow_on_expired_offer": false,
               "allow_on_self_referral": false,
               "has_liquid_criteria": false
             },
             "for_advocate": false,
             "for_friend": true,
             "highest_amount": true,
             "identifier": "friend_new_customer",
             "incentive_type": "discount_coupon",
             "coupon_expires_at": null
           }
         ],
         "trigger_widget": false,
         "campaign_tags": ["invite"]
       },
       "claim_links": {
         "facebook": "https://www.talkable.com/x/8L6xO2",
         "twitter": "https://www.talkable.com/x/KB89fO",
         "custom": "https://www.talkable.com/x/Yf794w"
       }
     }
   }
