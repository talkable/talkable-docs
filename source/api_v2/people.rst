.. _api_v2/people:
.. include:: /partials/common.rst

People
======

This API allows you to access and update persons. See examples below.

|br|

.. code-block:: text

   GET /people/<person_slug>

Returns a person.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email or username
   ================= ========================================================

|br|

.. code-block:: text

   PUT /people/<person_slug>

Updates an existing person or creates one if it does not exist.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email
   data              JSON object with one or more of following properties:

                     * first_name
                     * last_name
                     * username
                     * customer_id
                     * person_custom_properties

   ================= ========================================================

|br|

.. code-block:: text

   POST /people/<person_slug>/unsubscribe

Unsubscribes a person from receiving emails.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email
   ================= ========================================================

Example
-------

Find a person by email
......................

.. code-block:: text

   GET https://www.talkable.com/api/v2/people/customer@example.com?site_slug=my-store&api_key=i9uil7nQgDjucCiTJu

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "http://share.mystore.com/by/customer@example.com",
         "events_count": 0,
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": null,
         "gender": null,
         "subscribed_at": null,
         "unsubscribed_at": null,
         "sub_choice": false
       }
     }
   }

Update person’s username
........................

.. code-block:: javascript

   {
     "api_key": "i9uil7nQgDjucCiTJu",
     "site_slug": "my-store",
     "data": {
       "username": "lizard_king"
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X PUT \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","data":{"username":"lizard_king"}}' \
        https://www.talkable.com/api/v2/people/customer@example.com

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "http://share.mystore.com/by/lizard_king",
         "events_count": 0,
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": "lizard_king",
         "gender": null,
         "subscribed_at": null,
         "unsubscribed_at": null,
         "sub_choice": false
       }
     }
   }

Unsubscribe a person from receiving emails
..........................................

.. code-block:: javascript

   {
     "api_key": "i9uil7nQgDjucCiTJu",
     "site_slug": "my-store"
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store"}' \
        https://www.talkable.com/api/v2/people/customer@example.com/unsubscribe

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "http://share.mystore.com/by/customer@example.com",
         "events_count": 0,
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": null,
         "gender": null,
         "subscribed_at": null,
         "unsubscribed_at": "2014-11-18T05:49:54.000-07:00",
         "sub_choice": false
       }
     }
   }

.. container:: hidden

   .. toctree::
