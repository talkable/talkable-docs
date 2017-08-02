.. raw:: html

   <h2>Coupon codes as a reward</h2>

.. important::

   Any code sent via this web hook doesn’t need to be created on merchant site.
   When Talkable needs more coupons — it always calls
   :ref:`Create Coupon Web Hook <web_hooks/create_coupon>`.
   In this web hook Talkable just sends the information to merchant that coupon
   was given as the reward in case merchant want to store this infomation in
   its own database.
