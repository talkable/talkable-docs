.. _campaigns/views/notifier_offers_claim:
.. include:: /partials/common.rst

Friend Claim Email
------------------

Main purpose of this email is to send a Reward via email, and remind about
it in the future. |br|
Email is triggered to a Friend who passed Email Gating and received Reward
(i.e. coupon code). |br|
Friend Claim Email is a good fit for email capture: reward Friend for
getting his email. See :ref:`tutorials_email_gating` for more details.

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
