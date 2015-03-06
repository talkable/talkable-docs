.. _ecommerce/platform/shopify:
.. include:: /partials/common.rst

Shopify Store Integration
=========================

To integrate your Shopify store, you can install the `Shopify Talkable application`_
from App Store or manually add a code snippet to your checkout page.

Automatic integration
---------------------

1. In your Talkable administration panel, go to
   **Dashboard** |rarr| **Site Settings** |rarr| **Shopify Integration**.
2. Click **Initial Setup**

   .. image:: /_static/img/shopify-initial-setup.png
      :alt: Shopify initial setup
      
3. Modify existing integration script if needed

   .. image:: /_static/img/shopify-integration-script.png
      :alt: Shopify integration script

|br|

:ref:`Verifying Integration Instructions <ecommerce/verify>`

Manual integration
------------------

1. In your Shopify administration panel, go to
   **Settings** |rarr| **Checkout & Payment**.
2. Under **Order Processing** |rarr| **Additional Content & Scripts**,
   insert this code:

   .. include:: /partials/note_sample_code.rst

   .. include:: /samples/ecommerce/platform/shopify.rst

3. Click **Apply these settings**.

|br|

:ref:`Verifying Integration Instructions <ecommerce/verify>`

.. _Shopify Talkable application: https://apps.shopify.com/talkable-referral-platform

.. container:: hidden

   .. toctree::
