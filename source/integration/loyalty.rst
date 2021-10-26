.. _integration/loyalty:
.. include:: /partials/common.rst

.. meta::
   :description: You can integrate Talkable Loyalty to e-commerce sites in a few quick steps.

Loyalty Integration (beta)
==========================

Integrating Talkable Loyalty to e-commerce sites is done in
a few quick steps by adding the below scripts to your site.

.. _loyalty_integration:

   .. raw:: html

      <h2>Integration</h2>

1. Initialize Talkable integration library.

   Add the :ref:`Talkable Initialization Script <integration/loyalty/integration_components/initialization_script>`
   to your header or any template spanning every page.

 .. note::

    Skip this step if you already have Talkable integrated on your site

2. Add Loyalty Dashboard.

   To host the Loyalty campaign, create a new HTML page with a standard
   header/footer. The best practice is to create this page on ``www.your-site.com/loyalty``

   Copy Talkable container DIV element & paste it exactly where the Talkable iframe should be rendered, similarly to the referral standalone placement:

   .. code-block:: html

      <div id="talkable-loyalty"></div>

3. Add Redeem Widget.

   Copy Talkable container DIV element & paste it at the checkout
   exactly where the loyalty points redemption widget should render:

   .. code-block:: html

      <div id="talkable-loyalty"></div>

   It is recommended to add it above the discount field. Examples:

   .. figure:: /_static/img/loyalty/loyalty_checkout.png
      :alt: Sample checkout

4. Define Loyalty points redemption batches.

   Each redemption batch determines progressive point redemption options based on the available points balance of the loyalty member.
   For example, 500 points would equal a discount coupon for $50 off, 1000 points would equal $100, and so on.

   For every redemption batch, please generate single-use coupons for
   a certain discount amount ($50 off, $100 off, etc.) and upload all coupon lists into Talkable loyalty coupon lists.

   It is recommended to upload 100,000 single-use coupons into every coupon list.

   .. figure:: /_static/img/loyalty/redemption_batches.png
      :alt: Redemption batches

 .. note::

    All design and loyalty campaign setup is done inside the Talkable platform,
    then via iframe loyalty campaign content is injected into the site.

.. _loyalty_manual_integration:

   .. raw:: html

      <h2>Loyalty Manual Shopify integration</h2>

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

.. raw:: html

   <h2>Requirements</h2>

1. User accounts. The website must support user accounts since the loyalty program is only available to logged in users.

2. Single-use coupons. Every loyalty member will have a choice of redemption batches to redeem points for a one-time discount.
   When pressing a redeem button Talkable deducts points and issues a single-use coupon in return.

3. Ideally, only purchases without tax & shipping costs should be passed to Talkable.
   This simplifies future refunds support as taxes and shipping costs are not refundable.

.. container:: hidden

 .. toctree::

    loyalty/integration_components
    loyalty/custom_app
    loyalty/auto_enrollment
