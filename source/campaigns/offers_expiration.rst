.. _campaigns:
.. include:: /partials/common.rst

Offers Expiration
#################

Talkable Campaign allows to set offer expiration for Advocate and Friend
by specifying specific date or setting offer duration in hours.

.. note:: Offer Expiration does not prevent Advocate or Friend from getting rewards
     and receiving corresponding emails. This can be configured separately through
     Trigger/Sending criteria.

.. raw:: html

   <h2>Advocate</h2>

- ``deadline`` - Advocate will no longer be able to share after this date.
- All existing Advocate offers are always affected if specified date is changed
  while campaign is live.
- Deadline is not copied when campaign is copied.

.. raw:: html

   <h2>Friend</h2>

- ``deadline`` - Friend will no longer be able to claim the offer after this date.
- ``offer duration`` - Friend will no longer be able to claim the offer after X
  hours after Advocate shared it with him. Put 0 to disable expriration at all.
- All existing Friend offers are not affected if specified date or offer duration is
  changed while campaign is live.
- If date and offer duration are specified, Friend offer will be expired on
  the closest date.
- Friend offer deadline should never be earlier than Advocate offer deadline
  (because there is no sense to share offer that cannot be claimed).
- When campaign is copied only offer duration gets copied, but not deadline.
