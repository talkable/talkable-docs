.. _ecommerce/platform/x-cart:
.. include:: /partials/common.rst

X-Cart Store Integration
------------------------

1. Download the `X-Cart Curebit Module`_ and unzip it to your X-Cart main directory.
2. Open the file located at:

   | */skin/%FOLDER WITH YOUR CURRENT SKIN%/customer/main/order_message.tpl*

   using your favorite text editor if you use an external skin, otherwise edit:

   | */skin/common_files/customer/main/order_message.tpl*

3. Add the following code at the end of the file:

   .. code::

      {if $active_modules.Curebit}{include file="modules/Curebit/curebit.tpl"}{/if}

4. Save this file and upload it to your site.
5. Run the script located at *http://www.yoursite.com/curebit_install.php*

.. _X-Cart Curebit Module: http://curebit.com/xcart/curebit.zip

|br|

:ref:`Verifying Integration Instructions <ecommerce/verify>`

.. container:: hidden

   .. toctree::
