.. _standalone/standard:
.. include:: /partials/common.rst

Standard Integration
====================

In order for a customer to join a Standalone campaign, Curebit will need to know
the user's email. There are two ways of doing this.

.. raw:: html

   <h2>Provide the Curebit User's Email Directly</h2>

In the case that you already have the current user's email (e.g. if your site
requires the user to create an account and log in to purchase) you can provide
it to Curebit with some additional info.

.. raw:: html

   <h2>Let Curebit Ask for Email</h2>

In the case that the user is not yet registered on the merchant's site, and
the merchant does not yet know the user's email. The Affiliate signup page
will be displayed.

.. include:: /samples/standalone/standard.rst

.. raw:: html

   <h2>Using Current Location URL Parameters</h2>

You are able to pass some parameters to Curebit directly from current URL.

In this case Curebit integration code will automatically catch some of the
current location parameters and pass them to Curebit:

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

Suppose that you have Curebit integration code on "**http://your-merchant.com/share**".
The following code will register person@example.com in campaign with tag "custom":

.. code-block:: url

   http://your-merchant.com/share?email=person@example.com&campaign_tags=custom

.. include:: /partials/optimizing_for_viewport.rst

.. toctree::
