.. _web_hooks/unsubscribe:
.. include:: /partials/common.rst

Unsubscribe Web Hook
====================

Triggered when a person unsubscribes.

.. raw:: html

   <h2>Payload parameters provided </h2>

* **person** — subhash of parameters describing the person

  * **first_name** — friend's first name
  * **last_name** — friend's last name
  * **email** — friend’s email address
  * **username** — friend’s username
  * **unsubscribed_at** — date friend has unsubscribed
  * **opted_in_at** — date friend has subscribed
  * **sub_choice** — subscription choice
  * **custom_properties** — hash of friend’s custom properties (optional)

.. raw:: html

   <h2>Sample payload</h2>

.. code-block:: javascript

   {
     "person": {
       "first_name": "Bob",
       "last_name": "Smith",
       "email": "friend@example.com",
       "username": "username",
       "unsubscribed_at": "2015-08-13T11:14:08.835-07:00",
       "opted_in_at": "2014-08-13T11:14:08.835-07:00",
       "sub_choice": true
     }
   }

.. raw:: html

   <h2>cURL example</h2>

.. code-block:: bash

   curl --data 'key=<key>&payload={"person":{"first_name":"Bob","last_name":"Smith","email":"friend@example.com","username":"username","unsubscribed_at":"2015-08-13T11:14:08.835-07:00","opted_in_at":"2014-08-13T11:14:08.835-07:00","sub_choice":true}}' <url>

.. container:: hidden

   .. toctree::
