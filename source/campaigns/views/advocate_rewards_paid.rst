.. _campaigns/views/notifier_rewards_paid:
.. include:: /partials/common.rst

.. meta::
   :description: Send email to your brand Advocate when their account has been credited or a partial refund has been issued.

Advocate Reward Paid Email
--------------------------

Email is triggered to an Advocate when Referral marked as ``Approved``. |br|
Let Advocate know their account has been credited or a partial refund has
been issued.

Frequently used Variables:

- To show Reward Coupon Code use ``{{ coupon_code }}``.
- Main |cta| should point to a merchant site to start shopping ``{{ proceed_to_merchant_path }}``.

|br|

.. image:: /_static/img/basics/advocate-reward-paid-email.png
   :alt: Advocate Reward Paid Email

|br|

.. code-block:: liquid

  Your credit code: {{ coupon_code }}
  <a href="http://merchant-site.com/products">Spend your credit</a>

.. include:: /partials/developer_email_note.rst

.. raw:: html

   <h2>Email sending conditions</h2>

By default is sent immediately after the reward status turns into `Paid`, but can be delayed by configuration. This View is available only for **Advocate Incentive** where |advocate| is rewarded after |friend| buys using their coupon code.

When the coupon list for Sharing or Signup incentive is empty at the moment of reward issuing, **Reward Paid Email** won't be sent.
We will try to reward the Advocate and send the email in the background for 60 days (with an increasing duration between retries) in case when coupon list is refiled.
