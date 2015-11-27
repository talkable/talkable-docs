.. _optional/site_placements/post_purchase:
.. include:: /partials/common.rst

Post Purchase
=============

.. include:: /partials/post_purchase_description.rst

Flow
----

.. image:: /_static/img/site_placements/pp.png
   :alt: Talkable campaign flow — Post Purchase template,
   :class: is-minimal

Basic Integration
-----------------

On the order confirmation page the following integration script needs to be included:

.. include:: /samples/ecommerce/custom/post_purchase_basic.rst

.. note::

  Purchase subtotal amount should not include the discount, shipping, and taxes.

.. container:: hidden

  .. toctree::

Including Product Items
-----------------------

You can also add product specific tracking to Talkable, which will let your customers share specific items that they've purchased. Customer shares with products have higher click through and conversion rates.

Below is an example with product items passed along with purchase data (notice FOR loop):

.. include:: /samples/optional/product_items.rst

.. note::

  All product items are included into Purchase details inside Purchases report. This information is helpful for debugging.

Hiding Campaign Preloader
-------------------------

Embedding as Inline Widget
--------------------------

