.. _campaigns/views/notifier_offers_share_via_email:
.. include:: /partials/common.rst

Friend Share Email
------------------

Email is triggered by an Advocate to his Friends from the
:ref:`developer_advocate_share_page`. |br|
The main purpose of this email is to invite a Friend by showing a personal
Share Message from Advocate along with a unique Friend Claim Page link. Some
information about offer itself is recommended.

Frequently used Variables:

- Main |cta| should point to a :ref:`developer_friend_claim_page` — ``{{ short_url }}``.
- To show Email Share Message from Advocate use ``{{ custom_message_body }}``.

|br|

.. image:: /_static/img/basics/friend-share-email.png
   :alt: Friend Share Email

.. include:: /partials/developer_email_note.rst
