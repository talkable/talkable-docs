.. _campaigns/views/notifier_offers_email:
.. include:: partials/common.rst

.. meta::
   :description: Send email to tell your Advocate what your referral program is about. Motivate them to share your offer.

Advocate Offer Email
--------------------

Email is triggered to an |advocate| on sign up. Explain the value proposition
and encourage |advocate| to share using the buttons.

- For Standalone Campaign it triggers when |advocate| signs up.
- For Post-Checkout Campaign it triggers when |advocate| makes store purchase.

Main |cta| should point to an Advocate Signup/Share Page — ``{{ share_page_url }}``.

|br|

.. image:: _static/img/basics/advocate-offer-email.png

|br|

.. include:: partials/developer_email_note.rst

.. raw:: html

   <h2>Email sending conditions</h2>

By default is sent immediately after the offer is created, but can be delayed by configuration.

1. Talkable creates an offer based on the following criteria:

   1. Purchase creation
   2. Affiliate member signup. |advocate| can sign up manually by entering their email, or their email is passed via JS integration (or URL). For example, a customer signs up to refer-a-friend on a /share page. This triggers an affiliate member signup.

2. Main email sending criteria (unable to change):

   1. If |advocate| offer is active
