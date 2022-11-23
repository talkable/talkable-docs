.. _integration/claim_by_name:
.. include:: /partials/common.rst

.. meta::
   :description: You can integrate Talkable Loyalty to e-commerce sites in a few quick steps.

Claim by Name (beta)
====================

Integrating Claim by Name campaign to e-commerce sites is done in a few quick steps.

Claim by name setup contains two campaigns that integrated with each other:

1. Advocate campaign - campagin where advocates can add username for their offer and share that with friends
2. Friend campaign - campaign which responsible for rewarding friends when they claim with advocate's username

.. raw:: html

   <h2>Integration</h2>

1. Initialize Talkable integration library.

   Make sure that you integration version is above 5.1.0 otherwise need to upgrade integration.

   Please |contact_us| if you have any questions.

.. raw:: html
   <h2>Setup</h2>

1. Create advocate campaign

   Use HTML editing mode in :ref:`Campaign Editor <campaigns/campaign_placements/loyalty_dashboard>` to add liquid sharing channel

   .. code-block:: liquid

      {% assign advocate_share_page_channel_personal_name = "advocate_share_page_channel_personal_name" | localize: trait: "boolean", default: "Enabled" %}

2. Create Claim by Name placement

   If there is no :ref:`Claim by Name Placement <campaigns/campaign_placements/claim_by_name>` please create one.

3. Create Claim by Name campaign

   .. note::

      Do not forget to change incentives.

4. Run campagins live
