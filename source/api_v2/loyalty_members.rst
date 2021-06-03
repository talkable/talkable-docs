.. _api_v2/loyalty_members:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to find loyalty members and adjust their points balance.

Loyalty members
===============

This API allows you to find loyalty members and adjust their points balance.
See examples below.

|br|

.. code-block:: text

   GET /loyalty/members/<email>

Returns a loyalty member.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   email             Loyalty member’s email
   ================= ========================================================

|br|

.. code-block:: text

   POST /loyalty/members/<email>/manual_adjustment_actions

Adjusts loyalty member’s points balance.

.. container:: ptable

   ================= ===============================================================================
   Parameter         Description
   ================= ===============================================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   email             Loyalty member’s email
   data              JSON object with ``points`` property and optional ``description``.

                     E.g. ``{"points": 100}`` or ``{"points": -100, "description": "For cheating"}``
   ================= ===============================================================================

Example
-------

Find a loyalty member by email
..............................

.. code-block:: text

   GET https://www.talkable.com/api/v2/loyalty/members/customer@example.com?site_slug=my-store

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "loyalty_member": {
         "email": "customer@example.com",
         "points_balance": 1000
       }
     }
   }

Adjust loyalty member’s points balance
......................................

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","data":{"points":100,"description":"For being a loyal customer"}}' \
        https://www.talkable.com/api/v2/loyalty/members/customer@example.com/manual_adjustment_actions

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "loyalty_member": {
         "email": "customer@example.com",
         "points_balance": 1100
       }
     }
   }

.. container:: hidden

   .. toctree::
