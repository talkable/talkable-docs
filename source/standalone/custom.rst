.. _standalone/custom:
.. include:: /partials/common.rst

Custom Integration
==================

Sign Up
-------

Capture the email and make ajax request to Curebit with entered email, campaign
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
