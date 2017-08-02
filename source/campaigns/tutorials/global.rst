.. _campaigns/tutorials/global:
.. include:: /partials/common.rst

Global
------

.. _tutorials_zeroclipboard:

ZeroClipboard
.............

If you are using more multiple ZeroClipboard instances and one of them is placed inside hidden block (with display: none;), make sure to fire up that instance like following:

.. include:: /samples/liquid/global/zeroclipboard.rst

.. _tutorials_single_visitor_for_email_shares:


Allow showing coupon in the Friend Share Email and its reminder
...............................................................

This option means that there could be only one visitor for each email share (one per email per offer). When this option is active such opportunities appear:

**Show Coupon in the Friend Share Email and its reminder:**
  Talkable allows you to control whether you want to generate a unique coupon code for each email share or all shares made by an Advocate should have an exact same coupon code associated with it. When using single-use coupons it is recommended to enable this option only if you want to show the coupon inside Friend Share email and its reminder(s).

**{{ coupon_code_used }} interpolation:**
  {{ coupon_code_used }} becomes available as an interpolation in Friend share email and its reminder(s). It allows you to check whether the coupon code has been used already at checkout.

**Skip email gating:**
  Allows you to make a smooth user experience for Friend where they can surpass email gating on the Friend Claim page when clicking from the Friend Share email and its reminder(s). This is done for Friend’s convenience.

