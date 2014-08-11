.. _campaigns:
.. include:: /partials/common.rst

Offers Expiration
#################

Talkable Campaign allows to set offer expiration for Advocate and Friend
by specifying specific date or setting offer duration in hours.

.. raw:: html

   <h2>Advocate</h2>

- ``deadline`` - Advocate will no longer be able to share after this date.
- ``offer duration`` - Unsupported.
- Note: All existing offers are always affected in specified date is changed
  while campaign is live.
- Deadline is not copied when campaign is copied.

.. raw:: html

   <h2>Friend</h2>

- ``deadline`` - Friend will no longer be able to claim the offer after this date.
- ``offer duration`` - Friend will no longer be able to claim the offer after X
  hours after Advocate shared it with him.
- All Friend offers will not be affected if specified date or offer duration is
  changed while campaign is live.
- If date and offer duration are specified, friend's offers will be expired on
  the closest date.
- When campaign is copied only offer duration gets copied, but not deadline.
- Friend offer deadline should never be earlier than Advocate offer deadline
  (because there is no sense to share offer that cannot be claimed).
