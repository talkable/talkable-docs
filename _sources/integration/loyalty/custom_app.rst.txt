.. _integration/loyalty/custom_app:
.. include:: /partials/common.rst

.. meta::
   :description: Learn how to use Custom app to receive data about loyalty events.

Custom App for Loyalty
======================

Talkable offers a Custom app that allows sending Talkable data to the desired destinations such as your site, ESP, CDP.
The Custom App supports several actions. In the context of loyalty, the following might be useful:

* Sync loyalty actions
* Sync loyalty tier transitions

To make the app useful, it is recommended to modify the payload that will be sent when the app is triggered.
By default, Custom app payload contains only `email` for loyalty-related actions.

To set up a Custom app, go to **All site settings** → **App store** → **Custom app**.

Sync loyalty actions
~~~~~~~~~~~~~~~~~~~~

This action sends Talkable data to the configured endpoint URL in the following cases:

* loyalty member collects points according to loyalty action configurations;
* loyalty member gains or loses points due to a manual points adjustment;
* loyalty member exchanges (redeems) points for a coupon discount.

Liquid variables hints
----------------------

To determine which loyalty action triggered the Custom app, use `{{ action.identifier }}` liquid variable in the payload.

`{{ action.identifier }}` can have the following values:

* when loyalty member exchanges points for a coupon, it's always *"redeem"*;
* when loyalty member gains or loses points due to a manual points adjustment, it's always *"manual_adjustment"*;
* when loyalty member earns points according to loyalty action configurations, it can vary based on the action configuration type:

   * *"optin"* for "Loyalty join";
   * *"event"* for "Purchase points" and "Event points";
   * *"referral"* for "Refer a friend";
   * for a custom type it is taken straight from the action configuration "Identifier" field.

`{{ action.rule }}` contains details about the action configuration that is responsible for a particular points collection.

.. note::
   `{{ action.rule }}` is optional for *"manual_adjustment"* actions and always blank for *"redeem"* actions.

To see the full list of available variables, click "Show available variables" on Custom app action configuration page.

Sync loyalty tier transitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This action sends Talkable data to the configured endpoint URL once a loyalty member reaches a new tier.

Liquid variables hints
----------------------

`{{ tier_transition.reason }}` is either *"upgrade"* or *"downgrade"*, depending on the direction of the transition.

To see the full list of available variables, click "Show available variables" on Custom app action configuration page.
