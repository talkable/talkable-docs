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

1. Navigate to the App store:

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_1.png
      :alt: App store step 1

   .. image:: /_static/img/email_marketing_and_automation/app_store_step_2.png
      :alt: App store step 2

2. Choose a `Custom app` and click “Install”
3. Fill in `Endpoint URL` and `App name` fields, and enable the required actions.
4. Complete installation and enable the app:

   .. image:: /_static/img/email_marketing_and_automation/custom_app.png
      :alt: Custom App

Webhook Signature Verification
------------------------------

The `x-talkable-signature` header is included in each request and contains a signature that you have to verify to make sure the request is not compromised.

Talkable generates the signature using a `Base64 <https://en.wikipedia.org/wiki/Base64>`_ encoded hash-based message authentication code (`HMAC <https://en.wikipedia.org/wiki/HMAC>`_) with `SHA-256 <https://en.wikipedia.org/wiki/SHA-2>`_.

To verify the signature, you should complete the following steps:

1. Prepare the `payload_json` string

   Create a JSON string from the payload of the request.

2. Determine the expected signature
  
   - Compute an hex encoded **HMAC** with the **SHA256** hash function. Use the **Webhook security key** as a key, and use the `payload_json` string as a message.
   - Encode a computed hash with **Base64**

   Your Talkable **Webhook security key** can be found in the Webhook set up page by navigating to **Menu** then **Webhooks**.

   .. image:: /_static/img/menu_webhooks_screenshot.png
      :alt: Webhooks Menu Item

   .. raw:: html

      <hr>

   .. image:: /_static/img/webhook_secret_key.png
      :alt: Webhook Security Key

3. Compare the signatures

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
-----------------

Each action allows custom attributes to be included. You can see allowed interpolation variables by clicking `Show available variables` button:

.. image:: /_static/img/email_marketing_and_automation/variables.png
   :alt: Variables

Sync signups
............

This action automatically synchronizes all people whenever they sign up no matter if person opted in by email or phone number.

*Default payload:*

.. code-block:: JSON

   {
     "email": "person-9eb230f8d189fca9@talkable-sample.com",
     "email_optin": "true",
     "phone_number": "+12025551111",
     "phone_optin": "true"
   }

Sync email opt-ins
..................

This action automatically synchronizes all people whenever they sign up and opt in. Email signups without opt-in are not triggered by this action.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "email": "person-40728a5b940e3247@talkable-sample.com",
     "email_optin": "true"
   }

Sync phone opt-ins
..................

This action automatically synchronizes all people whenever they sign up and opt in for text messages. Signups without phone opt-in are not triggered by this action.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "email": "person-fa8e880e25bd47b3@talkable-sample.com",
     "phone_number": "+12025551111"
   }

Unsubscribe
...........

This action automatically synchronizes all people who unsubscribe from Talkable emails.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "email": "person-591542c54ff21a49@talkable-sample.com"
   }

Offer share
...........

This action automatically synchronizes all offer shares made by Advocates.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "email": "person-591542c54ff21a49@talkable-sample.com"
   }

Send reward
...........

This action automatically synchronizes reward information whenever a reward is issued.

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
.............

This action automatically sends coupons generated by Talkable to your system, allowing you to implement their applicability in your store. It is triggered whenever the quantity of available coupons drops below a Talkable threshold.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "coupon_code": "SAMPLE-COUPON-CODE",
     "coupon_discount_amount": "0.0"
   }

Event
.....

This action automatically synchronizes all registered Events and Purchases.

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

Referral Create
...............

This action automatically synchronizes all created referrals.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "campaign_id": "142",
     "referral_status": "in_progress",
     "advocate_email": "advocate@example.com",
     "friend_email": "friend@example.com"
   }

Referral status change
......................

This action automatically synchronizes all referral status changes.

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
.........................

This action sends information about a Friend when they attempt claiming a reward. The response from the Endpoint URL is checked to decide if a reward should be given. To reject unverified rewards, use `click_reward_verified` liquid variable in the incentive criteria.

**Note:** By default, the verification request times out at 1 second, and in that case the reward is considered verified.

*Default payload:*

.. code-block:: JSON

   {
     "email": "friend@example.com",
     "site_id": "1"
   }

Sync loyalty actions
....................

This action automatically synchronizes all loyalty actions performed by loyalty members.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "email": "loyalty@talkable.com"
   }

Sync loyalty tier transitions
.............................

This action automatically synchronizes all tier transitions of loyalty members whenever their tier changes.

*Default payload:*

.. code-block:: JSON

   {
     "site_id": "1",
     "email": "loyalty@talkable.com"
   }


Testing
-------

Testing Custom app actions can be accomplished with the help of Webhook Tester, an external service that tests your post-receive messages.

1. Visit `Webhook Tester <https://webhook.site/>`_ and click **Copy** to copy the URL you are given.
2. Open your Custom app.
3. Paste your Webhook Tester URL into **Endpoint URL** field and save.
4. Click **Send sample payload** near the action you want to test.

   .. image:: /_static/img/email_marketing_and_automation/send_sample_payload.png
      :alt: Send sample payload

5. After you finish the implementation on your site **change Webhook Tester URL
   to the live URL** in your Custom app.
6. Click **Send sample payload** to test action with Live URL.

Whitelisting Talkable IPs
-------------------------

In case your servers are behind firewall, you may need to whitelist Talkable IP
addresses so webhooks can be delivered. Pass list of these addresses to your network administrator:

.. hlist::
   :columns: 4

   .. include:: /partials/talkable_ip_list.rst
