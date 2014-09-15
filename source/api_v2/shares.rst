.. _api_v2/shares:
.. include:: /partials/common.rst

Shares
======

This API allows you to access offer shares.

|br|

.. code-block:: url

   POST /offers/<short_url_code>/shares

Creates offer share.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   short_url_code    Offer short code obtained with
                     :ref:`origin creation <api_v2/origins>`.
   ================= ========================================================

For `social share`:

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   channel           Options: `facebook`, `twitter`, `linkedin`, `other`
   ================= ========================================================

Or for `email share`:

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   channel           `email`
   recipients        List of recipient emails separated by comma or newline.
   email             Hash or JSON object with following properties:

                     * subject (optional)
                     * body (optional)
                     * reminder (optional, `true`/`false`, `true` by default)
   ================= ========================================================

Example
-------

Create a Facebook share
.......................

.. code-block:: url

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","channel":"facebook"}' \
        https://www.talkable.com/api/v2/offers/dZpBwd/shares

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

.. code-block:: url

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","channel":"email","recipients":"friend1@example.com,friend2@example.com","email":{"subject":"Hello!"}}' \
        https://www.talkable.com/api/v2/offers/dZpBwd/shares

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "reward": {
        "reason": "email_shared",
        "incentive_type": "discount_coupon",
        "incentive_description": "shared coupon \"10_OFF\" for $10.00 off",
        "amount": null,
        "coupon_code": "10_OFF"
      },
      "shares": [
        {
          "id": 4452107,
          "email": "friend1@example.com",
          "type": "EmailOfferShare",
          "short_url": "https://www.talkable.com/x/lDtvhD"
        },
        {
          "id": 4452108,
          "email": "friend2@example.com",
          "type": "EmailOfferShare",
          "short_url": "https://www.talkable.com/x/VsaTEe"
        }
      ]
    }
  }
