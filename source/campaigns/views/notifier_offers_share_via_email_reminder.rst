.. _campaigns/views/notifier_offers_share_via_email_reminder:
.. include:: /partials/common.rst

.. _friend_share_email_reminder_view:

Friend Share Email Reminder
---------------------------

Email is triggered only if Friend Share Email Reminder checkbox was checked
on the :ref:`advocate_share_page_view` when sharing. |br|
By default reminder email sends out in 72 hours after sharing if |friend| didn't
use their Offer (i.e. didn't make a store purchase using coupon code).

Main |cta| should point to a Friend Claim Page — ``{{ short_url }}``. |br|
To change email trigger delay open ``Editor`` / ``Extra fields`` for the
particular email.

|br|

.. image:: /_static/img/basics/friend-share-email-reminder.png
   :alt: Friend Share Email Reminder

.. include:: /partials/developer_email_note.rst

.. raw:: html

   <h2>Email sending conditions</h2>

By default the email is sent in 72 hours after the offer is shared.

1. Main email sending criteria (unable to change):

  - If |friend| offer is active
  - Recipient (|friend|) was not referred by this offer yet
  - Current offer is the last one shared with the recipient (if were delayed few reminders Talkable sends the last one)

