.. _api_v2/shares:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to create offer shares.

Shares
======

This API allows you to create offer shares.

|br|

.. code-block:: text

   POST /offers/<short_url_code>/shares/social

Creates a social share.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   short_url_code    Offer short code obtained with
                     :ref:`origin creation <api_v2/origins>`.
   channel           Options: `facebook`, `twitter`, `linkedin`, `whatsapp`,
                     `sms`, `other`
   ================= ========================================================

|br|

.. code-block:: text

   POST /offers/<short_url_code>/shares/email

Creates an email share.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   short_url_code    Offer short code obtained with
                     :ref:`origin creation <api_v2/origins>`.
   recipients        List of recipient emails separated by comma or newline.

   subject           (optional) Custom subject of the email
   body              (optional) Custom message added to the email body
   reminder          (optional, `true`/`false`, `true` by default)
                     Whether Talkable should send a reminder email later
   ================= ========================================================

Example
-------

Create a Facebook share
.......................

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","channel":"facebook"}' \
        https://www.talkable.com/api/v2/offers/dZpBwd/shares/social

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "share": {
        "short_url": "https://www.talkable.com/x/hQ0SZb",
        "channel_identifier": "facebook",
        "id": 10,
        "type": "SocialOfferShare",
        "offer": {
          "claim_url": "http://www.talkable.com/x/14PMvl",
          "email": "test-offer@gmail.com",
          "id": 71,
          "short_url_code": "0EiKB3",
          "show_url": "http://www.talkable.com/x/ArhsqM",
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
          "tag_names": ["test-invite"]
        },
        "friends_count": 4,
        "friend_clicks_count": 1,
      },
      "reward": {
        "id": 24,
        "reason": "shared",
        "incentive_type": "discount_coupon",
        "incentive_description": "shared coupon \"C1383-8321\" for $10 off",
        "incentive_custom_description": null,
        "amount": 10.0,
        "coupon": {
          "id": 951,
          "code": "C1383-8321",
          "active": true,
          "valid_until": null,
          "single_use": true,
          "used": false,
          "usages": 0,
          "amount": 10.0,
          "percentage_discount": false,
          "description": "$10",
          "expires_at": null
        },
        "coupon_code": "C1383-8321",
        "status": "Paid"
      }
    }
  }

Create an Email share
.....................

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","recipients":"friend1@example.com,friend2@example.com","subject":"Hello!","body":"World!","reminder":false}' \
        https://www.talkable.com/api/v2/offers/dZpBwd/shares/email

.. _email-sharing-response:

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "success": true,
      "validation_only": false,
      "stats": {
        "currently_sent": 2,
        "currently_not_sent": 0,
        "previously_sent": 0,
        "total_sent": 2,
        "sent_limit_exceeded": false,
        "left_emails": 20
      },
      "recipients": {
        "friend1@example.com": {
          "currently_sent": true,
          "previously_sent": false,
          "email_valid": true,
          "self_referral": false,
          "unsubscribed": false,
          "blacklisted": false,
          "meets_criteria": true,
          "sharable": true
        },
        "friend2@example.com": {
          "currently_sent": true,
          "previously_sent": false,
          "email_valid": true,
          "self_referral": false,
          "unsubscribed": false,
          "blacklisted": false,
          "meets_criteria": true,
          "sharable": true
        }
      },
      "reward": null
    }
  }
