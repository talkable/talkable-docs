.. _email_marketing_and_automation/dotdigital:
.. include:: partials/common.rst

.. meta::
   :description: With Dotdigital app clients can synchronize emails and phone numbers that Talkable collected, as well as manage email unsubscribes.

Dotdigital
==========

With the Dotdigital app, clients can synchronize emails and phone numbers that Talkable acquires with their Dotdigital platform. The integration supports:

- Email opt-ins from advocates and friends
- Phone number opt-ins for SMS marketing
- Email unsubscribe management

Here are the conditions when Talkable acquires emails and phone numbers:

1. Advocate signs up and opts in for Talkable marketing emails:

   .. image:: /_static/img/email_marketing_and_automation/signup_advocate.png
      :alt: Subscribe
      :scale: 50%

2. A friend passes email gating and opts in for Talkable marketing emails:

   .. image:: /_static/img/email_marketing_and_automation/signup_friend.png
      :alt: Signup
      :width: 430

3. Phone numbers are captured when users opt in for SMS communications during the referral process.

4. Email unsubscribes are automatically synchronized to ensure compliance with email preferences.

How to add a new app?
---------------------

Please use the following guide to start using the Dotdigital app:

1. Navigate into the App store:

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_1.png
      :alt: App store step 1
      :width: 595

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_2.png
      :alt: App store step 2
      :scale: 50%

2. Choose the Dotdigital app by clicking "Install"

3. Fill in all necessary fields. You can use tips on the right that instruct how to find all necessary credentials from your Dotdigital account:
   
   - API User Email
   - API User Password

   .. note::
      Regional API Endpoint will be filled by Talkable automatically, so it can be left blank.

   .. important::
      When creating an API user, make sure to select "Tiered" for the Rate limiting option.

4. Complete installation and enable the app:

   .. image:: /_static/img/email_marketing_and_automation/dotdigital.png
      :alt: dotdigital

Dotdigital application allows data fields to be included with each contact import. By default, Talkable sets the following data fields:

- ``FIRSTNAME``
- ``LASTNAME``

You can add custom data fields by modifying the payload of an app action.

.. image:: /_static/img/email_marketing_and_automation/dotdigital_payload.png
   :alt: dotdigital payload
   :scale: 50%

Talkable will add a prefix to each custom data field name

.. code-block:: JSON

   {
     "FAVORITE_COLOR": "{{ person.custom_properties.favorite_color }}", // Data field as defined in the payload
     "TKBL_FAVORITE_COLOR": "{{ person.custom_properties.favorite_color }}", // Data field sent to Dotdigital
   }

About Dotdigital
----------------

Dotdigital is a leading customer experience and data platform that helps marketing teams create personalized campaigns across email, SMS, social media, and other channels. With powerful automation tools and comprehensive analytics, Dotdigital enables brands to build lasting customer relationships and drive revenue growth.

For more information about Dotdigital's features and capabilities, visit `dotdigital.com <https://dotdigital.com/>`_.

.. include:: partials/contact_us.rst 
