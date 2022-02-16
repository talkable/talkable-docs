.. _api_v2/intro:
.. include:: /partials/common.rst

.. meta::
   :description: The Talkable API is built on HTTP. Our API is RESTful, returns JSON, and responds with standard HTTP response codes to indicate errors.

Introduction
============

The Talkable API is built on HTTP. Our API is RESTful, returns JSON and responds
with standard HTTP response codes to indicate errors.

Access the Talkable API
-----------------------

You can access documentation for the Talkable API and issue API calls from the Talkable API user interface.

The Talkable API user interface is available here:

https://www.talkable.com/api-docs/

Click **Authorize** to log in with the `API key <Authentication_>`_:

.. image:: /_static/img/swagger/authorize1.png
   :alt: Authorize step 1
   :class: is-minimal

Enter the `API key <Authentication_>`_ and click **Authorize** again:

.. image:: /_static/img/swagger/authorize2.png
   :alt: Authorize step 2
   :class: is-minimal

Click **Close**. The Authorize lock icon changes to locked:

.. image:: /_static/img/swagger/authorize3.png
   :alt: Authorize step 3
   :class: is-minimal
   :width: 156 px

.. raw:: html

   <h4>Actions</h4>

For details about the API call, expand the API method for each call. To issue an
API call from the Talkable API user interface, click **Try it out** for any
method. Edit the Example Values in the request body and click **Execute**.

.. image:: /_static/img/swagger/actions.png
   :alt: Actions
   :class: is-minimal

Authentication
--------------

You authenticate to the Talkable API by providing your API Key in the request.
You can manage your API key in the Account Settings.

.. warning:: Keep your API key secret!

   You should not embed the API key within a web page and make Talkable API calls
   within JavaScript running within a browser. Once someone has your API key, they
   could create their own API calls.

Authentication to the API is performed via Bearer authentication header.

.. raw:: html

   <h4>Example Request</h4>

.. code-block:: bash

   curl 'https://www.talkable.com/api/v2/campaigns?site_slug=my-store' \
     -H 'accept: application/json' \
     -H 'Authorization: Bearer i9uil7nQgDjucCiTJu'

Response Format
---------------

The API returns JSON-encoded objects (content-type: application/json).

Responses vary according to the method used, but every successful response
envelope includes these common parts:

.. code-block:: javascript

   {"ok": true, "result": ...}

Date Format
-----------

Talkable returns JSON for all API calls. JSON does not have a built-in date type,
dates are passed as strings encoded according to |iso8601|.
This format is supported by most programming languages out of the box:

.. code-block:: text

   2022-02-16T02:43:58.797-07:00

Errors
------

The following represents a common JSON error response resulting from a failed
Talkable API call:

.. code-block:: javascript

   {"ok": false, "error_message": "Message describing the error"}

Most error messages that Talkable API will return are not meant to be shown to
the user. We expect your service to gracefully handle errors and only show
meaningful information to the user.

Talkable returns standard HTTP response codes.

.. container:: ptable

   =================== ======================================================
   Code                Description
   =================== ======================================================
   200, 201            Everything worked as expected
   400                 Bad Request - Often missing a required parameter
   401                 Unauthorized - No valid API key provided
   404                 Not Found - The requested item doesn’t exist
   422                 Unprocessable Entity - The requested create, update,
                       or delete cannot be performed due to validation errors.
                       |br| See the response body for more details.
   500, 502, 503, 504  Server Errors - Something is wrong on Talkable’s end
   =================== ======================================================

.. _HTTP Basic Auth: https://en.wikipedia.org/wiki/Basic_access_authentication
