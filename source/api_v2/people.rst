.. _api_v2/people:
.. include:: /partials/common.rst

People
======

This API allows you to access and update persons. See examples below.

.. code-block:: url

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

.. code-block:: url

   PUT /people/<person_slug>

Updates existing person.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   person_slug       Person’s email or username
   data              JSON object with one or more of following properties:

                     * first_name
                     * last_name
                     * username
                     * customer_id

   ================= ========================================================

Example
-------

Find a person by email
......................

.. code-block:: url

   GET https://www.talkable.com/api/v2/people/customer@email.com?site_slug=my-store&api_key=i9uil7nQgDjucCiTJu

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "http://share.mystore.com/by/customer@example.com",
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": null,
         "gender": "male",
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
     "person_slug": "customer@email.com",
     "data": {
       "username": "lizard_king"
     }
   }

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X PUT \
        -d '{"api_key":"i9uil7nQgDjucCiTJu","site_slug":"my-store","person_slug":"customer@email.com","data":{"username":"lizard_king"}}' \
        https://www.talkable.com/api/v2/people

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "person": {
         "personal_claim_url": "http://share.mystore.com/by/lizard_king",
         "first_name": "John",
         "last_name": "Smith",
         "email": "customer@example.com",
         "username": "lizard_king",
         "gender": "male",
         "subscribed_at": null,
         "unsubscribed_at": null,
         "sub_choice": false
       }
     }
   }

.. container:: hidden

   .. toctree::
