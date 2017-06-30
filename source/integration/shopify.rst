.. _integration/shopify:
.. include:: /partials/common.rst

Shopify Integration
===================

Automatic integration
---------------------

  .. note::

     If you have previously integrated with Talkable, make sure you remove the manual
     Talkable integration script located in the Additional Content & Scripts section before
     you start the Automatic integration process. See `Manual integration`_ for details.

1. Install the `Shopify Talkable application`_.

2. In your Talkable administration panel, go to
   **Dashboard** → Expand **Settings** dropdown → **Shopify Integration**.

3. Then click **Install Talkable** in your Shopify administration panel.

4. Modify existing integration script if needed.

5. Activate Post Purchase or Invite(Standalone) Campaign.

6. Verify your integration using :ref:`Verifying Integration <integration/verify>`.

  .. note::

     Post Purchase campaign is located at the Thank you page after Checkout.

     To check how Standalone Campaign looks visit */pages/share* or */pages/invite* links of your store.
     You can edit these links in Administrative panel of your store.

Manual integration
------------------

1. In your Shopify administration panel, go to
   **Settings** |rarr| **Checkout & Payment**.
2. Under **Order Processing** |rarr| **Additional Content & Scripts**,
   insert this code:

   .. include:: /partials/note_sample_code.rst

   .. include:: /samples/ecommerce/platform/shopify.rst

3. Click **Apply these settings**.

4. Verify your integration using :ref:`Verifying Integration <integration/verify>`.

|br|

.. _Shopify Talkable application: https://apps.shopify.com/talkable

.. container:: hidden

   .. toctree::

      Verifying Integration Instructions <verify>
