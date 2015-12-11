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

By default Post Purchase campaign loads with a preloader. Adding `style` attribute to `iframe` object changes its appearance:

.. code-block:: html

  <!-- Place Talkable Container into appropriate place in the DOM -->
  <div id="talkable-pp-container"></div>

  <script>
    // All standard JS integration config goes here
    // var _talkableq = _talkableq || [];
    // ...

    var _talkable_purchase = {
      // ...
      iframe: {
        container: 'talkable-pp-container', // container element to where to place the iframe
        style: "display: none;" // this is just a standard inline CSS
      },
      // ...
    };

    // ...
    // _talkableq.push(['register_purchase', _talkable_purchase]);
  </script>

Embedding as Inline Widget
--------------------------

Post Purchase campaign can be also embedded as inline widget somewhere on the page. For that we only require placing the Container element into appropriate place on the site where Talkable iframe will be placed.

.. code-block:: html

  <!-- Place Talkable Container into appropriate place in the DOM -->
  <div id="talkable-pp-container"></div>

  <script>
    // All standard JS integration config goes here
    // var _talkableq = _talkableq || [];
    // ...

    var _talkable_purchase = {
      // ...
      iframe: {
        container: 'talkable-pp-container', // container element to where to place the iframe
        style: "display: block; width: 100%;" // this is just a standard inline CSS
      },
      // ...
    };

    // ...
    // _talkableq.push(['register_purchase', _talkable_purchase]);
  </script>

