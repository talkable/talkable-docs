.. _campaigns/campaign_placements/post_purchase:
.. include:: /partials/common.rst

Post Purchase Placement
=======================

You can create Campaigns of different types (Invite, Dashboard, Leaderboard, etc)
and show them to your customers on cart checkout. With the Post Purchase placement your Campaign will
show up automatically as a popup once the customer made a successful purchase on your site.

:ref:`Learn more about Placements <campaigns/campaign_placements>`

Flow
----

.. image:: /_static/img/campaign_placements/pp.png
   :alt: Talkable campaign flow — Post Purchase placement,
   :class: is-minimal

Integration instructions
------------------------

Instructions slightly vary based on your site platform.

Shopify Platform
----------------

#. **Install Talkable extension.** If you haven’t done it before for other campaigns on your site,
   then go to Integration Guide `https://www.talkable.com/sites/[YOUR-TALKABLE-SITE-ID]/integration` and install
   Shopify Talkable extension. Check the integration status with “Verify Integration” button.

#. **Configure Campaign and Placement.** Create a new Campaign with Post Purchase type of Placement,
   configure it and launch. It will be automatically attached to the Post Purchase Placement and so,
   show up to your customers every time they purchase successfully on your site.

   |

Magento Platform
----------------

#. **Install Talkable extension.** If you haven’t done it already, then go to Integration Guide
   `https://www.talkable.com/sites/[YOUR-TALKABLE-SITE-ID]/integration` and follow instructions. Check the integration status with “Verify Integration” button.

#. **Enable in Talkable extension.** Talkable extension is integrated on your Magento site
   Purchase Success page, so you don’t need to do anything in addition.
   Make sure the Post Purchase type of Campaigns is enabled in the Talkable extension settings in your Magento Admin Panel.

#. **Configure Campaign and Placement.** Create a new Campaign with Post Purchase type of Placement,
   configure it and launch. It will be automatically attached to the Post Purchase Placement and so,
   show up to your customers every time they purchase successfully on your site.

   |

Custom Platform
---------------

#. **Add Talkable.** If you haven’t done it already, then go to Integration Guide
   `https://www.talkable.com/sites/[YOUR-TALKABLE-SITE-ID]/integration`
   and add Talkable to your main site layout by following the instructions on **General Integration** tab.
   Check the integration status with “Verify Integration” button.


#. **Add Post Purchase Script.**
   Go to `https://www.talkable.com/sites/[YOUR-TALKABLE-SITE-ID]/integration` page, copy the
   pregenerated Talkable script and add it to your order confirmation page.
   At this point you need to pass all the order related properties such as order number, subtotal, coupon code, etc.

#. **Configure Campaign and Placement.**
   Create a new Campaign with Post Purchase type of Placement and launch it.
   It will be automatically attached to its Post Purchase Placement that triggers a
   Campaign on the order confirmation page.
   |br|
   If you need to change or reconfigure which Campaigns are shown on which URLs then visit
   `https://www.talkable.com/sites/[YOUR-TALKABLE-SITE-ID]/placements` page.

   |
