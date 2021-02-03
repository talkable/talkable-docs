.. _api_v2/campaigns:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to access campaigns.

Campaigns
=========

This API allows you to access campaigns.

|br|

.. code-block:: text

   GET /campaigns

Returns campaigns.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   ================= ========================================================

Example
-------

.. code-block:: text

   GET https://www.talkable.com/api/v2/campaigns?site_slug=my-store

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "campaigns": [
         {
           "appearance": "inline",
           "id": 35944,
           "name": "API campaign",
           "new_customer": null,
           "origin_max_age": null,
           "origin_min_age": null,
           "tag_names": ["api"],
           "slug": 35944,
           "type": "Standalone Campaign",
           "is_active": true,
           "status": "Live"
         },
         {
           "appearance": "popup",
           "id": 34601,
           "name": "PP campaign",
           "new_customer": null,
           "origin_max_age": null,
           "origin_min_age": null,
           "tag_names": ["default"],
           "slug": 34601,
           "type": "Post-Checkout Campaign",
           "is_active": true,
           "status": "Live"
         },
         {
           "appearance": "inline",
           "id": 34376,
           "name": "Inactive campaign",
           "new_customer": null,
           "origin_max_age": null,
           "origin_min_age": null,
           "tag_names": ["default"],
           "slug": 34376,
           "type": "Standalone Campaign",
           "is_active": false,
           "status": "Disabled"
         }
       ]
     }
   }
