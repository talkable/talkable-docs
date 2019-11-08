.. _advanced_features/url_parameters:
.. include:: /partials/common.rst

.. meta::
   :description: Talkable allows overriding some of the parameters right through URL query string.

Using URL Parameters
====================

Talkable allows overriding some of the parameters right through URL query string:

* email - |advocate| email address
* first_name - |advocate| first name
* last_name - |advocate| last name
* traffic_source - :ref:`Traffic Source <advanced_features/traffic_source>` value
* campaign_tags - overrides campaign tag to be loaded

Below is an example of |advocate| authorization through URL. Given the URL of
the page where Talkable campaign is integrated: http://example.com/share:

.. code-block:: html

   http://example.com/share?email=advocate%40example.com

Location parameters have higher priority than explicit parameters passed in the
integration.

.. note::

   Don’t forget to escape URL parameters with URI parameter encoder.

.. container:: hidden

  .. toctree::
