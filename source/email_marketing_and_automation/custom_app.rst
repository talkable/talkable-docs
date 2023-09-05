.. _email_marketing_and_automation/custom_app:
.. include:: /partials/common.rst

.. meta::
  :description: Custom App allows you to send Talkable data to a desired destination such as your site, ESP, CDP.

Custom App
=========

Custom App allows you to send Talkable data to a desired destination such as your site, ESP, CDP.
Talkable will send a request with data to the Custom App URL for each customer's event specified in the Custom App settings.

Webhook Signature Verification
------------------------------

The `x-talkable-signature` header included in each signed event contains signature that you must verify.

Talkable generates signatures using a `Base64 <https://en.wikipedia.org/wiki/Base64>`_ encoded hash-based message authentication code (`HMAC <https://en.wikipedia.org/wiki/HMAC>`_) with `SHA-256 <https://en.wikipedia.org/wiki/SHA-2>`_.

To verify signature, you must complete the following steps:

**1. Prepare the** `payload_json` **string**

  Create a JSON string from the payload of request.

**2. Determine the expected signature**

  - Compute an hex encoded **HMAC** with the **SHA256** hash function. Use the **Webhook security key** as a key, and use the `payload_json` string as a message.

  - Encode a computed hash with **Base64**

Your Talkable **Webhook security key** can be found in the Webhook set up page by navigating to **Menu** then **Webhooks**.

.. image:: /_static/img/menu_webhooks_screenshot.png
 :alt: Webhooks Menu Item

.. raw:: html

  <hr>

.. image:: /_static/img/webhook_secret_key.png
    :alt: Webhook security key

**3. Compare the signatures**

  Compare the signature from the header with your calculated signature.

Examples:
.........

**Ruby:**

.. code-block:: ruby

    require 'base64'
    require 'openssl'
    require 'active_support/security_utils'

    WEBHOOK_SECRET_KEY = 'my_webhook_secret'

    def verify_webhook(data, header_signature)
      calculated_signature = Base64.strict_encode64(OpenSSL::HMAC.hexdigest('sha256', WEBHOOK_SECRET_KEY, data))
      ActiveSupport::SecurityUtils.secure_compare(calculated_signature, header_signature)
    end

**JavaScript:**

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


