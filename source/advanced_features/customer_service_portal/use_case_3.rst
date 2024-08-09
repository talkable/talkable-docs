.. _advanced_features/customer_service_portal/use_case_3:
.. include:: /partials/common.rst

Use case #3: |br| Who should get the reward?
============================================

Talkable does not issue a reward in all referral cases. There may be numerous reasons why a reward is not issued to
an Advocate or Friend. The easiest way to find out the reward status is by visiting the Referrals tab:

.. image:: /_static/img/advanced_features/customer_service_portal/referrals.jpg

Navigating to each referral ‘Details’ page we can find out the status for each reward. Reason near the reward
status explains why the reward was not given.

.. image:: /_static/img/advanced_features/customer_service_portal/reason_reward.jpg

Every reward has the following possible statuses:

- **Pending**: the reward is awaiting referral approval. The referral can either be approved manually or automatically,
  depending on your configuration. If the referral status is Pending you may wait until the referral auto-approval
  happens. Otherwise please press “Void” or “Approve” button in the referral actions section, to either block or issue
  the reward.

- **Waiting for coupon**: there are not enough coupons left to pay the reward. Click on the reward link → Incentive
  type → Remember the coupon list chosen → Manage coupon lists → Find the desired coupon list and press “Add coupons”.

- **Given**: the reward was paid to the person but Talkable does not have information whether it was used or not.
  Most likely it was not yet used.

- **Voided**: the reward was voided because the referral was voided by a user manually.

- **Blocked/No reward**: the reward was blocked either because the associated referral was blocked according to
  Fraud Settings or because of other reasons: incentive criteria has blocked it, or the person was blocklisted.

.. image:: /_static/img/advanced_features/customer_service_portal/referral_incentive.jpg

(All incentive criteria are defined in Campaign Rules → Incentives. See reward criteria section.)

Here are some common incentive criteria block reasons:

- **Friend didn’t meet minimum purchase requirement**. On a screenshot above Friend’s referral purchase subtotal
  should be over $20. The incentive criteria will block Advocate’s reward in case Friend’s order subtotal will
  be less (post discount).

- **Friend’s offer was expired**. Based on Campaign Rules setup, Friend’s offer may expire after a certain period
  of time. Most likely the Friend received their coupon code by visiting a share link and then decided to save their
  discount for later. If Friend makes a purchase after their offer expires (using that coupon) the Advocate will not
  get a reward.

- **Friend is not a new customer**. Friend was an existing customer (> 1 purchase tracked) while making their referral
  purchase, however the incentive configuration only allows referring new customers.

- **Friend has already been referred**. The Advocate has already referred this Friend before but the incentive
  configuration only allows referring the same Friend only once.

Other reasons why a reward can be blocked (not incentive related):

- **Advocate has reached maximum rewards**. This is because Talkable has set a threshold for the maximum number of
  rewards that an Advocate can receive. The Friend may be rewarded in this case (as in the example above),
  but not the Advocate.

- The associated referral was blocked/voided for self/cross referral.

Handling customer inquiries
---------------------------

Here is how to detect self-referrals in case you’ve got an email/call from a customer:

1. Enter the customer’s email address in the Person Lookup.
2. Review the “Referrals” tab and look for a “self-referral” alert:

.. image:: /_static/img/advanced_features/customer_service_portal/self_referral.jpg

3. Inspect the customer’s email address to see if it’s the same or similar to the Friends; you  can also inspect inside
the referral details the IP address and cookie to see if they match:

.. image:: /_static/img/advanced_features/customer_service_portal/fraud_settings.jpg

4. If it’s not obvious why the customer was flagged for self-referral (meaning that none of these three items matched),
   then you should click “Details” to dive deeper.

5. Inspect to see if any other “blocked reasons” appear. In the below case, we see that not only do the email addresses
   match, but there was also a matching cookie on the Friend purchase (meaning they used the same browsing session to both
   share as an Advocate and click on the share link as a Friend), and lastly, there’s a matching combination of IP address
   and user agent - meaning the Advocate and Friend were using the same device and IP address, in combination.

.. image:: /_static/img/advanced_features/customer_service_portal/blocked_reasons.jpg

Cross referrals
---------------

The last use case is when an Advocate has not received his or her reward due to **Cross Referral**. Cross referral
occurs when an Advocate shares with a Friend who purchases and that same Friend then shares with an Advocate
in an attempt to get both the Advocate and Friend rewards.

We identify this in the same way as described above.

.. container:: hidden

   .. toctree::
