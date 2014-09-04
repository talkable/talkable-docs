.. _api_v2/campaigns:
.. include:: /partials/common.rst

Campaigns
=========

This API allows you to access campaigns.

|br|

.. code-block:: url

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

.. code-block:: url

   GET https://www.talkable.com/api/v2/campaigns?site_slug=my-store&api_key=i9uil7nQgDjucCiTJu

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "campaigns": [
        {
          "id": 35944,
          "name": "API campaign",
          "cached_slug": "35944-api-campaign",
          "tag_names": [
            "api"
          ],
          "type": "Standalone Campaign",
          "is_active": true
        },
        {
          "id": 34601,
          "name": "PP campaign",
          "cached_slug": "34601-pp-campaign",
          "tag_names": [
            "default"
          ],
          "type": "Post-Checkout Campaign",
          "is_active": true
        },
        {
          "id": 34376,
          "name": "Inactive campaign",
          "cached_slug": "34376-inactive-campaign",
          "tag_names": [
            "default"
          ],
          "type": "Standalone Campaign",
          "is_active": false
        }
      ]
    }
  }
