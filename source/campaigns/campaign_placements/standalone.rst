.. _campaigns/campaign_placements/standalone:
.. include:: /partials/common.rst

Standalone Placement
====================

You can create Campaigns of different types (Invite, Dashboard, Leaderboard, etc) and place them on a standalone page
on your site.
With the Standalone placement your Campaign will show up on any particular page of your site.
An Advocate does not need to make a purchase to become eligible to share from such Campaigns.

Good practice is to use `https://[your-site]/.../share` URL for this new page and link it from the main site navigation.

:ref:`Learn more about Placements <campaigns/campaign_placements>`

Flow
----

.. image:: /_static/img/campaign_placements/standalone.png
   :alt: Talkable campaign flow — Standalone placement
   :class: is-minimal

Integration instructions
------------------------

Instructions slightly vary based on your site platform.

Shopify Platform
----------------

#. **Install Talkable extension.** If you haven’t done it before for other campaigns on your site,
   then go to Integration Guide `https://admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/integration` and install
   Shopify Talkable extension. Check the integration status with “Verify Integration” button.

#. **Prepare Page.** Once installed Talkable extension creates a new page "`[your-site] referral program`".
   The address of this page is `https://[your-site]/pages/share` by default.
   Make sure this page is accessible to your customers from the navigation menu of your site, you can configure that in the
   Shopify site settings.
   |br|
   |br|
   The page template already has a required container
   `<div id="talkable-offer"></div>`
   placed between Header and Footer of your page which makes your customers think this is a site feature built in-house.
   |br|
   |br|
   If you want to change the place where to show Standalone Talkable campaign on your site, you can do that by changing the
   place of Talkable container on the page.
   |br|
   Also you can create other pages based on `page.talkable` template and use them for other Standalone Campaigns.

#. **Configure Campaign and Placement.** Create a new Campaign with Standalone type of Placement,
   configure it and launch. It will automatically attach to the placement with
   |br|
   `https://[your-site]/pages/share`
   URL address and so, show up to your customers there.

   |

Magento Platform
----------------

#. **Install Talkable extension.** If you haven’t done it already, then go to Integration Guide
   `https://admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/integration` and follow instructions.
   Check the integration status with “Verify Integration” button.

#. **Enable in Talkable extension.** By default Talkable extension creates two pages on your site `https://[your-site]/share`
   and on `https://[your-site]/customer/dashboard` that are suitable for Standalone Campaigns.
   Make sure the Invite and Dashboard type of Campaigns are enabled in the Talkable extension settings on your
   Magento Admin Panel.

#. **Configure Campaign and Placement.** Create a new Campaign with Standalone type of Placement,
   configure it and launch. It will automatically attach to the placement with |br| `https://[your-site]/share` URL address
   and so, show up to your customers there.
   |br|
   For Advocate Dashboard type of Campaigns you could use a separate default
   “Standalone Dashboard” Placement that matches `https://[your-site]/customer/dashboard` URL on your site.
   |br|
   For this or another change you need to visit:
   |br|
   `https://admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/placements`
   page and re-attach the Campaigns from one to another Placement.

   |

Custom Platform
---------------

#. **Add Talkable.** If you haven’t done it already, then go to Integration Guide
   `https://admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/integration`, copy the prepared
   Talkable script and add to your site main layout. The script already has `<YOUR-TALKABLE-SITE-ID>`,
   so it is ready to use. Check the integration status with “Verify Integration” button.

#. **Prepare Page.** Create a page or select the existing one on your site where the customers can access
   the Campaign offers. Best practice is `https://[your-site]/share` URL address.
   Then define where on this page the Standalone Campaign views should show up in order to look naturally,
   usually it is somewhere in between the page Header and Footer, and add a script from your
   |br|
   `https://admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/integration`
   |br|
   page. Make sure this page is accessible to your customers from the navigation menu.

#. **Configure Campaign and Placement.** Create a new Campaign with Standalone type of Placement,
   configure it and launch. It will automatically attach to the default Standalone Placement that has
   `https://[your-site]/share` URL address and so, show up to your customers there.
   |br|
   |br|
   If you need to change or reconfigure which Campaigns are shown on which URLs then
   visit `https://admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/placements` page.

   |
