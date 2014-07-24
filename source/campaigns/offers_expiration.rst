.. _campaigns:
.. include:: /partials/common.rst

Offers Expiration
#################

Curebit Campaign allows to set offer expiration for Advocate and Friend 
by specifying specific date or set offer duration in hours

Advocate
--------

- ``deadline`` - Advocate will no longer be able to share after this date.
- ``offer duration`` - Unsupported
- Note: All existing offers are always affected in specified date is changed while campaign is live
- Deadline is not copied when campaign is copied

Friend
------

- ``deadline`` - Friend will no longer be able to claim the offer after this date
- ``offer duration`` - Friend will no longer be able to claim the offer after X hours after Advocate shared it with him
- All Friend offers will not be affected if specified date or offer duration is changed while campaign is live.
- If date and offer duration are specified friend offers will expire when the closest date will code
- When campaign is copied only offer duration gets copied, but not deadline.




