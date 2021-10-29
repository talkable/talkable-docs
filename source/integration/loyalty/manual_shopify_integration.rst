.. _integration/loyalty/manual_shopify_integration:
.. include:: /partials/common.rst

.. meta::
   :description: Learn how to manually set up loyalty Shopify integration.

Manual Shopify integration
==========================

1. Pass Shopify authorization
2. You will be redirected to your Shopify store, log in and click the Install button
3. After successful installation you will be redirected back to Talkable
4. Click “Integrate manually“
5. Set up Referral Integration :ref:`manually <integration/ecommerce_platforms/shopify/manual_integration>`
6. Then navigate to:

    * Open `Themes / Templates`
    * Click “Add a new template“
    * Create a new template for `page` called `loyalty`
    * Paste the following code inside layout:

    .. code-block:: html

      {% if shop.customer_accounts_enabled %}
         <div id="talkable-loyalty"></div>
      {% endif %}

    * Click “Save”

7. Then navigate to:

    * Open `Online Store / Pages`
    * Click “Add page“
    * Add title `loyalty`
    * Select Theme template `loyalty`
    * Click “Save”

.. raw:: html

   <h2>Requirements</h2>

User accounts. The website must support user accounts since the loyalty program is only available to logged in users.
