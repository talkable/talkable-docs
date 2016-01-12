.. _ecommerce/custom:
.. include:: /partials/common.rst

Other Platform
==============

.. include:: /partials/note_enterprise_integration.rst

Adding Talkable to Your Site
----------------------------

In order to integrate Talkable campaign(s) on your site you need to set the following script into HEAD tag inside
your main layout which is used on every page. This is initialization of the Talkable JS integration library:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    window._talkableq = window._talkableq || [];
    _talkableq.push(['init', {
      site_id: 'YOUR-TALKABLE-SITE-ID' // Required - Talkable Site ID, you can find it on the Dashboard inside Talkable upon login
    }]);

    _talkableq.push(['authenticate_customer', {
      email: 'customer@example.com', // Optional - Customer email, it is recommended to always pass it when available
      first_name: 'Name', // Optional - Customer first name
      last_name: 'Surname' // Optional - Customer last name
    }]);
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

Site Placements
---------------

.. include:: /partials/site_placements_description.rst

|hr|

Post Purchase Site Placement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: /partials/post_purchase_description.rst

Below is an example of the very basic Post Purchase integration.

.. include:: /samples/ecommerce/custom/post_purchase_basic.rst

`Integration example <http://learn.talkable.com/docs/pp-basic>`_

:ref:`Learn more <optional/site_placements/post_purchase>` about more advanced features of Post Purchase integration.

|hr|

Advanced Features
-----------------

Here is a full list of things you can do with Talkable:

.. toctree::
  :maxdepth: 1
  :glob:

  /optional/*

