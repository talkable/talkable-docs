.. _integration/custom/overview:
.. include:: /partials/common.rst

Integration High-Level Overview
===============================

Integrating Talkable referral marketing platform to e-commerce sites is done in
a few quick steps by adding the below scripts to your site.

 .. note::

    All design and referral campaign setup is done inside the Talkable platform,
    then via ‘iframe’ referral campaign content is injected into the e-commerce
    site. The below scripts also handle the collection of specific necessary user
    data for Talkable to service the referral campaigns.

    Site-specific integration scripts are found after logging in at
    ``https://www.admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/integration/other``

.. raw:: html

   <h2>Integration Steps</h2>

1. Add the :ref:`Talkable Initialization Script <integration/custom/integration_components/initialization_script>`
   to your header or any template spanning every page. Surface variables for
   email and name if the user is logged in.

2. Add the :ref:`Talkable Post Purchase Script <integration/custom/integration_components/post_purchase_script>`
   to your checkout confirmation page to pass purchase details to Talkable for
   all purchases.

   Surface purchase detail variables as described in more detail in
   :ref:`Integration Components <integration/custom/integration_components>`.

 .. note::

    If a business has both one-time purchases and subscription transactions, or
    the business has a strictly subscription or SaaS model we recommend integrating
    the ‘Post Purchase’ through Events. :ref:`Learn more <advanced_features/events>`.

    Post Purchase step is the only step which changes for subscription business
    model integration - other steps remain the same.

3. To host the Invite Standalone campaign, create a new HTML page with standard
   header/footer. Best practice is to create this page on ``www.your-site.com/share``

   The Invite Standalone campaign will be your landing page to drive traffic to
   from marketing email and other onsite and offsite locations to refer friends.
   Copy & paste the Talkable container DIV element into the body as seen in
   :ref:`Integration Components <integration/custom/integration_components>`.

   .. code-block:: html

      <div id="talkable-offer"></div>

4. To host the Advocate Dashboard Standalone campaign, create an additional new
   HTML page under your user accounts section behind login.

   This Advocate Dashboard Standalone page allows Advocates to view referral
   details for the friends they’ve shared with. Copy & paste the Talkable container
   DIV element into the body as seen in
   :ref:`Integration Components <integration/custom/integration_components>`.

   .. code-block:: html

      <div id="talkable-offer"></div>
