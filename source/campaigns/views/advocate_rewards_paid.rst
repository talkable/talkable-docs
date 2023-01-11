.. _campaigns/views/notifier_rewards_paid:
.. include:: /partials/common.rst

.. meta::
   :description: Send email to your brand Advocate when their account has been credited or a partial refund has been issued.

Advocate Reward Paid Email
--------------------------

Let Advocates know they have been rewarded, or a partial refund has been issued. |br|
The email is triggered and sent when an Advocate receives a reward. It can be a Signup, Share, or Referral reward (when Referral is marked as ``Approved``).
All trigger conditions are configured via :ref:`incentive_criteria`.

Advocate Reward Paid Email template could be customised via :ref:`editor`.

Frequently used Variables:

- To show Reward Coupon Code use ``{{ coupon_code }}``.
- Main |cta| should point to a merchant site to start shopping ``{{ proceed_to_advocate_destination_url }}``.

.. image:: /_static/img/basics/advocate-reward-paid-email-v2.png
   :alt: Advocate Reward Paid Email

.. include:: /partials/developer_email_note.rst

.. raw:: html

   <h2>Email sending conditions</h2>

By default is sent immediately after the reward status turns into `Paid`, but can be delayed by configuration. |br|

When the coupon list for Sharing or Signup incentive is empty at the moment of reward issuing, **Reward Paid Email** will not be sent.
We will try to reward the Advocate and send the email in the background for 60 days (with an increasing duration between retries) in the case of coupon list fulfillment.