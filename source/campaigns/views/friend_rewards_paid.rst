.. _campaigns/views/friend_rewards_paid:
.. include:: /partials/common.rst

.. _friend_rewards_paid:

Friend Reward Paid Email
------------------------

Main purpose of this email is to send a Reward via email, and remind about
it in the future. |br|
Email is triggered to a |friend| who passed Email Gating, and received Reward
(i.e. coupon code). |br|

The email will be sent once Talkable knows Friend’s email which they provides on the Friend Claim Page (such technique works great for email capturing). See :ref:`tutorials_email_gating` for more details.

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

.. code-block:: liquid

   Here is your {{ reward.incentive.description }} OFF deal you just claimed!
   Use it on any purchase by {{ valid_until }}
   Coupon code: {{ coupon_code }}
   <a href="{{ proceed_to_merchant_path }}">Shop now</a>

.. include:: /partials/developer_email_note.rst

.. raw:: html

   <h2>Email sending conditions</h2>

By default is sent immediately after the reward is created, but can be delayed by configuration.

Main email sending criteria (unable to change):

- The Email **will not** be sent only if all three conditions meet:

  1. Reward type is Click
  2. ‘Allow coupon in the Friend Share Email' is enabled inside Campaign Rules
  3. Friend Share Email is already sent

In all other scenarious the email will be sent immediately unless delayed by configuration.
