.. _integration/loyalty/manual_shopify_integration:
.. include:: /partials/common.rst

.. meta::
   :description: Learn how to manually setup loyalty shopify integration.

Loyalty Manual Shopify integration
==================================

1. Pass Shopify authorization :ref:`my-reference-label`.
2. You will be redirected to your Shopify store, log in and click the install button
3. After successful installation you will be redirected back to Talkable
4. Click “Integrate manually“
5. In your Shopify Admin follow:

    * Online Store
    * Themes
    * Actions → Edit code
    * Open `Layout / theme.liquid` file
    * Before closing `</head>` paste the following code:

    .. code-block:: html

      <div id="talkable-loyalty"></div>

    * Click “Save”.

6. Then navigate to:

    * Open `Themes / Templates`
    * Click “Add a new template“
    * Create a new template for `page` called `loyalty-dashboard`
    * Paste the following code inside layout:

    .. code-block:: html

      {% if shop.customer_accounts_enabled %}
         {% if customer %}
           <div id="talkable-loyalty"></div>
         {% else %}
           {{ 'Log in' | customer_login_link }}
         {% endif %}
      {% endif %}

    * Click “Save”

7. Then navigate to:

    * Open `Online Store / Pages`
    * Click “Add page“
    * Add title `loyalty-dashboard`
    * Select Theme template `loyalty-dashboard`
    * Click “Save”
