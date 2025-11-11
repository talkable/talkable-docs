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

Integration Setup
-----------------

Please use the following guide to start using the Yotpo integration:

1. Navigate into the App store:

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_1.png
      :alt: App store step 1
      :width: 595

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_2.png
      :alt: App store step 2
      :scale: 50%

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

Loyalty data usage
------------------

New data that synced from Yotpo can be accessed through person custom properties:

Available Yotpo loyalty variables:

* yotpo.points_earned
* yotpo.points_balance
* yotpo.vip_tier_name

Tracking Loyalty-Driven Referral Performance
............................................

You can track referral performance using the provided Yotpo Loyalty variables to identify which customers generate the most referrals and use these insights to optimize your campaigns.
These custom properties can be viewed within the **People** report details:

1. Navigate to the **People** report, select the desired date range and filters, generate the report, and click the **Details** link for the customer you're interested in.

   .. image:: /_static/img/email_marketing_and_automation/yotpo_people_report_index.png
      :alt: Yotpo Loyalty & Referrals person custom properties in People report

2. Scroll to the **Custom Properties** section and review the following values:

   .. image:: /_static/img/email_marketing_and_automation/yotpo_people_report_details.png
      :alt: Yotpo Loyalty & Referrals person custom properties in People report

Exclusive Referral Rewards for customers
........................................

Yotpo custom properties allow you to configure referral rewards that vary by their values.
Lets create better reward for **Gold Tier** advocates in the example below:

1. Open the **Rules** page of the desired campaign and navigate to the **Incentives** section.

   .. image:: /_static/img/email_marketing_and_automation/yotpo_incentive_index.png
      :alt: Using Yotpo Loyalty & Referrals person custom properties in Incentive criteria

2. Create a new **Advocate Referral Incentive** with the desired reward amount.

   .. image:: /_static/img/email_marketing_and_automation/yotpo_incentive_create.png
      :alt: Using Yotpo Loyalty & Referrals person custom properties in Incentive criteria

3. Go to **Advanced Settings**, and fill in **Incentive Criteria** fields with the following code:

   .. code-block:: liquid
      :force:

      {% if advocate_info.custom_properties.yotpo.vip_tier_name == "Gold Tier" %}
        true
      {% else %}
        Should have Gold Tier
      {% endif %}

   .. image:: /_static/img/email_marketing_and_automation/yotpo_incentive_criteria.png
      :alt: Using Yotpo Loyalty & Referrals person custom properties in Incentive criteria

4. Learn more about incentive criteria on :ref:`Incentive Criteria <campaigns/tutorials/incentive_criteria>` page.

Yotpo Points in Talkable Wallet
...............................

You can use Yotpo custom properties to display customer's loyalty points alongside their referral rewards directly in the Talkable Wallet.
This gives customers a unified view of both referral and loyalty activity in one place.

In the example below, we'll show how to display the customer's Yotpo points balance in the header of the Apple Wallet pass:

1. Navigate to the **Editor** of the desired campaign:

   .. image:: /_static/img/email_marketing_and_automation/yotpo_wallet_editor.png
      :alt: Using Yotpo Loyalty & Referrals person custom properties in campaign easy editor

2. Open the **Talkable wallet for iPhone** view, on the right part of the screen you can see Apple pass preview:

   .. image:: /_static/img/email_marketing_and_automation/yotpo_wallet_view.png
      :alt: Using Yotpo Loyalty & Referrals person custom properties in campaign easy editor

3. Update the **Apple Wallet header field label** localization with **REFERRALS | POINTS**, and set the **Apple Wallet header field value** to the following code:

   .. code-block:: liquid
      :force:

      {{ referrals_count_by_status.total | default: 0 }} | {{  custom_properties.yotpo.point_balance | default: 0 }}

4. In the preview, you'll see that the wallet header now displays Points in addition to Referrals:

   .. image:: /_static/img/email_marketing_and_automation/yotpo_wallet_points.png
      :alt: Using Yotpo Loyalty & Referrals person custom properties in campaign easy editor

5. Learn more about the campaign editor on the :ref:`Editor <campaigns/editor>` page.

.. include:: /partials/contact_us.rst
