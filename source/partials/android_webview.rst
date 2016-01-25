.. raw:: html

   <h2>Show offer</h2>

When you have `registeredOrigin` you can show offer for user from `activity`.
You can do this in two ways:

1. Show full screen offer

.. code-block:: java

  registeredOrigin.showFullScreenOffer(this);

2. Get fragment with offer and place into container in your activity

.. code-block:: java

  registeredOrigin.getOfferFragment();
