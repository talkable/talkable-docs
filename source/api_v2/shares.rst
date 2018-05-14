.. _api_v2/shares:
.. include:: /partials/common.rst

Shares
======

This API allows you to access offer shares.

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
                     `other`
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

   subject           (optional) Custom subject of the e-mail
   body              (optional) Custom message added to the e-mail body
   reminder          (optional, `true`/`false`, `true` by default)
                     Whether Talkable should send a reminder e-mail later
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
       "reward": null,
       "share": {
         "id": 4452084,
         "type": "SocialOfferShare",
         "short_url": "https://www.talkable.com/x/hQ0SZb"
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

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "reward": null,
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
      }
    }
  }
