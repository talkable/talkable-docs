.. _integration/loyalty/shopify_integration:
.. include:: /partials/common.rst

.. meta::
   :description: Learn how to manually set up loyalty Shopify integration.

Shopify Integration
===================

.. _integration/loyalty/shopify/automatic_integration:

Automatic integration
---------------------

After passing :ref:`Shopify authorization <integration/ecommerce_platforms/shopify/automatic_integration>`,
Loyalty page will be located at `/pages/loyalty`.

To turn Loyalty integration on/off, navigate to Talkable Shopify Integration page `https://admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/integration/shopify`

.. _integration/loyalty/shopify/manual_integration:

Manual integration
------------------

1. Pass Shopify authorization
2. You will be redirected to your Shopify store, log in and click the Install button
3. After successful installation you will be redirected back to Talkable
4. Click “Integrate manually“
5. Set up Referral Integration :ref:`manually <integration/ecommerce_platforms/shopify/manual_integration>`
6. In your Shopify Admin create resources for loyalty dashboard page:

    1. Create a loyalty dashboard page section:

        * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Sections**
        * Click “Add a new section“
        * Create a new Liquid section called `talkable-loyalty-dashboard.liquid`
        * In the newly created file, add the following code:

          .. code-block:: html

             {% if shop.customer_accounts_enabled %}
               <div id="talkable-loyalty"></div>
             {% endif %}

        * Optionally, update the schema name to anything meaningful, for example, “Loyalty dashboard“
        * Click “Save”

    2. Create a loyalty dashboard page template:

        * Go to **Templates**
        * Click “Add a new template“
        * Create a new JSON template of type `page` called `loyalty_dashboard.talkable` (`page.loyalty_dashboard.talkable.json`)
        * Change the type of the main section to `talkable-loyalty-dashboard`

          .. code-block:: JSON

             {
               "sections": {
                 "main": {
                   "type": "talkable-loyalty-dashboard"
                 }
               }
             }

          .. important::
             The name of the section should be the same as the one you used
             in the previous step when naming your section file.

          .. important::
             If your main section is disabled, remove the row that does it.

    3. Create a page:

        * Exit theme editor if it was opened
        * Go to **Online Store** → **Pages**
        * Click “Add page“
        * Add title: `Loyalty Dashboard`
        * Select theme template: `loyalty_dashboard.talkable`
        * Click “Save”

.. raw:: html

   <h2>Requirements</h2>

User accounts. The website must support user accounts since the loyalty program is only available to logged in users.

Manual migrating from a vintage theme to an Online store 2.0 theme
------------------------------------------------------------------

If you have previously integrated Talkable in your vintage Shopify theme and want to migrate to a newer theme,
you need to do the following:

1. :ref:`Migrate the referral pages <integration/ecommerce_platforms/shopify/manual_integration_theme_migration>`

2. If you have a `templates/page.talkable-loyalty-dashboard.liquid` file, store its content elsewhere and delete the file

3. Create a loyalty dashboard page section:

    * In the theme code editor (**Online Store** → **Themes** → **Edit code**), go to **Sections**
    * Click “Add a new section“
    * Create a new Liquid section called `talkable-loyalty-dashboard.liquid`
    * In the newly created file, add the following code:

      .. code-block:: html

         {% if shop.customer_accounts_enabled %}
           <div id="talkable-loyalty"></div>
         {% endif %}

      If there were any customizations in the `templates/page.talkable-loyalty-dashboard.liquid`, add them as well

    * Optionally, update the schema name to anything meaningful, for example, “Loyalty dashboard“
    * Click “Save”

4. Create a loyalty dashboard page template:

    * Go to **Templates**
    * Click “Add a new template“
    * Create a new JSON template of type `page` called `loyalty_dashboard.talkable` (`page.loyalty_dashboard.talkable.json`)
    * Change the type of the main section to `talkable-loyalty-dashboard`

      .. code-block:: JSON

         {
           "sections": {
             "main": {
               "type": "talkable-loyalty-dashboard"
             }
           }
         }

      .. important::
         The name of the section should be the same as the one you used
         in the previous step when naming your section file.

      .. important::
         If your main section is disabled, remove the row that does it.
