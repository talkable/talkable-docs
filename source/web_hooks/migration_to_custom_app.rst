.. _web_hooks/migration_to_custom_app:
.. include:: partials/common.rst

.. meta::
   :description: Migration from Webhooks to Custom App.

Migration from Webhooks to Custom App
=====================================

The transition from Webhooks to :ref:`Custom App <email_marketing_and_automation/custom_app>` provides a more flexible approach to integrate Talkable events with your systems. This guide outlines the key improvements, differences, and step-by-step instructions to help you successfully migrate to the new Custom App architecture.

How Custom App enhances or replaces Webhooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Webhooks are useful for triggering HTTP requests based on specific Talkable events, but they have limitations, such as:

- Each event type requires a separate webhook configuration.
- Only one webhook can be set per event.
- Payload customization is not supported.

Custom App overcomes these limitations by providing:

- A single endpoint to manage multiple events, reducing setup complexity.
- Built-in testing tools for verifying event payloads before production use.
- Customizable payload with a wide range of data variables.
- Conditional execution with Liquid criteria for each event.

By migrating from webhooks to :ref:`Custom App <email_marketing_and_automation/custom_app>`, businesses can streamline their data integration processes and reduce maintenance overhead.

Webhooks vs Custom App
~~~~~~~~~~~~~~~~~~~~~~

+---------------------------+------------------------------+------------------------------------------+
| Feature                   | Webhooks                     | Custom App                               |
+===========================+==============================+==========================================+
| **Flexibility**           | Fixed event-based triggers   | Supports custom event handling           |
+---------------------------+------------------------------+------------------------------------------+
| **Configuration**         | Requires manual endpoint     | Centralized configuration in Talkable UI |
|                           | setup per event              |                                          |
+---------------------------+------------------------------+------------------------------------------+
| **Customizable Payload**  | Limited or manual payload    | Flexible payload configuration via UI    |
|                           | manipulation                 |                                          |
+---------------------------+------------------------------+------------------------------------------+
| **Conditional Execution** | Not supported out of the box | Allows event triggers based on custom    |
|                           |                              | rules and conditions                     |
+---------------------------+------------------------------+------------------------------------------+

Transition from Webhooks to Custom App
--------------------------------------

To transition from webhooks to the :ref:`Custom App <email_marketing_and_automation/custom_app>`, follow these steps:

1. Review Current Webhooks

   - Identify the webhooks currently used in your system (e.g., Sync signups, Send reward, Referral status change).
   - Note the payload structure and data sent to each endpoint.

2. Install and Configure Custom App

   - Follow the Set Up instructions below to install and enable the Custom App.
   - Configure the same actions as your existing webhooks.

3. Test Custom App Actions

   - Use the Webhook Tester to confirm that data is sent correctly.
   - Compare payloads from the Custom App to ensure they match what was previously received via webhooks.

4. Disable Legacy Webhooks

   - Once the Custom App is fully functional, deactivate the old webhooks in the Talkable settings.
   - Ensure all integrations are working smoothly before making the final switch.
