.. _email_marketing_and_automation/yotpo:
.. include:: /partials/common.rst

.. meta::
  :description: Synchronize customer loyalty data from Yotpo Loyalty & Referrals platform with Talkable integration.

Yotpo
=====

Loyalty & Referrals
-------------------

Yotpo Loyalty & Referrals is a comprehensive customer loyalty platform that helps businesses create loyalty programs with points and rewards, manage VIP tiers, and track customer engagement.

The Talkable integration with Yotpo allows you to **leverage customer loyalty data to create personalized referral experiences** for your most valuable customers. The saved Yotpo loyalty data can be found in their custom properties.

Integration with Yotpo is done in Talkable with the corresponding App Store application.

This integration synchronizes data **FROM Yotpo TO Talkable**. It supports the following data to be synchronized:

* Customer loyalty points balance
* VIP tier status (Bronze, Silver, Gold, etc.)
* Tier change notifications (gained or lost status)

.. note::

  This is a **pull-only integration** - Talkable receives loyalty data from Yotpo but does not send any data back to Yotpo.

Here are the conditions when Talkable receives loyalty data:

1. Customer's loyalty points balance changes in Yotpo
2. Customer gains a VIP tier status in Yotpo
3. Customer loses a VIP tier status in Yotpo

The integration uses webhooks to automatically sync this data in real-time, ensuring your Talkable campaigns always have the most up-to-date loyalty information.

Loyalty data usage
~~~~~~~~~~~~~~~~~~

New data that synced from Yotpo can be accesed through person custom properties:

Available Yotpo loyalty variables:

* yotpo.points_earned
* yotpo.point_balance
* yotpo.total_redemptions
* yotpo.total_points_redeemed
* yotpo.vip_tier_name
* yotpo.successfull_referales
* yotpo.referrales_made_and_clicked
* yotpo.is_referred_by_other_customer

Integration Setup
~~~~~~~~~~~~~~~~~

Please use the following guide to start using the Yotpo integration:

1. Navigate into the App store:

   .. image:: /_static/img/email_marketing_and_automation/app_store_navigation.png
      :alt: App store navigation

2. Choose "Yotpo Loyalty & Referrals" by clicking "Install"

   .. image:: /_static/img/email_marketing_and_automation/yotpo.png
      :alt: Yotpo Loyalty & Referrals at App Store index page

3. You will be redirected to Yotpo for OAuth authorization:

   - Log into your Yotpo account
   - Click "Connect" to grant Talkable access to your loyalty data
   - You will be redirected back to Talkable automatically

4. Complete installation and enable the app:

   The integration will automatically configure with your Yotpo store credentials. Enable the "Sync Loyalty Data" action and then enable the app itself.

5. Test the integration by making a points adjustment in your Yotpo dashboard and verify the data appears in Talkable customer profiles.

.. include:: /partials/contact_us.rst
