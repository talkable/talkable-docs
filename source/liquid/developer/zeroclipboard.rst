.. _liquid/developer/zeroclipboard:
.. include:: /partials/common.rst

Zeroclipboard tricks
====================

If you want use two element zeroclipboard and in turn show them, then you need to use code like this:

**HTML:**

.. code-block:: html

  <div class="js-before">
    <div data-clipboard-text="First" data-copied-label="First" class="js-click-to-copy">
      First element
    </div>
  </div>
  <div class="js-after hidden">
    <div data-clipboard-text="Second" data-copied-label="Second" class="js-click-to-copy">
      Second element
    </div>
  </div>

**JS:**

.. code-block:: javascript

  $(function() {

    Curebit.bindClickToCopy('.js-click-to-copy');

    var switchBlocks = function() {
      $('.js-before, .js-after').toggleClass("hidden");
      // Re-init ZeroClipboard instance to refresh tooltip position
      Curebit.bindClickToCopy('.js-click-to-copy');
    };

  });

**CSS:**

.. code-block:: css

  .hidden {
    display: none;
  }
