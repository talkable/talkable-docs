.. _web_hooks/migration_to_custom_app:
.. include:: /partials/common.rst

.. meta::
   :description: Migration from Webhooks to Custom App.

Migration from Webhooks to Custom App
=====================================

The transition from Webhooks to :ref:`Custom App <email_marketing_and_automation/custom_app>` provides a more flexible, secure, and maintainable approach to integrating Talkable events with your internal systems. This guide outlines the key improvements, differences, and step-by-step instructions to help you successfully migrate to the new Custom App architecture.

How Custom App enhances or replaces Webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Webhooks are useful for triggering HTTP requests based on specific Talkable events, but they have limitations, such as:

- Each event type requires a separate webhook configuration.
- Security is managed via a shared security key, which may pose risks if not handled properly.
- Troubleshooting failed webhook deliveries can be complex due to limited error-handling options.

Custom App overcomes these limitations by providing:

- A single endpoint to manage multiple events, reducing setup complexity.
- Stronger authentication mechanisms with HMAC-SHA256 signature verification.
- Built-in testing tools for verifying event payloads before production use.
- Improved monitoring and logging for troubleshooting failed requests efficiently.

By migrating from webhooks to :ref:`Custom App <email_marketing_and_automation/custom_app>`, businesses can streamline their data integration processes, improve security, and reduce maintenance overhead.

Webhooks vs Custom App
~~~~~~~~~~~~~~~~~~~~~~

+--------------------+----------------------------+------------------------------------------+
| Feature            | Webhooks                   | Custom App                               |
+====================+============================+==========================================+
| **Flexibility**    | Fixed event-based triggers | Supports custom event handling           |
+--------------------+----------------------------+------------------------------------------+
| **Configuration**  | Requires manual endpoint   | Centralized configuration in Talkable UI |
|                    | setup per event            |                                          |
+--------------------+----------------------------+------------------------------------------+
| **Testing**        | Manual testing via         | Integrated testing and payload preview   |
|                    | Webhook Tester             |                                          |
+--------------------+----------------------------+------------------------------------------+
| **Error Handling** | Limited retry mechanism    | Advanced logging and troubleshooting     |
+--------------------+----------------------------+------------------------------------------+

Why Migrate to Custom App?
--------------------------

   - **Simplified Integration**: Manage all event handling in one place instead of setting up multiple webhooks.
   - **Enhanced Security**: :ref:`Custom App <email_marketing_and_automation/custom_app>` verifies request authenticity using HMAC-SHA256.
   - **Custom Payloads**: Define and modify event data dynamically without changing webhook implementations.

Transition from Webhooks to Custom App
--------------------------------------

To transition from webhooks to the :ref:`Custom App <email_marketing_and_automation/custom_app>`, follow these steps:

1. Review Current Webhooks

   - Identify the webhooks currently used in your system (e.g., Sync signups, Send reward, Referral status change).
   - Note the payload structure and data sent to each endpoint.

2. Install and Configure Custom App

   - Follow the Set Up instructions below to install and enable the Custom App.
   - Configure the same actions as your existing webhooks.

3. Verify Webhook Signature (if applicable)

   - Ensure your Custom App verifies the `x-talkable-signature` as described in the Webhook Signature Verification section.

4. Test Custom App Actions

   - Use the Webhook Tester to confirm that data is sent correctly.
   - Compare payloads from the Custom App to ensure they match what was previously received via webhooks.

5. Disable Legacy Webhooks

   - Once the Custom App is fully functional, deactivate the old webhooks in the Talkable settings.
   - Ensure all integrations are working smoothly before making the final switch.
