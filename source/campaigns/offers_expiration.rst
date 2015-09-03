.. _campaigns:
.. include:: /partials/common.rst

Offers Expiration
#################

Talkable Campaign allows to set offer expiration for |advocate| and |friend|
by specifying specific date or setting offer duration in hours.


.. raw:: html

   <h2>Advocate</h2>

- ``deadline`` - |advocate| will no longer be able to share after this date.
- All existing |advocate| offers are always affected if specified date is changed
  while campaign is live.
- Deadline is not copied when campaign is copied.
- When campaign is deactivated, all |advocate| offers instantly become expired because deactivating a campaign is equal to set |advocate| offer deadline to now.
- When |advocate| offer is expired, Advocate and Friend are still eligible for reward. 
  In other words advocate offer expiration only prevents |advocate| from sharing but not from getting rewarded

.. raw:: html

   <h2>Friend</h2>

- ``deadline`` - |friend| will no longer be able to claim the offer after this date.
- ``offer duration`` - |friend| will no longer be able to claim the offer X
  hours after |advocate| shared it with him. Leave blank to disable expiration at all.
- All existing |friend| offers will be affected if specified date or offer duration is
  changed while campaign is live.
- If date and offer duration are specified, |friend| offer will be expired on
  the closest date calculated from offer duration or specified in deadline.
- |friend| offer deadline should never be earlier than |advocate| offer deadline
  (because there is no sense to share offer that cannot be claimed).
- When |friend| offer is expired, |friend| and |advocate| are not able to receive any rewards. 
  But they still may try to use coupon they received earlier because talkable platform doesn't control coupon expiration. Only merchant site does that.
- When campaign is copied only offer duration gets copied, but not deadline.
