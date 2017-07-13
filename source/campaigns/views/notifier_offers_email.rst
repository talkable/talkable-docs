.. _campaigns/views/notifier_offers_email:
.. include:: /partials/common.rst

Advocate Offer Email
--------------------

Email is triggered to an |advocate| on sign up. Explain the value proposition
and encourage |advocate| to share using the buttons.

- For Standalone Campaign it triggers when |advocate| signs up.
- For Post-Checkout Campaign it triggers when |advocate| makes store purchase.
  It is not recommended to use this email here since it may look spammy.

Main |cta| should point to an Advocate Share Page — ``{{ share_page_url }}``.

|br|

.. image:: /_static/img/basics/advocate-offer-email.png

|br|

.. include:: /partials/developer_email_note.rst

.. raw:: html

   <h2>Email sending conditions</h2>

By default is sent immediately after the offer is created, but can be delayed by configuration.

1. Talkable creates an offer based on the following criteria:

  - Purchase creation
  - Affiliate member signup. |advocate| can sign up manually by entering their email, or their email is passed via JS integration (or URL). For example, a customer signs up to refer-a-friend on a /share page. This triggers an affiliate member signup.

2. Main email sending criteria (unable to change):

  - If |advocate| offer is active
