.. _ecommerce/platform/shopify:
.. include:: /partials/common.rst

Shopify Store Integration
=========================

To integrate your Shopify store, you can install the `Shopify Talkable application`_
from App Store or manually add a code snippet to your checkout page.

Automatic integration
---------------------

  .. note::

     If you have previosuly integrated with Talkable, make sure you remove the manual
     Talkable integration script located in the Additional Content & Scripts section before
     you start the Automatic integration process. See `Manual integration`_ for details.

1. In your Talkable administration panel, go to
   **Dashboard** |rarr| **Shopify Integration**.

2. Then click **Install Talkable** in your Shopify administration panel.

3. Modify existing integration script if needed.

4. Activate Post Purchase or Standalone Campaign.

5. Verify your integration using :ref:`Verifying Integration Instructions <ecommerce/verify>`.

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

4. Verify your integration using :ref:`Verifying Integration Instructions <ecommerce/verify>`.

|br|

.. _Shopify Talkable application: https://apps.shopify.com/talkable

.. include:: /partials/traffic_source.rst

.. container:: hidden

   .. toctree::
