.. _campaigns/campaign_placements/loyalty_widget:
.. include:: /partials/common.rst

.. meta::
  :description: Loyalty Widget Placement is a Placement for Loyalty Campaigns.

Loyalty Widget Placement
========================

Once you have your Loyalty Campaigns set up, you can use this placement to show to your customers a widget that will allow them to convert their points into a coupon that can be used on a checkout page.

.. note::
  If a customer is not signed in (`email` was not provided to the `authenticate_customer` call), the widget prompts them to join the loyalty program and provide the email manually.

It is a good practice to show this widget when your customers are about to check out so that they are able to convert their points to a coupon and apply it to the purchase.

:ref:`Learn more about Placements <campaigns/campaign_placements>`

Integration instructions
------------------------

Loyalty Widget Placement doesn’t require any additional integration since integration `5.0.0`.
If you have already added Talkable to your main layout (completed General Integration
for Custom platform, or installed Shopify, Magento, or Salesforce Commerce Cloud extensions), then you are all done.
