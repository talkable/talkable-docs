.. _api_v2/rewards:
.. include:: /partials/common.rst

Rewards
=======

This API allows you to access visitor rewards.

|br|

.. code-block:: text

   GET /rewards

Returns rewards.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   visitor_uuid      Visitor uuid
   status (optional) Filter rewards by status.
                     By default API returns only `Paid` rewards.

                     Options: `Paid`, `Unpaid`, `Voided`, `All`

   ================= ========================================================

Example
-------

.. code-block:: text

   GET https://www.talkable.com/api/v2/rewards?site_slug=my-store&visitor_uuid=8a55ef82-82c1-4596-babb-e989fd717965

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "rewards": [
         {
           "id": 22017,
           "reason": "shared",
           "incentive_type": "discount_coupon",
           "incentive_description": "shared coupon \"10_OFF\" for $10.00 off",
           "amount": 10.0,
           "coupon_code": "10_OFF",
           "status": "Paid"
         },
         {
           "id": 22018,
           "reason": "referrer",
           "incentive_type": "rebate",
           "incentive_description": "$10.00 back",
           "amount": 10.0,
           "coupon_code": null,
           "status": "Paid"
         }
       ]
     }
   }
