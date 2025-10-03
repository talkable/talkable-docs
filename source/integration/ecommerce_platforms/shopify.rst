.. _integration/ecommerce_platforms/shopify:
.. include:: partials/common.rst

.. meta::
   :description: Here’s how you can integrate Talkable Shopify app with your store.

Shopify
=======

.. _integration/ecommerce_platforms/shopify/automatic_integration:

Automatic integration
---------------------

.. note::

   If you have previously integrated with Talkable, make sure you remove the manual
   Talkable integration script located in the Additional Content & Scripts section before
   you start the Automatic integration process. See `Manual integration`_ for details.

1. Contact sales@talkable.com to learn about our pricing and set up an account with Talkable

   - Provide a valid Shopify store URL. Example: `https://123test.myshopify.com`
   - Choose “Shopify” as your platform during registration process

2. Install the Shopify integration app via the link provided by Talkable team
3. After the successful installation you will be redirected back to Talkable
4. Enable “Referral Integration“ toggle
5. Create, set up, and launch Campaigns (Invite, Advocate Dashboard, etc.)
6. Verify your integration using :ref:`Verifying Integration instructions <integration/verify>`

   .. note::

      Post Purchase campaign is located at the “Thank you” page after Checkout.

      To check how Standalone Campaign looks visit */pages/share* or */pages/invite* links of your store.
      You can edit these links in Administrative panel of your store.

   .. important::

      If you are managing the Shopify theme code using a `Shopify Github integration`_,
      make sure to pull the changes to the theme made by the automatic integration to avoid
      resetting them with a commit. The theme updates are described in the
      :ref:`Manual integration instructions<integration/ecommerce_platforms/shopify/manual_integration>`.

.. _integration/ecommerce_platforms/shopify/manual_integration:

Manual integration
------------------

For Shopify Online Store 2.0 themes
...................................

If your Shopify store uses an `Online Store 2.0 theme <https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions>`_,
please follow the instructions below.

1. Provide a valid Shopify store URL and choose “Shopify” as your platform during registration process
2. On the Welcome screen click “I’m a Developer”
3. Pass Shopify authorization
4. You will be redirected to your Shopify store, log in and click the install button
5. After successful installation you will be redirected back to Talkable
6. Click “Integrate manually“
7.  In your Shopify Admin, add the integration to your layout:

    1.  Create a snippet:

        * Go to **Online Store** → **Themes**
        * Click **Actions** ("..." button) → **Edit code**
        * Go to **Snippets**
        * Click “Add a new snippet“
        * Create a new snippet called `talkable-partial`
        * In the newly created file, add the following code:

          .. include:: samples/ecommerce/platform/shopify_init_script.rst

          .. include:: partials/note_sample_code.rst

        * Click “Save”

    2.  Render the snippet in the layout:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Layout**
        * Open `theme.liquid` file
        * Before closing `</head>` paste the following code:

          .. code-block:: liquid

             {% render "talkable-partial" %}

        * Click “Save”

8.  In your Shopify Admin, create resources for referral share page:

    1.  Create a share page section:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Sections**
        * Click “Add a new section“
        * Create a new Liquid section called `talkable-campaign.liquid`
        * In the newly created file, add the `<div>` block for the referral campaign.

          .. code-block:: html

             <div id="talkable-offer"></div>

        * Optionally, update the schema name to anything meaningful, for example, “Referral campaign“

          .. image:: _static/img/shopify/editor_section.png
             :alt: Shopify editor - talkable-campaign section
             :class: is-minimal

        * Click “Save”

    2.  Create a share page template:

        * Go to **Templates**
        * Click “Add a new template“
        * Create a new JSON template of type `page` called `talkable` (`page.talkable.json`)
        * Change the type of the main section to `talkable-campaign`

          .. image:: _static/img/shopify/editor_template.png
             :alt: Shopify editor - Talkable page section
             :class: is-minimal

          .. important::
             The name of the section should be the same as the one you used
             in the previous step when naming your section file.

          .. important::
             If your main section is disabled, remove the row that does it.

    3.  Create a page:

        * Exit theme editor if it was opened
        * Go to **Online Store** → **Pages**
        * Click “Add page“
        * Add title: `Share`
        * Select theme template: `talkable`
        * Click “Save”

9.  In your Shopify Admin, create resources for referral dashboard page:

    1.  Create a dashboard page section:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Sections**
        * Click “Add a new section“
        * Create a new Liquid section called `talkable-dashboard.liquid`
        * In the newly created file, add the following code:

          .. code-block:: html

             {% if shop.customer_accounts_enabled %}
               {% if customer %}
                 <div id="talkable-offer"></div>
               {% else %}
                 {{ 'Log in' | customer_login_link }}
               {% endif %}
             {% endif %}

        * Optionally, update the schema name to anything meaningful, for example, “Referral dashboard“
        * Click “Save”

    2.  Create a dashboard page template:

        * Go to **Templates**
        * Click “Add a new template“
        * Create a new JSON template of type `page` called `dashboard.talkable` (`page.dashboard.talkable.json`)
        * Change the type of the main section to `talkable-dashboard`

          .. code-block:: JSON

             {
               "sections": {
                 "main": {
                   "type": "talkable-dashboard"
                 }
               }
             }

          .. important::
             The name of the section should be the same as the one you used
             in the previous step when naming your section file.

          .. important::
             If your main section is disabled, remove the row that does it.

    3.  Create a page:

        * Exit theme editor if it was opened
        * Go to **Online Store** → **Pages**
        * Click “Add page“
        * Add title: `Referral Dashboard`
        * Select theme template: `dashboard.talkable`
        * Click “Save” (Customer accounts must be enabled in **Settings** → **Checkout**)

10. In your Shopify Admin, add a post-purchase script:

    * Go to **Settings** → **Checkout**
    * Scroll down to **Order status page**
    * Paste the following code into **Additional scripts** field:

      .. include:: samples/ecommerce/platform/shopify.rst

      .. include:: partials/note_sample_code.rst

    * Click “Save”.

11. Verify your integration using :ref:`Verifying Integration instructions <integration/verify>`.

.. important::

   If you are managing the Shopify theme code using a `Shopify Github integration`_,
   make sure to pull the changes to the theme made by the automatic integration to avoid
   resetting them with a commit.

For Shopify vintage themes
..........................

If your Shopify store uses a `vintage theme <https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions>`_,
please follow the instructions below.

1. Provide a valid Shopify store URL and choose “Shopify” as your platform during registration process
2. On the Welcome screen click “I’m a Developer”
3. Pass Shopify authorization
4. You will be redirected to your Shopify store, log in and click the install button
5. After successful installation you will be redirected back to Talkable
6. Click “Integrate manually“
7.  In your Shopify Admin, add the integration to your layout:

    1.  Create a snippet:

        * Go to **Online Store** → **Themes**
        * Click **Actions** ("..." button) → **Edit code**
        * Go to **Snippets**
        * Click “Add a new snippet“
        * Create a new snippet called `talkable-partial`
        * In the newly created file, add the following code:

          .. include:: samples/ecommerce/platform/shopify_init_script.rst

          .. include:: partials/note_sample_code.rst

        * Click “Save”

    2.  Render the snippet in the layout:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Layout**
        * Open `theme.liquid` file
        * Before closing `</head>` paste the following code:

          .. code-block:: liquid

             {% render "talkable-partial" %}

        * Click “Save”

8.  In your Shopify Admin, create resources for referral share page:

    1.  Create a share page template:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Templates**
        * Click “Add a new template“
        * Create a new Liquid template of type `page` called `talkable` (`page.talkable.liquid`)
        * Paste the following code inside layout of this page instead of `{{ page.content }}`:

          .. code-block:: html

             <div id="talkable-offer"></div>

        * Click “Save”

    2.  Create a page:

        * Exit theme editor if it was opened
        * Go to **Online Store** → **Pages**
        * Click “Add page“
        * Add title: `Share`
        * Select theme template: `talkable`
        * Click “Save”

9.  In your Shopify Admin, create resources for referral dashboard page:

    1.  Create a dashboard page template:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Templates**
        * Click “Add a new template“
        * Create a new Liquid template of type `page` called `dashboard.talkable` (`page.dashboard.talkable.liquid`)
        * Paste the following code inside layout of this page instead of `{{ page.content }}`:

          .. code-block:: html

             {% if shop.customer_accounts_enabled %}
               {% if customer %}
                 <div id="talkable-offer"></div>
               {% else %}
                 {{ 'Log in' | customer_login_link }}
               {% endif %}
             {% endif %}

        * Click “Save”

    2.  Create a page:

        * Exit theme editor if it was opened
        * Go to **Online Store** → **Pages**
        * Click “Add page“
        * Add title: `Referral Dashboard`
        * Select theme template: `dashboard.talkable`
        * Click “Save” (Customer accounts must be enabled in **Settings** → **Checkout**)

10. In your Shopify Admin, add a post-purchase script:

    * Go to **Settings** → **Checkout**
    * Scroll down to **Order status page**
    * Paste the following code into **Additional scripts** field:

      .. include:: samples/ecommerce/platform/shopify.rst

      .. include:: partials/note_sample_code.rst

    * Click “Save”.

11. Verify your integration using :ref:`Verifying Integration instructions <integration/verify>`.

    .. code:: html

      <span class="a">https://123test.myshopify.com</span>

.. important::

   If you are managing the Shopify theme code using a `Shopify Github integration`_,
   make sure to pull the changes to the theme made by the automatic integration to avoid
   resetting them with a commit.

.. _integration/ecommerce_platforms/shopify/manual_integration_theme_migration:

Manual migrating from a vintage theme to an Online store 2.0 theme
------------------------------------------------------------------

If you have previously integrated Talkable in your vintage Shopify theme and want to migrate to a newer theme,
you need to do the following:

1.  Share page migration:

    1. If you have a `templates/page.talkable.liquid` file, store its content elsewhere and delete the file
    2.  Create a share page section:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Sections**
        * Click “Add a new section“
        * Create a new Liquid section called `talkable-campaign.liquid`
        * In the newly created file, add the `<div>` block for the referral campaign.

          .. code-block:: html

             <div id="talkable-offer"></div>

          If there were any customizations in the `templates/page.talkable.liquid`, add them as well

        * Optionally, update the schema name to anything meaningful, for example, “Referral campaign“
        * Click “Save”

    3.  Create a share page template:

        * Go to **Templates**
        * Click “Add a new template“
        * Create a new JSON template of type `page` called `talkable` (`page.talkable.json`)
        * Change the type of the main section to `talkable-campaign`

          .. image:: _static/img/shopify/editor_template.png
             :alt: Shopify editor - Talkable page section
             :class: is-minimal

          .. important::
             The name of the section should be the same as the one you used
             in the previous step when naming your section file.

          .. important::
             If your main section is disabled, remove the row that does it.

2.  Dashboard page migration:

    1. If you have a `templates/page.talkable-dashboard.liquid` file, store its content elsewhere and delete the file
    2.  Create a dashboard page section:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Sections**
        * Click “Add a new section“
        * Create a new Liquid section called `talkable-dashboard.liquid`
        * In the newly created file, add the `<div>` block for the referral campaign.

          .. code-block:: html

             {% if shop.customer_accounts_enabled %}
               {% if customer %}
                 <div id="talkable-offer"></div>
               {% else %}
                 {{ 'Log in' | customer_login_link }}
               {% endif %}
             {% endif %}

          If there were any customizations in the `templates/page.talkable-dashboard.liquid`, add them as well

        * Optionally, update the schema name to anything meaningful, for example, “Referral dashboard“
        * Click “Save”

    3.  Create a dashboard page template:

        * Go to **Templates**
        * Click “Add a new template“
        * Create a new JSON template of type `page` called `dashboard.talkable` (`page.dashboard.talkable.json`)
        * Change the type of the main section to `talkable-dashboard`

          .. code-block:: JSON

             {
               "sections": {
                 "main": {
                   "type": "talkable-dashboard"
                 }
               }
             }

          .. important::
             The name of the section should be the same as the one you used
             in the previous step when naming your section file.

          .. important::
             If your main section is disabled, remove the row that does it.

.. important::

   If you are managing the Shopify theme code using a `Shopify Github integration`_,
   make sure to pull the changes to the theme made by the automatic integration to avoid
   resetting them with a commit.

.. note::
   Also Talkable provides integration for Shopify Plus.


.. include:: partials/contact_us.rst

.. _Shopify Github integration: https://shopify.dev/docs/storefronts/themes/tools/github
