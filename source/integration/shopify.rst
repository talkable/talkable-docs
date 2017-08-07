.. _integration/shopify:
.. include:: /partials/common.rst

Shopify Integration
===================

Extension integration
---------------------

  .. note::

     If you have previously integrated with Talkable, make sure you remove the manual
     Talkable integration script located in the Additional Content & Scripts section before
     you start the Automatic integration process. See `Manual integration`_ for details.

1. Create Talkable account at |signup_link|

|space_indent| - Provide a valid Shopify store URL. Example: |example_link|. |br|
|space_indent| - Choose “Shopify” as your Platform during registration process

2. On the Welcome screen click "I’m Developer"
3. Click **Install Shopify App**
4. You will be redirected to your Shopify store, log in and click the install button
5. After successful installation you will be redirected back to Talkable
6. Create, set up, and Launch Campaigns (Invite, Advocate Dashboard, etc.)
7. Verify your integration using :ref:`Verifying Integration <integration/verify>`.

  .. note::

     Post Purchase campaign is located at the “Thank you” page after Checkout.

     To check how Standalone Campaign looks visit */pages/share* or */pages/invite* links of your store.
     You can edit these links in Administrative panel of your store.

Manual integration
------------------

1. In your Shopify administration panel, go to
   **Settings** |rarr| **Checkout & Payment**.
2. Under **Order Processing** |rarr| **Additional Content & Scripts**,
   insert this code:

   .. include:: /partials/note_sample_code.rst

   .. include:: /samples/ecommerce/platform/shopify.rst

3. Click **Apply these settings**.
4. Verify your integration using :ref:`Verifying Integration <integration/verify>`.

|br|

.. |signup_link| raw:: html

  <a
    href="https://talkable.com/register?object_or_array"
    target="_blank"
  >
    https://talkable.com/register?object_or_array
  </a>

.. |example_link| raw:: html

  <span class="a">http://123test.myshopify.com</span>

.. container:: hidden

   .. toctree::

      Verifying Integration Instructions <verify>
