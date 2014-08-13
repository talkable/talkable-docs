.. _standalone/standard:
.. include:: /partials/common.rst

Standard Integration
====================

.. include:: /partials/note_enterprise_integration.rst

.. include:: /partials/integration_head.rst

Standalone campaign can be integrated to the page with the following code:

.. include:: /samples/standalone/standard.rst

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
`Example integration <http://docs.talkable.com/samples/viewport-sa.html>`_.

`Source integration <https://github.com/curebit/docs/blob/gh-pages/samples/viewport-sa.html>`_.

.. include:: /partials/for_modern_sa_js_apps.rst

.. container:: hidden

   .. toctree::
