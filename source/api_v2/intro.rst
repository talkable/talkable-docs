.. _api_v2/intro:
.. include:: /partials/common.rst

Introduction
============

The Talkable API is built on HTTP. Our API is RESTful, returns JSON and responds
with standard HTTP response codes to indicate errors.

Base URL
--------

All API URLs referenced in this documentation start with the following base part:

.. code-block:: url

   https://www.talkable.com/api/v2

Authentication
--------------

You authenticate to the Talkable API by providing your ``api_key`` in the request.
You can manage your API key in the Account Settings.

.. warning:: Keep your API key secret!

Response Format
---------------

The API returns JSON-encoded objects (content-type: application/json).

.. Responses vary according to the method used, but every successful response
   envelope (except for very simple ones, which are just ``{"ok": true}``) includes
   these common parts:

Responses vary according to the method used, but every successful response
envelope includes these common parts:

.. code-block:: javascript

   {"ok": true, "result": ...}

Date Format
-----------

Talkable returns JSON for all API calls. JSON does not have a built-in date type,
dates are passed as strings encoded according to |iso8601|.
This format is supported by most programming languages out of the box:

.. code::

   2014-04-02T02:43:58.797-07:00

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

.. container:: hidden

   .. toctree::
