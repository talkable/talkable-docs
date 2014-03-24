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
  <div class="js-after">
    <div data-clipboard-text="Second" data-copied-label="Second" class="js-click-to-copy">
      Second element
    </div>
  </div>

**JS:**

.. code-block:: javascript

  $(function() {

    Curebit.bindClickToCopy('.js-click-to-copy');

    var switchBlocks = function() {
      $('.js-before').hide(300);
      setTimeout(function() {
        $('.js-after').show(300);
        // after you showed block, need re-init zeroclipboard
        Curebit.bindClickToCopy('.js-click-to-copy');
      }, 300);
    };

  });

**CSS:**

.. code-block:: css

  .js-after {
    display: none;
  }
