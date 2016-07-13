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
   sharing_channels  Optional: array of social sharing channels for which will be
                     generated sharing links.

                     Options: `facebook`, `twitter`, `linkedin`, `sms`,
                     `other` or custom, except `email`, `reminder`,
                     `facebook_sponsored` and `coupon`.
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

With sharing links
..................

.. code-block:: url

   GET https://www.talkable.com/api/v2/offers/dZpBwd?site_slug=my-store&api_key=i9uil7nQgDjucCiTJu&sharing_channels=facebook,twitter,custom

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
       },
       "claim_links": {
         "facebook": "https://www.talkable.com/x/8L6xO2",
         "twitter": "https://www.talkable.com/x/KB89fO",
         "custom": "https://www.talkable.com/x/Yf794w"
       }
     }
   }
