.. _api_v2/visitors:
.. include:: /partials/common.rst

Visitors
========

This API allows you to create visitors. See examples below.

|br|

.. code-block:: text

   POST /visitors

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   data              Hash or JSON object with following properties:

                     * uuid - UUID of new visitor that will be created
   ================= ========================================================

Example
-------

Create a visitor
................

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X POST \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","data":{"uuid":"b3967d36-4e7f-46bc-92b3-57344347cd6a"}}' \
        https://www.talkable.com/api/v2/visitors

Sample response:

.. code-block:: javascript

   {
     "result": {
       "uuid": "b3967d36-4e7f-46bc-92b3-57344347cd6a"
     }
   }
