.. _integration/custom/integration_tag_manager:
.. include:: /partials/common.rst

Integrating with a Tag Manager
==============================

-  :underline:`Initialization Script in a Tag Manager:` Place the
   :ref:`Initialization Script <integration/custom/integration_components/initialization_script>`
   in a tag that is
   visible in the head template on all pages.

-  :underline:`Post Purchase Integration in a Tag Manager:` Since the post
   purchase integration on the checkout confirmation page requires the
   Init script to work, you’re welcome to combine the :ref:`Initialization Script <integration/custom/integration_components/initialization_script>`
   + :ref:`Post Purchase Script <integration/custom/integration_components/post_purchase_script>`
   script into a
   single tag for the checkout confirmation page. In fact this is
   recommended for Google Tag Manager, when combining the place the
   Initialization script on top/before the Post purchase script in the
   tag.

-  :underline:`Tag Manager Data Layer to Pass Variables:` You’ll need to
   ensure a data layer object is set up to collect and pass the
   variables to Talkable inside your tag.

-  :underline:`Troubleshooting:` You can use `window._talkableq` for all
   `talkableq` variable instances if you’re having trouble with variable
   interpolation and need to use a global namespace.
