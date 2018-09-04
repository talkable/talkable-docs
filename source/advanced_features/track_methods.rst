.. _advanced_features/track_methods:
.. include:: /partials/common.rst

Referral Tracking Methods
#########################

Tracking referrals is an essential feature of the Talkable platform. When the
new event occurs Talkable Referral Engine tries to connect it to an Advocate
through a Friend Offer. It can be done using multiple methods. Each method is
applied according to their priority until the Friend Offer would be found.
Therefore Talkable interface shows each referral with the associated tracking
method.

Talkable platform tries to track as many referrals as possible, while gives an
opportunity to setup whether those referrals should qualify for a reward or be a
part of the attribution model (aka appear on the site dashboard). That is why
Talkable interface doesn’t have a lot of options to control Tracking Methods
while provides the customization for the rewarding criteria inside campaigns and
attribution model inside dashboards and reports.

The list of tracking methods by their priority:

.. raw:: html

   <h2>Manually Generated</h2>

- Only applies when the referral is made from Talkable admin pages.
- Has the top priority because it forces the referral to be made without
  checking any criteria.

.. raw:: html

   <h2>Sticky Advocate</h2>

- Only available for sites that have this feature enabled in the site settings.
- Designed for case where a single person can only be referred once, so that
  another Advocate will not be able to refer it again (or “steal” him from the
  previous Advocate).
- Checks whether a buyer was referenced before through his previous purchases or
  events (by same email or browser cookie) and attributes current event to the
  same Advocate as the previous one.
- Makes each Friend bounded to particular Advocate forever without the ability
  to make it referred again by a different Advocate.

.. raw:: html

   <h2>Coupon</h2>

- Friend used the coupon code he received through a Friend offer.
- Only applies to campaigns that are giving a single use coupon as a reward to a
  Friend before they make a purchase.

.. raw:: html

   <h2>Cookie</h2>

- Friend used the same browser session as when clicking the referral link.

.. raw:: html

   <h2>Web Cookie</h2>

- Only applies to the iOS/Android Mobile SDKs.
- Friend used the same browser session as when clicking the referral link.
- The technology for the referral detection is very different for Mobile SDK
  from the browser. That is why Talkable distinguishes between Cookie and Web
  Cookie tracking methods.

.. raw:: html

   <h2>Gated Email</h2>

- Friend used the same email address as they entered on the claim page.
- Only applies to campaigns that have Friend Signup feature enabled.

.. raw:: html

   <h2>Share Email</h2>

- Friend used the same email address in the Friend Share Email.
- Only applies to offers shared by Email channel.

.. raw:: html

   <h2>IP Address</h2>

- Friend used the same IP address as when clicking the referral link.
- Time limit: only applies when a Friend made a purchase or event within 1 hour
  after clicking the referral link.
- The method doesn’t apply to the blacklisted IP addresses, blacklisted emails,
  QA IP addresses and QA emails.

.. raw:: html

   <h2>Event Chain</h2>

- Friend was already referred before and this is his subsequent event. In this
  case, this event is automatically attributed to the same Advocate as the
  previous one.
- The method doesn’t apply to blacklisted emails and IP addresses.
