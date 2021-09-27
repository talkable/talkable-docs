.. _integration/shopify:
.. include:: /partials/common.rst

.. meta::
   :description: Here’s how you can integrate Talkable Shopify app with your store.

Shopify Integration
===================

Automatic integration
---------------------

  .. note::

     If you have previously integrated with Talkable, make sure you remove the manual
     Talkable integration script located in the Additional Content & Scripts section before
     you start the Automatic integration process. See `Manual integration`_ for details.

1. Contact sales@talkable.com to learn about our pricing and set up an account with Talkable

|space_indent| - Provide a valid Shopify store URL. Example: |example_link|. |br|
|space_indent| - Choose “Shopify” as your platform during registration process

2. On the Welcome screen click “I’m a Developer“
3. Pass Shopify authorization
4. You will be redirected to your Shopify store, log in and click the install button
5. After successful installation you will be redirected back to Talkable
6. Click “Integrate automatically“
7. Turn on coupon auto-sync checkbox
8. Create, set up, and launch Campaigns (Invite, Advocate Dashboard, etc.)
9. Verify your integration using :ref:`Verifying Integration instructions <integration/verify>`.

  .. note::

     Post Purchase campaign is located at the “Thank you” page after Checkout.

     To check how Standalone Campaign looks visit */pages/share* or */pages/invite* links of your store.
     You can edit these links in Administrative panel of your store.

Manual integration
------------------

1. Provide a valid Shopify store URL and choose “Shopify” as your platform during registration process
2. On the Welcome screen click “I’m a Developer”
3. Pass Shopify authorization
4. You will be redirected to your Shopify store, log in and click the install button
5. After successful installation you will be redirected back to Talkable
6. Click “Integrate manually“
7. In your Shopify Admin follow:

    * Online Store
    * Themes
    * Actions → Edit code
    * Open `Layout / theme.liquid` file
    * Before closing `</head>` paste the following code:

    .. include:: /samples/ecommerce/platform/shopify_init_script.rst

    .. include:: /partials/note_sample_code.rst

    .. include:: /partials/note_sample_integration.rst

    * Click “Save”.

8. Then navigate to:

    * Open `Themes / Templates`
    * Click “Add a new template“
    * Create a new template for `page` called `talkable`
    * Paste the following code inside layout of this page instead of `{{ page.content }}`:

    .. code-block:: html

      <div id="talkable-offer"></div>

    * Click “Save”
    * Create a new template for page called `dashboard.talkable`
    * Paste the following code inside layout of this page instead of `{{ page.content }}`:

    .. code-block:: html

      {% if shop.customer_accounts_enabled %}
        {% if customer %}
          <div id="talkable-offer"></div>
        {% else %}
          {{ 'Log in' | customer_login_link }}
        {% endif %}
      {% endif %}

9. Then navigate to:

    * Open `Online Store / Pages`
    * Click “Add page“
    * Add title `Share`
    * Select Template suffix `page.talkable`
    * Click “Save”
    * Click “Add page“
    * Add title `Referral Dashboard`
    * Select Template suffix `page.dashboard.talkable`
    * Click “Save” (Customer accounts must be enabled in `Settings / Checkout`)

10. Then navigate to:

    * Settings
    * Checkout
    * Scroll down to **Order Processing**
    * Paste the following code into **Additional scripts** field:

    .. include:: /samples/ecommerce/platform/shopify.rst

    .. include:: /partials/note_sample_code.rst

    .. include:: /partials/note_sample_integration.rst

11. Click “Save”.
12. Verify your integration using :ref:`Verifying Integration instructions <integration/verify>`.

.. |example_link| raw:: html

  <span class="a">http://123test.myshopify.com</span>

.. container:: hidden

   .. toctree::

      Verifying Integration instructions <verify>
