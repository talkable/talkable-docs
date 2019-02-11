.. _integration/shopify:
.. include:: /partials/common.rst

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

2. On the Welcome screen click "I’m a Developer"
3. Click **Install Shopify App**
4. You will be redirected to your Shopify store, log in and click the install button
5. After successful installation you will be redirected back to Talkable
6. Create, set up, and launch Campaigns (Invite, Advocate Dashboard, etc.)
7. Verify your integration using :ref:`Verifying Integration instructions <integration/verify>`.

  .. note::

     Post Purchase campaign is located at the “Thank you” page after Checkout.

     To check how Standalone Campaign looks visit */pages/share* or */pages/invite* links of your store.
     You can edit these links in Administrative panel of your store.

Manual integration
------------------

1. In your Shopify Admin follow:

    * Online Store
    * Themes
    * Click “Customize” near your current theme
    * Theme actions → Edit code
    * Open `Layout / theme.liquid` file
    * Before closing `</head>` paste the following code:

    .. include:: /samples/ecommerce/platform/shopify_init_script.rst

    .. include:: /partials/note_sample_code.rst

    .. include:: /partials/note_sample_integration.rst

    * Click “Save”.

2. Then navigate to:

    * Open `Themes/Templates`
    * Click `Add a new template`
    * Create a new template for `page` called `talkable`
    * Paste the following code inside layout of this page:

    .. code-block:: html

      <div id="talkable-offer"></div>

    * Click “Save”

3. Then navigate to:

    * Open `Online Store / Pages`
    * Click `Add page`
    * Select Template suffix `page.talkable`
    * Click “Save”

4. Then navigate to:

    * Settings
    * Checkout
    * Scroll down to **Order Processing**
    * Paste the following code into **Additional scripts** field:

    .. include:: /samples/ecommerce/platform/shopify.rst

    .. include:: /partials/note_sample_code.rst

    .. include:: /partials/note_sample_integration.rst

5. Click “Save”.
6. Verify your integration using :ref:`Verifying Integration instructions <integration/verify>`.

Watch a |video| demonstrating the full integration from start to finish.

|br|

.. |example_link| raw:: html

  <span class="a">http://123test.myshopify.com</span>

.. |video| raw:: html

   <a href="https://youtu.be/NxVscXSRtSA" target="_blank">video</a>

.. container:: hidden

   .. toctree::

      Verifying Integration instructions <verify>
