.. raw:: html

   <h2>Optimizing for Viewport</h2>

Curebit provides flexibility for the merchant to decide how they want to
optimize mobile.

If your site is responsive, all you'll want to do is set ``responsive: true``.
In your campaign, there are different views for mobile, tablet and desktop.
We'll automatically pull the correct theme view based on the user's device
once we detect the viewport. We'll use our responsive engine to size the
Curebit iframe to the right size. Like Magic! You'll also want to comment out
``device: 'desktop'`` line.

If you have separate mobile, tablet and desktop sites (or any combination of
the three), you can leave ``responsive: true`` on but also specifically set the
campaign theme view to use. This will prevent Curebit from automatically
assigning the theme view to use, but will allow us to resize within the screen
to make sure all elements fit well.

.. raw:: html

   <h2>Setup Your Theme</h2>

Make sure you have this CSS in your campaign theme so it won't have a double
scrollbars on resize (if ``responsive: true``)

.. code:: css

   body { overflow: hidden; }

`Demo integration link <http://jsfiddle.net/iurevych/sVtc8/>`_
