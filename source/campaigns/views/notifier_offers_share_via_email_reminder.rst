.. _campaigns/views/notifier_offers_share_via_email_reminder:
.. include:: /partials/common.rst

Friend Share Email Reminder
---------------------------

Email is triggered only if Friend Share Email Reminder checkbox was checked
on the :ref:`developer_advocate_share_page` when sharing. |br|
By default reminder email sends out in 72 hours after sharing if Friend didn't
use his Offer (i.e. didn't make a store purchase using coupon code).

Main |cta| should point to a Friend Claim Page — ``{{ short_url }}``. |br|
To change email trigger delay open ``Editor`` / ``Extra fields`` for the
particular email.

|br|

.. image:: /_static/img/basics/friend-share-email-reminder.png
   :alt: Friend Share Email Reminder

.. include:: /partials/developer_email_note.rst
