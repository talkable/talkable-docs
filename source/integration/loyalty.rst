.. _integration/loyalty:
.. include:: /partials/common.rst

Loyalty Integration (beta)
==========================

.. meta::
   :description: You can integrate Talkable Loyalty to e-commerce sites in a few quick steps.

Integrating Talkable Loyalty to e-commerce sites is done in
a few quick steps by adding the below scripts to your site.

Integration
-----------

1. Initialize Talkable integration library.

   Add the :ref:`Talkable Initialization Script <integration/loyalty/integration_components/initialization_script>`
   to your header or any template spanning every page.

 .. note::

    Skip this step if you already have Talkable integrated on your site

2. Add Loyalty Dashboard.

   To host the Loyalty campaign, create a new HTML page with standard
   header/footer. Best practice is to create this page on ``www.your-site.com/loyalty``

   Copy Talkable container DIV element & paste it exactly where the Talkable iframe should be rendered, similarly to the referral standalone placement:

   .. code-block:: html

      <div id="talkable-loyalty"></div>

3. Add Redeem Widget.

   Copy Talkable container DIV element & paste it at the checkout
   exactly where the loyalty points redemption widget should render:

   .. code-block:: html

      <div id="talkable-loyalty"></div>

   It is recommended to add it above the discount field. Here is two examples:
   https://monosnap.com/file/WXfAIPEMUv7W7SoUixASmDvSFxNeiI

4. Define Loyalty points redemption batches.

   Each redemption batch determines progressive point redemption options based on the available points balance of the loyalty member. For example: 500 points would equal a discount coupon for $40 off, 1000 points would equal $100 and so on.

   For every redemption batch please generate single-use coupons for a certain discount amount ($40 off, $100 off, etc) and upload all coupons lists into Talkable loyalty coupon lists.

   It is recommended to upload 100K single-use coupons into every coupon list.

   https://monosnap.com/file/lXCK9bIey1XDaYDtbDJhSDuDZI9LLT

 .. note::

    All design and loyalty campaign setup is done inside the Talkable platform,
    then via ‘iframe’ loyalty campaign content is injected into the e-commerce
    site. The below scripts also handle the collection of specific necessary user
    data for Talkable to service the loyalty campaigns.

    ????? TODO ?????
    Site-specific integration scripts are found after logging in at
    ``https://www.admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/integration/other``

Requirements
------------

1. User accounts. The website must support user accounts since the loyalty program is only available to logged in users.

2. Single-use coupons. Every loyalty member will have a choice of redemption batches to redeem points for a one-time discount. When pressing a redeem button Talkable deducts points and issues a single-use coupon in return.

3. Ideally only purchases without tax & shipping cost should be passed to Talkable. This simplifies future refunds support as taxes and shipping cost are not refundable.
