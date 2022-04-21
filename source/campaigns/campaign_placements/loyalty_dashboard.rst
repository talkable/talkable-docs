.. _campaigns/campaign_placements/loyalty_dashboard:
.. include:: /partials/common.rst

.. meta::
   :description: Loyalty Dashboard Placement is a Placement for Loyalty Campaigns.

Loyalty Dashboard Placement
===========================

You can create Loyalty Campaigns and place them on a standalone page on your site. With the Loyalty Dashboard Placement your Campaign will show up on any particular page of your site.

.. note::
   Customers need to be authenticated in order to view their Loyalty Dashboard. This means that `email` has to be present in the `authenticate_customer` call of the :ref:`Talkable Initialization Script <integration/loyalty/integration_components/initialization_script>`.

It is a good practice is to use `https://[your-site]/…/loyalty` URL for this new page and adding a link from any place that makes sense considering your website configuration. Most common uses are links in the user accounts section, or from the user accounts menu.

:ref:`Learn more about Placements <campaigns/campaign_placements>`

Integration instructions
------------------------

Loyalty Dashboard Placement doesn’t require any additional integration since integration `5.0.0`.
If you have already added Talkable to your main layout (completed General Integration
for Custom platform, or installed Shopify, Magento, or Salesforce Commerce Cloud extensions), then you are all done.
