.. _campaigns/views:
.. include:: /partials/common.rst

Views
=====

Each Talkable campaign has a set of pages and emails to help you control nearly every
step of the refer-a-friend campaign. Such page or email is called a View. You can also
control appearance of each View by visiting Appearance:

.. image:: /_static/img/campaign/subnav.png
   :alt: Campaign Appearance

|br|
|br|
Understanding Page-Views is easy, just go through the glossary and learn who lands on
what Page-View and where. Email-Views are more tricky in terms of understanding when
they are sent. All Email-Views must go through a pre-validation step before they are
sent:

\1. Check if the Campaign View is in use (controlled inside Campaign Rules). Otherwise
the email will never be sent.

.. image:: /_static/img/campaign/rules-views.png

|br|
2. Is the recipient email in a valid email format (i.e. Talkable mail servers can deliver an email to a real recipient)? If so, we move on to campaign specific rules
to determine whether or not the email should be sent (see `Email sending conditions` sectopn inside each Email-View).

After pre-validation Talkable campaign level validation kicks in:

1. Who is the recipient? |advocate| or |friend|?
2. What are the email sending conditions for the campaign?
3. Time Conditional |rarr| send an email in 3 days
4. Action Conditional |rarr| send email after friend purchases
5. Inaction Conditional |rarr| send 2nd email if friend does not purchase
6. Offer State Conditional |rarr| send email only if offer still valid / send email is
   offer is expired
7. Customer Attribute Conditional |rarr| send email if user is new customer

.. raw:: html

  <h2>Views glossary</h2>

.. toctree::

   views/affiliate_members_new
   views/offers_show
   views/notifier_offers_email
   views/notifier_offers_share_via_email
   views/notifier_offers_share_via_email_reminder
   views/offers_claim
   views/advocate_rewards_confirmation
   views/advocate_rewards_paid
   views/friend_rewards_paid
