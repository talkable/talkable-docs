.. _integration/custom/validating_integration:
.. include:: /partials/common.rst

Validating the Integration
==========================

Visual Confirmation Note
........................

In order to see visual confirmation you must create or have existing
Talkable campaigns. Campaigns must be enabled for visual display (see
examples below on how to enable campaigns). Note that enabling campaigns
on production will allow your customers to see referral content. If you
want to limit visual display, or want to validate on your production
site without customers seeing visual display, then see the :ref:`Test Mode Display <integration/custom/validating_integration/test_mode_display>`
section below.

Validation Checklist
....................

1. Perform a test checkout.

   **Confirm Visual Result** You should see visual confirmation content
   on the checkout confirmation page if the post purchase campaign is enabled.

   **Confirm Data Result** Navigate to Reports > Purchases tab inside
   the Talkable platform to ensure all parameters that you’re using
   in the post purchase script are being passed. Data populates in real time.

2. Visit your Home Page.

   **Confirm Visual Result** You should see the floating Talkable Widget button.

3. Visit your Advocate Landing Page.

   **Confirm Visual Result** You should see visual confirmation content
   in the location where you placed the Talkable Container DIV.

4. Visit your Referral Dashboard Page.

   **Confirm Visual Result** You should see visual confirmation content
   in the location where you placed the Talkable Container DIV.

How to create or check for existing campaigns
.............................................

You’ll need to have a campaign of each type in order to validate
display.

There are 4 types:

1. :underline:`Post Purchase:` displays as a pop up after checkout

2. :underline:`Floating Widget:` displays as a floating widget button on your home
   page (and every page)

3. :underline:`Invite Standalone:` displays inline on your /invite advocate landing
   page

4. :underline:`Advocate Dashboard Standalone:` displays inline in your /referrals
   page

-  :underline:`How to create campaigns:` Here’s a screencast showing you how to
   quickly create all campaigns in less than 1 minute
   https://www.screencast.com/t/pVHTFoz9m1

-  :underline:`How to enable campaigns:` Here’s a screencast showing you how to
   enable campaigns (ignore any warnings for now and note the site
   display placement) https://screencast.com/t/brMNNqGDjD

.. _integration/custom/validating_integration/test_mode_display:

Test Mode Display
.................

After creating campaigns, while still in test mode before activating,
you can append a URL query string parameter to page where you want to
display a campaign in test mode which prevents anyone else from seeing
visual display. Note that each campaign has campaign tags under the
campaign name and you can reference these in the URL using the following
guidelines:

1. Floating widget on your homepage:

   `www.your-site.com?campaign_tags=test-popup`

2. Advocate Landing Page /invite:

   `www.your-site.com/invite?campaign_tags=test-invite`

3. Referral Dashboard:

   `www.your-site.com/referrals?campaign_tags=test-dashboard`

Note that campaigns must be newly created campaigns in test mode to be
eligible for test mode display. Use the following image as a visual
guideline:

.. figure:: /_static/img/campaigns-dashboard.jpg
   :alt: Campaigns
