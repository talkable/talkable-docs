.. _api_v2/traffic_sources:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to access traffic sources.

Traffic sources
===============

This API allows you to access traffic sources. Traffic source can be used to filter metrics.

|br|

.. code-block:: text

   GET /traffic_sources

Returns all traffic sources

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   ================= ========================================================

Example
-------

Offers metric
.............

.. code-block:: text

   GET https://www.talkable.com/api/v2/traffic_sources?site_slug=my-store

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": [
       { "identifier": "talkable-gem" },
       { "identifier": "post-event" }
     ]
   }
