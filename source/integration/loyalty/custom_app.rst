.. _integration/loyalty/custom_app:
.. include:: /partials/common.rst

.. meta::
  :description: Learn how to use Custom app to receive data about loyalty events.

Custom App for Loyalty
======================

Talkable offers a Custom App that allows you to send Talkable data to an outside destination such as your site, ESP, or CDP.
The Custom App supports several actions. In the context of loyalty, the following actions might be useful:

* Sync loyalty actions
* Sync loyalty tier transitions

By default, the Custom App payload contains only `email` for loyalty-related actions.
However, it is recommended to modify the payload that will be sent when the app is triggered.

To set up a Custom App, go to **All site settings** → **App store** → **Custom app**.

Sync loyalty actions
~~~~~~~~~~~~~~~~~~~~

This feature sends Talkable data to the configured endpoint URL in the following cases:

* when a loyalty member earns points according to loyalty action configurations (eg. by subscribing to your newsletter);
* when a loyalty member earns or has points deducted due to a manual points adjustment (eg. made by a Customer Service representative);
* when a loyalty member exchanges (redeems) points for a coupon discount.

Liquid variables hints
----------------------

To determine which loyalty action triggered the Custom App, use `{{ action.identifier }}` liquid variable in the payload.

`{{ action.identifier }}` can have the following values:

* when loyalty member exchanges points for a coupon, the Action Identifier is *"redeem"*;
* when loyalty member gains or loses points due to a manual points adjustment, the Action Identifier is *"manual_adjustment"*;
* when loyalty member earns points according to loyalty action configurations, the Action Identifier varies based on the action configuration type:

   * *"optin"* for "Loyalty join";
   * *"event"* for "Purchase points" and "Event points";
   * *"referral"* for "Refer a friend";
   * for a custom type, the Identifier is taken straight from the action configuration "Identifier" field.

`{{ action.rule }}` contains details about the action configuration that is responsible for a particular points collection.

.. note::
  `{{ action.rule }}` is optional for *"manual_adjustment"* actions and always blank for *"redeem"* actions.

To see the full list of available variables, click "Show available variables" on the Custom App action configuration page.

Sync loyalty tier transitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This feature sends Talkable data to the configured endpoint URL once a loyalty member reaches a new tier.

Liquid variables hints
----------------------

`{{ tier_transition.reason }}` is either *"upgrade"* or *"downgrade"*, depending on the direction of the transition.

To see the full list of available variables, click "Show available variables" on the Custom App action configuration page.
