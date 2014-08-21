.. _api_v2/origins:
.. include:: /partials/common.rst

Origins
=======

This API allows you to create origins. See examples below.

|br|

.. code-block:: url

   POST /origins

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   type              Type of origin to create (*"Purchase"* or *"AffiliateMember"*)
   data              JSON object with following properties:

                     For Purchase:

                     * email
                     * subtotal
                     * order_number
                     * order_date (|iso8601| formatted datetime)
                     * items (optional)
                     * customer_id (optional)
                     * coupon_code (optional)

                     For AffiliateMember:

                     * email

   ================= ========================================================

Example
-------

Create a purchase
.................

.. code-block:: javascript

   {
     "api_key": "i9uil7nQgDjucCiTJu",
     "site_slug": "my-store",
     "type": "Purchase",
     "data": {
       "email": "customer@mail.com",
       "order_number": 12,
       "order_date": "2014-03-14T05:49:54-07:00",
       "subtotal": 100,
       "items": [
         {
           "price": 25,
           "quantity": 4,
           "product_id": "TSHIRT"
         }
       ]
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","type":"Purchase","data":{"email":"customer@mail.com","order_number":12,"order_date":"2014-03-14T05:49:54-07:00","subtotal":100,"items":[{"price":25,"quantity":4,"product_id":"TSHIRT"}]}}' \
        https://www.talkable.com/api/v2/origins

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "origin": {
         "id": 31386398,
         "order_number": 12,
         "subtotal": 100.0,
         "order_date": "2014-03-14T05:49:54.000-07:00",
         "customer_id": null,
         "type": "Purchase",
         "coupon_code": ""
       },
       "offer": {
         "short_url_code": "dZpBwd",
         "email": "customer@mail.com",
         "show_url": "http://curebit.com/x/iXh4Je",
         "claim_url": "http://curebit.com/x/LSKEAX"
       }
     }
   }

Create an affiliate member
..........................

.. code-block:: javascript

   {
     "api_key": "i9uil7nQgDjucCiTJu",
     "site_slug": "my-store",
     "type": "AffiliateMember",
     "data": {
       "email": "affiliate@mail.com"
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","type":"AffiliateMember","data":{"email":"affiliate@mail.com"}}' \
        https://www.talkable.com/api/v2/origins

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "origin": {
         "id": 31386400,
         "email": "affiliate@mail.com",
         "customer_id": null,
         "type": "AffiliateMember"
       },
       "offer": {
         "short_url_code": "Jp8qY9",
         "email": "affiliate@mail.com",
         "show_url": "http://curebit.com/x/5BN5h7",
         "claim_url": "http://curebit.com/x/TM2OhR"
       }
     }
   }

.. container:: hidden

   .. toctree::
