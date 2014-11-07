.. _campaigns/views/notifier_offers_share_via_email:
.. include:: /partials/common.rst

.. _friend_share_email_view:

Friend Share Email
------------------

Email is triggered by an |advocate| to his |friend|\s from the
:ref:`advocate_share_page_view`. |br|
The main purpose of this email is to invite a |friend| by showing a personal
Share Message from |advocate| along with a unique Friend Claim Page link. Some
information about offer itself is recommended.

Frequently used Variables:

- Main |cta| should point to a :ref:`friend_claim_page_view` — ``{{ short_url }}``.
- To show Email Share Message from Advocate use ``{{ custom_message_body }}``.

|br|

.. image:: /_static/img/basics/friend-share-email.png
   :alt: Friend Share Email

.. include:: /partials/developer_email_note.rst
