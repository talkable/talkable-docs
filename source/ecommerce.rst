.. _ecommerce:
.. include:: /partials/common.rst

E-Commerce Integration
######################

.. Using `raw` directive here so this subtitle doesn't get added to toctree
.. raw:: html

   <h2>Getting Started</h2>

First of all please choose your platform, we make things really easy if you integrate
via official Talkable extension:

1. :ref:`Shopify <ecommerce/platform/shopify>`
2. :ref:`Magento <ecommerce/platform/magento>`
3. :ref:`Custom platform <ecommerce/custom>`

.. raw:: html

   <h2>How It Works?</h2>

.. image:: /_static/img/integration.png
   :alt: Integration,
   :class: is-minimal

Talkable integrates with e-commerce platforms or custom web sites through
JavaScript calls to Talkable API. But most customers can integrate quickly without
knowing how to code.

The standard integration provides end-to-end referral tracking that has two steps:

1. Opening the referral loop — this is a place from where |advocate| invites their
   |friend|. This step is a starting point of the referral program. It can be either
   a standalone page somewhere on your website from where all the sharing is done or
   a post purchase popup on the order confirmation page so that each customer who
   buys can participate in the referral program as |advocate|.
2. Closing the referral loop — it is not customer facing piece, it only creates
   |advocate| and |friend| relation which is called "Referral". At this point
   Talkable checks the referral for fraud and makes decision as to rewarding
   |advocate| for successful referral or blocking it, based on fraud setup.

.. raw:: html

   <h2>Getting Additional Help</h2>

If you need help integrating Talkable, or you're an enterprise client
looking for integration services, feel free to |contact_us|.

.. container:: hidden

   .. toctree::

      ecommerce/platform/shopify
      ecommerce/platform/magento
      ecommerce/custom

   .. toctree::
      :hidden:

      ecommerce/platform
      ecommerce/verify

