.. _campaigns/views/notifier_rewards_confirmation:
.. include:: /partials/common.rst

.. _notifier_rewards_confirmation:

Advocate/Friend Reward Confirmation Email
-----------------------------------------

Main purpose of this email is to send a Reward via email, and remind about
it in the future. |br|
Email is triggered to a |advocate| or a |friend| who passed Email Gating, and received Reward
(i.e. coupon code). |br|

Use Email sending condition to differentiate |advocate| from |friend| email.

Here is an example of a Friend Reward Confirmation Email:

.. raw:: html

  <pre>{% if reward.incentive.identifier == 'click' %}
    true
  {% endif %}</pre>

.. image:: /_static/img/campaign/friend_confirmation_sending_criteria.png

The email will be sent once Talkable knows Friend's email which they provides on the Friend Claim Page (such technique works great for email capturing). See :ref:`tutorials_email_gating` for more details.

You can see your Incentive identifier inside Campaign Rules:

.. image:: /_static/img/campaign/incentive_identifier.png

Frequently used Variables:

- Main |cta| should point to a merchant site to start shopping
  ``{{ proceed_to_merchant_path }}``.
- To show coupon code use ``{{ coupon_code }}``.
- To show expiration date use ``{{ valid_until }}``.
  :ref:`Formatting options <liquid_filter_format_date>`.

|br|

.. image:: /_static/img/basics/friend-claim-email.png
   :alt: Friend Claim Email

|br|

.. code-block:: html

   Here is your {{ incentives.click.description }} OFF deal you just claimed!
   Use it on any purchase by {{ valid_until }}
   Coupon code: {{ coupon_code }}
   <a href="{{ proceed_to_merchant_path }}">Shop now</a>

.. include:: /partials/developer_email_note.rst

.. raw:: html

   <h2>Email sending conditions for Advocate</h2>

By default is sent immediately after the reward is created, but can be delayed by configuration.

.. raw:: html

   <h2>Email sending conditions for Friend</h2>

Main email sending criteria (unable to change):

- The Email **will not** be sent only if all three conditions meet:

  1. Reward type is Click
  2. ‘Allow coupon in the Friend Share Email' is enabled inside Campaign Rules
  3. Friend Share Email is already sent

In all other scenarious the email will be sent immediately unless delayed by configuration.

