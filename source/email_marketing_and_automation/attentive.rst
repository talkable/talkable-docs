.. _email_marketing_and_automation/attentive:
.. include:: /partials/common.rst

.. meta::
   :description: With Attentive app clients can synchronize mobile numbers that Talkable collected.

Attentive
=========

.. tip::

   This is a custom integration that can be implemented with extra effort. If you wish to integrate this vendor, please contact your Customer Success Manager to apply it to your campaigns.

Talkable converts customers into brand advocates by enabling trusted, word-of-mouth referrals. Attentive connects with customers on the most engaging channel: SMS.

Together, Talkable and Attentive drive personalized brand engagement and the **acquisition of high-value, loyal customers.**

**Use cases:**

1. Capture phone numbers through Talkable to seamlessly grow your SMS subscriber list. The integration automatically passes these numbers to your Attentive messaging flow.

2. Promote refer-a-friend to your SMS list to facilitate increased sharing. Mobile messages have a 99% open rate.

   **Sample SMS triggered post-purchase:**

     Thanks for your recent purchase! A referral from you would mean a lot to us! Share ‘Brand name’ with friends & we’ll share $10 with you 😃

3. Trigger referral messages through SMS for increased engagement.

   For example, send advocates their referral reward via text to increase redemptions and repeat shoppers.

App Store
---------

Integration with Attentive is done in Talkable with the corresponding App store application.

It supports next data to be synchronized from Talkable to Attentive:

* Email and phone opt ins
* Reward coupons

.. note::

   For phone and phone opt-in synchronization, corresponding attributes should be configured in a Talkable campaign: :ref:`Phone number gating <advanced_features/phone_number_gating>`

Here are the conditions when Talkable acquires phone numbers:

1. Advocate signs up, provides phone number and opts in for Talkable marketing text messages:

   .. image:: /_static/img/email_marketing_and_automation/signup_advocate_sms.png
      :alt: Subscribe
      :scale: 50%

2. Friend passes phone gating and opts in for Talkable marketing text messages:

   .. image:: /_static/img/email_marketing_and_automation/signup_friend_sms.png
      :alt: Signup
      :width: 337

Each ESP application allows custom attributes to be included with each request. The following interpolation variables are allowed:

1. ``{{ person }}`` - a data object for either Advocate or Friend whenever they sign up or pass phone gating and opt-in for marketing text messages.

2. ``{{ ip }}`` – a data object from which IP address either a signup or phone gating occurred.

3. ``{{ campaign }}`` – a data object with details about the campaign within which the phone was captured.

.. image:: /_static/img/email_marketing_and_automation/variables.png
   :alt: Variables
   :scale: 50%

Each variable is described in the “Available variables” sidebar and can be expanded to see all nested properties.

How to add a new app?
---------------------

Please use the following guide to start using an app you need:

1. Navigate into the App store:

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_1.png
      :alt: App store step 1
      :width: 595

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_2.png
      :alt: App store step 2
      :scale: 50%

2. Choose an app you need by clicking “Install”

3. Fill in all necessary fields. You can use tips on the right that instruct how to find all necessary credentials.

4. Complete installation and enable the app:

   .. image:: /_static/img/email_marketing_and_automation/attentive_activate.png
      :alt: Attentive

5. Test the app by pressing on the “Send sample payload” and then check if you are seeing a test request inside your ESP:

   .. image:: /_static/img/email_marketing_and_automation/send_sample_payload.png
      :alt: Send sample payload
      :scale: 50%

.. include:: /partials/contact_us.rst
