.. _ecommerce:
.. include:: /partials/common.rst

E-Commerce Integrations
#######################

Talkable integrates with e-commerce platforms or custom web sites through
JavaScript calls to our API. But most customers can integrate quickly without
knowing how to code.

The standard integration provides end-to-end referral tracking and displays
offers via popup after purchase. Other features are optional.

.. Using `raw` directive here so this subtitle doesn't get added to toctree
.. raw:: html

   <h2>E-commerce Platform Integration</h2>

If you use one of the shopping carts listed in :ref:`platform integration <ecommerce/platform>` section, you can use a supported
extension to integrate Talkable. It's often as easy as copying and pasting code,
and we provide instructions.

.. raw:: html

   <h2>E-commerce Custom Integration</h2>

If you're not using one these shopping carts, you can still use Talkable.
With our :ref:`custom integration <ecommerce/custom>` option, you just copy
a few lines of JavaScript to your order confirmation page and you're ready to go.

.. raw:: html

   <h2>Tag Managers</h2>

If you are using |segment_io| as your tag manager, it can be used to "toggle"
Talkable on.

Instructions can be found at:
|customer_io|

.. raw:: html

   <h2>Getting Additional Help</h2>

If you would like help integrating Talkable, or you're an enterprise client
looking for integration services, feel free to |contact_us|.

.. |segment_io| raw:: html

   <a href="https://segment.io/" target="_blank">Segment.io</a>

.. |customer_io| raw:: html

   <a href="http://customer.io/docs/basic-integration.html" target="_blank">http://customer.io/docs/basic-integration.html</a>

.. container:: hidden

   .. toctree::

      ecommerce/custom
      ecommerce/platform
      ecommerce/verify
      ecommerce/verification_digest

