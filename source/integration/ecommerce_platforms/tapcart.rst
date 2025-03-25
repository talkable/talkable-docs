.. _integration/ecommerce_platforms/tapcart:
.. include:: /partials/common.rst

.. meta::
   :description: Learn how to integrate Talkable's referral program with your Tapcart mobile app.

Tapcart
==================

Overview
--------

The integration with Tapcart enables mobile app-based referral programs that leverage contact sharing to drive customer acquisition. This powerful combination allows your customers to easily share referral codes through their preferred communication channels, including SMS and social platforms.

Through Tapcart's Contact Sharing feature, you can integrate with referral code-based services like Talkable. Contact Sharing incentivizes consumers (via gift cards or discounts) to share referral-based offerings through their preferred social platform or directly with SMS contacts on their device. The integration focuses on utilizing key elements of social proof to increase consumer engagement and spending with your brand.

Requirements
------------

* Tapcart Enterprise subscription
* Talkable Enterprise account
* Valid API credentials from Talkable


Integration Setup
-----------------

Follow these steps to configure the integration:

1. Access Integration Settings
   
   * Navigate to your Tapcart Dashboard
   * Select the "Integrations" section
   * Locate and select "Talkable"

   .. note::
      You will see a configuration form with multiple fields to complete the integration setup.

2. Configure API Connection
   
   * Obtain your API Key from Talkable Dashboard (Account Settings → Basic Settings)
     
     .. note::
        The API Key can be found in the Basic Settings section of your Account Settings page in Talkable.

   * Enter your Site Slug (found in the URL of your Talkable Dashboard)
     
     .. note::
        Look at your Talkable Dashboard URL - the Site Slug is the unique identifier in the URL path.

   * Specify the Campaign Tag (ensure it's unique to your Tapcart campaign)
     
     .. note::
        This tag should be used exclusively for your Tapcart campaign to ensure proper tracking.

3. Customize User Experience
   
   * Upload a Promotional Banner (used to inspire customers to access this feature)
   * Create Onboarding Text (explains the referral process and applicable rewards)
   * Compose a default Share Message (pre-populated message for texts/emails, editable by customers)
   * Set up Share Intent text (brief subheader shown when generating share links)
   * Configure Automatic Presentation settings (triggers after purchase or second app session)

4. Save and Enable
   
   * Once all fields are completed, select 'Save & Enable' to complete the setup

.. tip::
   To maximize visibility, add the referral program to your app's menu navigation! Learn how to modify your app's menu in the Tapcart documentation.

Customer Journey
----------------

Access Methods
~~~~~~~~~~~~~~

Users can access the referral program through multiple entry points:

* Account page within the app
* Menu navigation
* Automatic presentation after purchase
* Second app session prompt

Sharing Process
~~~~~~~~~~~~~~~

**Contact List Method:**

1. Grant contact access permission to allow the app to access the device's contact list
2. Select contacts for sharing from the device's contact list
3. Send referral messages to selected contacts

**Alternative Sharing:**

1. Choose sharing platform (SMS, social media, etc.)
2. Review and customize pre-populated message (customers can edit before sending)
3. Send referral invitation through the chosen platform

Referral Redemption
~~~~~~~~~~~~~~~~~~~

1. Recipients click the shared referral link
2. Enter email address to receive discount code
3. Apply code during purchase
4. Original referrer receives credit for the conversion

The integration automatically tracks all referral activities and properly attributes conversions to the referring users.

Support and Resources
---------------------

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.

.. note::
   The integration automatically tracks referral conversions and attributes them to the appropriate users.

.. tip::
   Customize your menu navigation to prominently feature the referral program for maximum engagement.

