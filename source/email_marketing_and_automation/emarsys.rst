.. _email_marketing_and_automation/emarsys:
.. include:: /partials/common.rst

.. meta::
  :description: With Hubspot app clients can synchronize emails that Talkable collected.

Emarsys
=======

With ESP apps clients can synchronize emails that Talkable acquires with their ESP. Here are the conditions when Talkable acquires emails:

1. Advocate signs up and opts in for Talkable marketing emails:

  .. image:: /_static/img/email_marketing_and_automation/subscribe.png
    :alt: Subscribe

2. A friend passes email gating and opts in for Talkable marketing emails:

  .. image:: /_static/img/email_marketing_and_automation/signup.png
    :alt: Signup

Each ESP application allows custom attributes to be included with each request. The following interpolation variables are allowed:

1. ``{{ person }}`` - a data object for either advocate or friend whenever they sign up or pass email gating and opt-in for marketing emails.
2. ``{{ ip }}`` – a data object from which IP address either a signup or email gating occurred.
3. ``{{ campaign }}`` – a data object with details about the campaign within which the email was captured.

.. image:: /_static/img/email_marketing_and_automation/variables.png
  :alt: Variables

Each variable is described in the “Available variables” sidebar and can be expanded to see all nested properties.

How to add a new app?
---------------------

Please use the following guide to start using an app you need:

1. Navigate into the App store:

  .. image:: /_static/img/email_marketing_and_automation/app_store_step_1.png
      :alt: App store step 1

  .. image:: /_static/img/email_marketing_and_automation/app_store_step_2.png
      :alt: App store step 2

2. Choose an app you need by clicking “Install”
3. Fill in all necessary fields. You can use tips on the right that instruct how to find all necessary credentials.
4. Complete installation and enable the app:

  .. image:: /_static/img/email_marketing_and_automation/hubspot.jpg
      :alt: hubspot

5. Test the app by pressing on the “Send sample payload” and then check if you are seeing a test request inside your ESP:

  .. image:: /_static/img/email_marketing_and_automation/send_same_payload.png
    :alt: Send same payload

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.
