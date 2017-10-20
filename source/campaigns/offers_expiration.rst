.. _campaigns/offers_expiration:
.. include:: /partials/common.rst

Offers Expiration
#################

Talkable Campaign allows to set offer expiration for |Advocate| and |Friend|
by specifying specific date or setting offer duration in hours.

.. raw:: html

   <h2>Advocate</h2>

- ``Advocate deadline`` - |advocate| will no longer be able to share after this date.
- All existing |Advocate| offers are always affected if specified date is changed
  while campaign is live.
- |Advocate| Deadline is not copied when campaign is copied.
- When campaign is deactivated, all |Advocate| offers instantly become expired because deactivating a campaign is equal to set |Advocate| offer deadline to now.
- When |Advocate| offer is expired, |Advocate| is still eligible for reward.
  In other words Advocate offer expiration only prevents |Advocate| from sharing but not from getting rewarded.
- This setting doesn’t affect |Friend| reward in any way.

.. raw:: html

   <h2>Friend</h2>

- ``Friend Deadline`` - |Friend| will no longer be able to claim the offer after this date.
- ``Friend Offer Duration`` - |Friend| will no longer be able to claim the offer X
  hours after |Advocate| shared it with him. Leave blank to disable expiration at all.
- All existing |Friend| offers will be affected if specified date or offer duration is
  changed while campaign is live.
- If a deadline and an offer duration are both specified, |Friend| offer will be expired on
  the closest date calculated from offer duration or specified in deadline.
- |Friend| offer deadline should never be earlier than |Advocate| offer deadline
  (because there is no sense to share offer that cannot be claimed).
- When |Friend| offer is expired, |Friend| and |Advocate| are not able to receive any rewards.
  But they still may try to use coupon they received earlier because talkable platform doesn’t control coupon expiration. Only merchant site does that.
- When campaign is copied only offer duration gets copied, but not deadline.
