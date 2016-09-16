.. _campaigns/site_placements/post_purchase:
.. include:: /partials/common.rst

.. _post_purchase_campaign:

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

When the Talkable JS integration library is all set (:ref:`see 1 step here <ecommerce/custom>`) on the order confirmation page the following integration script needs to be included:

.. include:: /samples/ecommerce/custom/post_purchase_basic.rst

.. note::

  1. Purchase subtotal amount should not include the discount, shipping, and taxes.
  2. Make sure to pass email address of the customer, otherwise Purchase won't be registered. See `Overriding Customer Data`_.

.. container:: hidden

  .. toctree::

Including Product Items
-----------------------

You can also add product specific tracking to Talkable, which will let your customers share specific items that they've purchased. Customer shares with products have higher click through and conversion rates.

Below is an example with product items passed along with purchase data (notice FOR loop):

.. include:: /samples/optional/product_items.rst

.. note::

  All product items are included into Purchase details inside Purchases report. This information is helpful for debugging.

Embedding as Inline Widget
--------------------------

Post Purchase campaign can be also embedded as inline widget somewhere on the page. For that we only require placing the Container DIV element into appropriate place on the site where Talkable iframe will be placed.

Next step is to go into that Post Purchase campaign inside Talkable and:

1. Visit Editor
2. Switch into HTML/CSS editor (top right corner)
3. Open Extra fields
4. Enable Responsive iframe feature by pressing "On"
5. Find Integration CSS textarea and change its CSS to position the iframe not as a popup but as inline block. Here is an example that does it:

.. code-block:: scss

  #{$iframe} {
    display: block;
    width: 100%;
  }

6. Now close Extra fields and inside HTML code area remove the following lines of code:

.. code-block:: html

  <div class="campaign-overlay"></div>

And remove this DIV as well:

.. code-block:: html

  <div class="campaign-helper"></div>

7. Inside CSS area replace this code:

.. code-block:: css

  body.signup,
  body.share {
      height: 100%;
  }

With this:

.. code-block:: css

  body.signup,
  body.share {
    overflow: hidden;
  }

Overriding Customer Data
------------------------

In case you need to override customer data during Purchase registration include `customer` object in addition to the rest of the data:

.. code-block:: html

  <!-- Place Talkable Container into appropriate place in the DOM -->
  <div id="talkable-offer"></div>

  <script>
    var _talkable_data = {
      // purchase: {
      // ...
      // },
      customer: {
        email: 'overridden@example.com',
        first_name: 'OverriddenName',
        last_name: 'OverriddenSurname'
      }
    };

    _talkableq.push(['register_purchase', _talkable_data]);
  </script>

