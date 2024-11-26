.. _email_marketing_and_automation/custom_app:
.. include:: /partials/common.rst

.. meta::
  :description: Custom App allows you to send Talkable data to a desired destination such as your site, ESP, CDP.

Custom App
==========

Custom App allows you to send Talkable data to a desired destination such as your site, ESP, CDP.
Talkable will send a request with data to the Custom App URL for each customer's event specified in the Custom App settings.

Set Up
------

1. Navigate into the App store:
  .. image:: /_static/img/email_marketing_and_automation/app_store_step_1.png
    :alt: App store step 1

  .. image:: /_static/img/email_marketing_and_automation/app_store_step_2.png
    :alt: App store step 2
2. Choose an `Custom app` and clicking “Install”
3. Fill in `Endpoint URL` and `App name` fields and enable actions you need.
4. Complete installation and enable the app:
  .. image:: /_static/img/email_marketing_and_automation/custom_app.png
      :alt: Custom App

Webhook Signature Verification
------------------------------

The `x-talkable-signature` header is included in each request and contains a signature that you have to verify to make sure the request is not compromised.

Talkable generates the signature using a `Base64 <https://en.wikipedia.org/wiki/Base64>`_ encoded hash-based message authentication code (`HMAC <https://en.wikipedia.org/wiki/HMAC>`_) with `SHA-256 <https://en.wikipedia.org/wiki/SHA-2>`_.

To verify the signature, you should complete the following steps:

**1. Prepare the** `payload_json` **string**

  Create a JSON string from the payload of the request.

**2. Determine the expected signature**

  - Compute an hex encoded **HMAC** with the **SHA256** hash function. Use the **Webhook security key** as a key, and use the `payload_json` string as a message.

  - Encode a computed hash with **Base64**

Your Talkable **Webhook security key** can be found in the Webhook set up page by navigating to **Menu** then **Webhooks**.

.. image:: /_static/img/menu_webhooks_screenshot.png
 :alt: Webhooks Menu Item

.. raw:: html

  <hr>

.. image:: /_static/img/webhook_secret_key.png
    :alt: Webhook Security Key

**3. Compare the signatures**

  Compare the signature from the header with your calculated signature.

**Examples:**

*Ruby:*

.. code-block:: ruby

    require 'base64'
    require 'openssl'
    require 'active_support/security_utils'

    WEBHOOK_SECRET_KEY = 'my_webhook_secret'

    def verify_webhook(data, header_signature)
      calculated_signature = Base64.strict_encode64(OpenSSL::HMAC.hexdigest('sha256', WEBHOOK_SECRET_KEY, data))
      ActiveSupport::SecurityUtils.secure_compare(calculated_signature, header_signature)
    end

*JavaScript:*

.. code-block:: javascript

  const crypto = require('crypto');

  const WEBHOOK_SECRET_KEY = 'my_webhook_secret';

  function verifyWebhook(data, headerSignature) {
    // Calculate HMAC
    const calculatedSignature = btoa(crypto
      .createHmac('sha256', WEBHOOK_SECRET_KEY)
      .update(data)
      .digest('hex')
    );

    return crypto.timingSafeEqual(
      Buffer.from(calculatedSignature, 'base64'),
      Buffer.from(headerSignature, 'base64')
    );
  }

Available actions
----------------
Each action allows custom attributes to be included. You can see allowed interpolation variables by clicking `Show available variables` button:

.. image:: /_static/img/email_marketing_and_automation/variables.png
  :alt: Send same payload

Referral Create
^^^^^^^^^^^^^^^
When referral has been created this action sends you information.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "campaign_id": "142",
    "referral_status": "in_progress",
    "advocate_email": "advocate@example.com",
    "friend_email": "friend@example.com"
  }

Sync signups
^^^^^^^^^^^^
This action automatically synchronizes all people whenever they sign up no matter if person opted in by email or phone number.

*Default payload:*

.. code-block:: JSON

  {
    "email": "person-9eb230f8d189fca9@talkable-sample.com",
    "email_optin": "true",
    "phone_number": "+12025551111",
    "phone_optin": "true"
  }

Sync email opt ins
^^^^^^^^^^^^^^^^^^
This action automatically synchronizes all people whenever they sign up and opt in. Email signups without opt in are not triggered by this action.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "email": "person-40728a5b940e3247@talkable-sample.com",
    "email_optin": "true"
  }

Sync phone opt ins
^^^^^^^^^^^^^^^^^^
This action automatically synchronizes all people whenever they sign up and opt in for text messages. Signups without phone opt in are not triggered by this action.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "email": "person-fa8e880e25bd47b3@talkable-sample.com",
    "phone_number": "+12025551111"
  }

Sync loyalty actions
^^^^^^^^^^^^^^^^^^^^
This action automatically synchronizes all loyalty members whenever they make a loyalty action.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "email": "loyalty@talkable.com"
  }

Sync loyalty tier transitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This action automatically synchronizes all loyalty members whenever their tier is changed.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "email": "loyalty@talkable.com"
  }

Unsubscribe
^^^^^^^^^^^
Whenever customers unsubscribe from Talkable emails they will also become unsubscribed in your ESP.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "email": "person-591542c54ff21a49@talkable-sample.com"
  }

Offer Share
^^^^^^^^^^^
Whenever a person shares the offer the share information will be sent to your ESP.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "email": "person-591542c54ff21a49@talkable-sample.com"
  }

Send reward
^^^^^^^^^^^
This action sends the reward information to your ESP.

*Default payload:*

.. code-block:: JSON

  {
    "description": "$5",
    "amount": "5.0",
    "coupon_code": "FR_NEW_5_OFF",
    "reason": "click",
    "site_id": "1"
  }

Create coupon
^^^^^^^^^^^^^
When the quantity of available coupons drops below a Talkable threshold this action sends you information.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "coupon_code": "SAMPLE-COUPON-CODE",
    "coupon_discount_amount": "0.0"
  }

Event
^^^^^
When Event or Purchase have been registered this actions sends you information.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "type": "Event",
    "created_at": "2024-11-25 00:00:00 -0800",
    "event_category": "public_event",
    "event_number": "183247241",
    "subtotal": "100.0",
    "currency_iso_code": "USD",
    "email": "advocate@example.com"
  }

Referral Status Change
^^^^^^^^^^^^^^^^^^^^^^
When referral has been created this action sends you information.

*Default payload:*

.. code-block:: JSON

  {
    "site_id": "1",
    "campaign_id": "142",
    "referral_status": "in_progress",
    "advocate_email": "advocate@example.com",
    "friend_email": "friend@example.com"
  }

Click reward verification
^^^^^^^^^^^^^^^^^^^^^^^^^
This action sends information about a Friend when they attempt claiming a reward. The response from the Endpoint URL is checked to decide if a reward should be given. To reject unverified rewards, use `click_reward_verified` liquid variable in the incentive criteria.

**Note:** By default, the verification request times out at 1 second, and in that case the reward is considered verified.

*Default payload:*

.. code-block:: JSON

  {
    "email": "friend@example.com",
    "site_id": "1"
  }


Testing
-------
Testing Custom app actions can be accomplished with the help of Webhook Tester, an external service that tests your post-receive messages.

1. Visit `Webhook Tester <https://webhook.site/>`_ and click **Copy** to copy the URL you are given.
2. Open your Custom app .
3. Paste your Webhook Tester URL into **Endpoint URL** field and save.
4. Click **Send sample payload** near the action you want to test.
  .. image:: /_static/img/email_marketing_and_automation/send_same_payload.png
      :alt: Send same payload
5. After you finish the implementation on your site **change Webhook Tester URL
   to the live URL** in your Custom app.
6. Click **Send sample payload** to test action with Live URL.

Whitelisting Talkable IPs
-------------------------

In case your servers are behind firewall, you may need to whitelist Talkable IP
addresses so webhooks can be delivered. Pass list of these addresses to your network administrator:

.. hlist::
   :columns: 4

   * 100.26.94.244
   * 18.207.91.200
   * 18.210.165.17
   * 18.232.203.127
   * 18.233.48.151
   * 184.73.206.68
   * 23.21.155.129
   * 3.222.226.72
   * 34.197.54.191
   * 34.226.253.236
   * 34.231.104.179
   * 34.232.247.192
   * 35.169.186.170
   * 35.171.77.58
   * 35.173.87.187
   * 44.217.136.252
   * 44.219.211.174
   * 50.16.143.102
   * 50.17.244.178
   * 52.204.148.18
   * 52.22.0.55
   * 52.6.41.1
   * 52.7.94.243
   * 54.164.128.44
   * 54.208.14.192
   * 54.86.208.153
   * 54.86.241.218
   * 54.91.51.228
