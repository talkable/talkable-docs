.. _standalone:
.. include:: /partials/common.rst

Standalone Integrations
#######################

.. include:: /partials/note_enterprise_integration.rst

.. include:: /partials/integration_head.rst

Basic Integration
=================

Standalone campaign can be integrated to the page with the following code:

.. include:: /samples/standalone/standard.rst

.. include:: /partials/passing_custom_data.rst

.. raw:: html

   <h2>Using Current Location URL Parameters</h2>

You are able to pass some parameters to Talkable directly from current URL.

In this case Talkable integration code will automatically catch some of the
current location parameters and pass them to Talkable:

* email - will be passed as affiliate email
* first_name - will be passed as affiliate first_name
* last_name - will be passed as affiliate last_name
* customer_id - will be passed as customer_id
* campaign_tags - will be passed as campaign tags

.. note::

   Location parameters have higher priority than explicit parameters passed in
   the integration code above.

.. note::

   Don't forget to escape them with URI parameter encoder.

.. raw:: html

   <h3>Example</h3>

Suppose that you have Talkable integration code on "**http://your-merchant.com/share**".
The following code will register person@example.com in campaign with tag "custom":

.. code-block:: url

   http://your-merchant.com/share?email=person@example.com&campaign_tags=custom

.. include:: /partials/optimizing_for_viewport.rst

`Example integration <http://jsbin.com/jipoqotaheri/1>`_.

`Source integration <http://jsbin.com/jipoqotaheri/1/edit?html,output>`_.

.. include:: /partials/for_modern_sa_js_apps.rst

|hr|

Custom Integration
==================

Sign Up
-------

Capture the email and make ajax request to Talkable with entered email, campaign
tags and possible any other data like first/last name or gender. We return back
a json containing offer short code. Then redirect user to share page.

.. include:: /partials/note_sample_code.rst

.. include:: /samples/standalone/custom/sign_up.rst

.. raw:: html

   <h3>Sample response</h3>

.. code-block:: javascript

   {
     "success": true,
     "offer_code": "pLs495",
     "offer_link": "http://curebit.com/o/pLs495/show",
     "facebook_offer_link": "http://curebit.com/x/PiqkTF"
   }

.. raw:: html

   <h3>Sample errors</h3>

.. code-block:: javascript

   {
     "success": false,
     "errors": ["Email can't be blank"]
   }

.. include:: /partials/passing_custom_data.rst

|hr|

Get a Coupon Code
-----------------

Use offer short code to get a Coupon Code after share.

.. include:: /samples/standalone/custom/coupon.rst

.. raw:: html

   <h3>Sample response</h3>

.. code-block:: javascript

   {
     "success": true,
     "coupon_code": "CODE-123"
   }

.. raw:: html

   <h3>Sample errors</h3>

.. code-block:: javascript

   {
     "success": false,
     "errors": ["event_sharing_channel is not specified"]
   }

.. container:: hidden

  .. toctree::

