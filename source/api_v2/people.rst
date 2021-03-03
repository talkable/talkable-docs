.. _api_v2/people:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to access and update the list of people.

People
======

This API allows you to access and update persons. See examples below.

|br|

.. code-block:: text

   GET /people/<person_slug>

Returns a person.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email or username
   ================= ========================================================

|br|

.. code-block:: text

   GET /people/<person_slug>/referrals_as_advocate

Returns referrals where person is an advocate.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email or username
   ================= ========================================================

|br|

.. code-block:: text

   GET /people/<person_slug>/rewards

Returns rewards that person has earned in referral program.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email or username
   ================= ========================================================

|br|

.. code-block:: text

   GET /people/<person_slug>/shares_by

Returns shares that person made.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email or username
   ================= ========================================================

|br|

.. code-block:: text

   PUT /people/<person_slug>

Updates an existing person or creates one if it does not exist.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email
   data              JSON object with one or more of following properties:

                     * first_name
                     * last_name
                     * username
                     * customer_id
                     * person_custom_properties

   ================= ========================================================

|br|

.. code-block:: text

   POST /people/<person_slug>/unsubscribe

Unsubscribes a person from receiving emails.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email
   ================= ========================================================

|br|

.. code-block:: text

   POST /people/<person_slug>/anonymize

Anonymizes a person.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email
   ================= ========================================================

|br|

.. code-block:: text

   GET /people/<person_slug>/personal_data

Returns personal data.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email
   ================= ========================================================

Example
-------

Find a person by email
......................

.. code-block:: text

   GET https://www.talkable.com/api/v2/people/customer@example.com?site_slug=my-store

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "https://share.mystore.com/by/customer@example.com",
         "events_count": 0,
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": null,
         "subscribed_at": null,
         "unsubscribed_at": null,
         "sub_choice": false,
         "customer_id": "1",
         "custom_properties": {
           "price_plan": "platinum"
         },
         "referred_by": null,
         "referral_counts": {
           "total": 3,
           "approved": 2,
           "pending": 1,
         },
         "reward_counts": {
           "total": 3
           "unpaid": 1,
           "paid": 2,
         },
         "share_counts": {
           "total": 3
           "facebook": 1,
           "other": 2,
         }
       }
     }
   }

Get Friends referred by Advocate
......................

.. code-block:: text

   GET https://www.talkable.com/api/v2/people/customer@example.com/referrals_as_advocate?site_slug=my-store

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "referrals": [
        {
          "ad_rewarded": true,
          "advocate_person": {
            "id": 39198,
            "email": "customer@example.com",
            "first_name": null,
            "last_name": null
          },
          "campaign_id": 145,
          "created_at": "2021-03-02T09:24:55.000-08:00",
          "friend_person": {
            "id": 39202,
            "email": "friend@example.com",
            "first_name": null,
            "last_name": null
          },
          "id": 4,
          "offer_id": 71,
          "qa_generated": false,
          "referred_origin_id": 40085,
          "referred_subtotal": 100,
          "status": "pending",
          "track_method": "coupon",
          "updated_at": "2021-03-02T09:24:55.000-08:00",
        },
        {
          "ad_rewarded": true,
          "advocate_person": {
            "id": 39198,
            "email": "customer@example.com",
            "first_name": null,
            "last_name": null
          },
          "campaign_id": 145,
          "created_at": "2021-03-02T09:16:15.000-08:00",
          "friend_person": {
            "id": 39200,
            "email": "john@example.com",
            "first_name": "John",
            "last_name": null
          },
          "id": 2,
          "offer_id": 71,
          "qa_generated": false,
          "referred_origin_id": 40083,
          "referred_subtotal": 100,
          "status": "approved",
          "track_method": "cookie",
          "updated_at": "2021-03-02T09:16:16.000-08:00",
        }
      ]
    }
  }

Get rewards received by person
......................

.. code-block:: text

   GET https://www.talkable.com/api/v2/people/customer@example.com/rewards?site_slug=my-store

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "rewards": [
        {
          "amount": 5,
          "id": 11,
          "reason": "referrer",
          "status": "Unpaid",
          "coupon": null,
          "coupon_code": null,
          "incentive_type": "discount_coupon",
          "incentive_description": "shared coupon \"AD_5_OFF\" for $5 off",
          "incentive_custom_description": null
        },
        {
          "amount": 5,
          "id": 10,
          "reason": "referrer",
          "status": "Paid",
          "coupon": {
            "description": "$5",
            "amount": 5,
            "code": "AD_5_OFF",
            "expires_at": null,
            "id": 2,
            "percentage_discount": null,
            "single_use": false,
            "used": false,
            "active": true,
            "usages": null,
            "valid_until": null
          },
          "coupon_code": "AD_5_OFF",
          "incentive_type": "discount_coupon",
          "incentive_description": "shared coupon \"AD_5_OFF\" for $5 off",
          "incentive_custom_description": null
        },
      ]
    }
  }


Get shares made by person
......................

.. code-block:: text

   GET https://www.talkable.com/api/v2/people/customer@example.com/shares_by?site_slug=my-store

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "shares": [
        {
          "short_url": "https://www.talkable.com/x/8t9d2p",
          "channel_identifier": "facebook",
          "id": 11,
          "type": "SocialOfferShare",
          "offer": {
            "claim_url": "https://www.talkable.com/x/14PMvl",
            "email": "test-offer@gmail.com",
            "id": 71,
            "short_url_code": "0EiKB3",
            "show_url": "https://www.talkable.com/x/ArhsqM",
            "coupon_code": null,
            "incentives": {
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
            },
            "trigger_widget": false,
            "campaign_tags": ["test-invite"]
          },
          "campaign": {
            "slug": 145,
            "is_active": true,
            "appearance": "inline",
            "id": 145,
            "joinable_category_names": ["affiliate_member"],
            "name": "Standalone landing page",
            "new_customer": null,
            "origin_max_age": null,
            "origin_min_age": null,
            "status": "Test",
            "tag_names": ["test-invite"],
            "type": "Standalone Campaign"
          },
          "friends_count": 0,
          "friend_clicks_count": 0
        },
        {
          "short_url": "https://www.talkable.com/x/14PMvl",
          "channel_identifier": "other",
          "id": 10,
          "type": "SocialOfferShare",
          "offer": {
            "claim_url": "https://www.talkable.com/x/14PMvl",
            "email": "test-offer@gmail.com",
            "id": 71,
            "short_url_code": "0EiKB3",
            "show_url": "https://www.talkable.com/x/ArhsqM",
            "coupon_code": null,
            "incentives": {
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
            },
            "trigger_widget": false,
            "campaign_tags": ["test-invite"]
          },
          "campaign": {
            "slug": 145,
            "is_active": true,
            "appearance": "inline",
            "id": 145,
            "joinable_category_names": ["affiliate_member"],
            "name": "Standalone landing page",
            "new_customer": null,
            "origin_max_age": null,
            "origin_min_age": null,
            "status": "Test",
            "tag_names": ["test-invite"],
            "type": "Standalone Campaign"
          },
          "friends_count": 4,
          "friend_clicks_count": 1
        }
      ]
    }
  }

Update person’s username
........................

.. code-block:: javascript

   {
     "site_slug": "my-store",
     "data": {
       "username": "lizard_king"
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X PUT \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","data":{"username":"lizard_king"}}' \
        https://www.talkable.com/api/v2/people/customer@example.com

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "https://share.mystore.com/by/lizard_king",
         "events_count": 0,
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": "lizard_king",
         "subscribed_at": null,
         "unsubscribed_at": null,
         "sub_choice": false,
         "customer_id": "1",
         "custom_properties": {
           "price_plan": "platinum"
         },
         "referred_by": null,
         "referral_counts": {
           "total": 3,
           "approved": 2,
           "pending": 1,
         },
         "reward_counts": {
           "total": 3
           "unpaid": 1,
           "paid": 2,
         },
         "share_counts": {
           "total": 3
           "facebook": 1,
           "other": 2,
         }
       }
     }
   }

Unsubscribe a person from receiving emails
..........................................

.. code-block:: javascript

   {
     "site_slug": "my-store"
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store"}' \
        https://www.talkable.com/api/v2/people/customer@example.com/unsubscribe

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "https://share.mystore.com/by/customer@example.com",
         "events_count": 0,
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": null,
         "subscribed_at": null,
         "unsubscribed_at": "2014-11-18T05:49:54.000-07:00",
         "sub_choice": false,
         "customer_id": "1",
         "custom_properties": {
           "price_plan": "platinum"
         },
         "referred_by": null,
         "referral_counts": {
           "total": 3,
           "approved": 2,
           "pending": 1,
         },
         "reward_counts": {
           "total": 3
           "unpaid": 1,
           "paid": 2,
         },
         "share_counts": {
           "total": 3
           "facebook": 1,
           "other": 2,
         }
       }
     }
   }

Anonymize a person
..................

.. code-block:: javascript

   {
     "site_slug": "my-store"
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store"}' \
        https://www.talkable.com/api/v2/people/customer@example.com/anonymize

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": null,
         "events_count": 0,
         "first_name": null,
         "last_name": null,
         "email": "b19b4a80-3bb2-48f2-831a-6e180b4c6a7e@anonymized.email",
         "username": null,
         "subscribed_at": null,
         "unsubscribed_at": null,
         "sub_choice": false,
         "customer_id": null,
         "custom_properties": {
           "price_plan": "platinum"
         },
         "referred_by": null,
         "referral_counts": {
           "total": 3,
           "approved": 2,
           "pending": 1,
         },
         "reward_counts": {
           "total": 3
           "unpaid": 1,
           "paid": 2,
         },
         "share_counts": {
           "total": 3
           "facebook": 1,
           "other": 2,
         }
       }
     }
   }

Get personal information about a person
.......................................

.. code-block:: text

   GET https://www.talkable.com/api/v2/people/customer@example.com/personal_data?site_slug=my-store

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "created_at": "2018-04-30T02:14:35.000-07:00",
         "customer_id": null,
         "email": "customer@example.com",
         "first_name": null,
         "last_name": null,
         "opted_in_at": null,
         "unsubscribed_at": null,
         "username": null,
         "origins": [
           {
             "type": "AffiliateMember",
             "created_at": "2018-04-30T02:14:35.000-07:00",
             "ip_address": "1.2.3.4",
             "order_number": "customer@example.com",
             "subtotal": 0.0
           }
         ]
       }
     }
   }

.. container:: hidden

   .. toctree::
