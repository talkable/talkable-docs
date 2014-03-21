.. _ecommerce/platform/oscommerce:
.. include:: /partials/common.rst

osCommerce Store Integration
----------------------------

1. Download the `osCommerce Curebit Add-On`_ package and unzip it to your
   osCommerce catalog directory (eg /var/www/oscommerce/catalog).
2.

   * For **version 2.3**, in your catalog directory, edit *checkout_success.php*
     and replace this code:

     .. include:: /samples/ecommerce/platform/oscommerce-23-before.rst

     With this code:

     .. include:: /samples/ecommerce/platform/oscommerce-23-after.rst

   * For **version 2.2**, in your catalog directory, edit *checkout_success.php*
     and replace this code:

     .. include:: /samples/ecommerce/platform/oscommerce-22-before.rst

     With this code:

     .. include:: /samples/ecommerce/platform/oscommerce-22-after.rst

3. Login to your administrator console (eg http://yourstoredomain.com/admin)
   with your administrator credentials.
4. Click on **Modules** |rarr| **Order Total**.
5. Click **Install Module** (osCommerce 2.3 only).
6. Click on the Curebit Checkout **Install** or **Install Module**.
7. Click **Edit**.
8. Enter your Curebit Site ID. You can get this from your Curebit dashboard
   after you log in and create a site.
9. Click **Save** (or **Update**).

.. _osCommerce Curebit Add-On: http://addons.oscommerce.com/info/7669

.. include:: /partials/verifying_integration.rst

.. container:: hidden

   .. toctree::
