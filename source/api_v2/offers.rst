.. _api_v2/offers:
.. include:: /partials/common.rst

Advocate Offers
===============

This API allows you to access advocate offers.

|br|

.. code-block:: url

   GET /offers/<short_url_code>

Returns advocate offer.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   short_url_code    Advocate offer short code obtained with
                     :ref:`origin creation <api_v2/origins>`.
   interpolations    Optional: array of interpolations to return in response
   ================= ========================================================

Example
-------

.. code-block:: url

   GET https://www.talkable.com/api/v2/offers/dZpBwd?site_slug=my-store&api_key=i9uil7nQgDjucCiTJu

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "offer": {
         "short_url_code": "dZpBwd",
         "email": "customer@example.com",
         "show_url": "https://www.talkable.com/x/iEov9g",
         "claim_url": "https://www.talkable.com/x/5B3xO1"
       }
     }
   }
