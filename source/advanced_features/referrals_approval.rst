.. _advanced_features/referrals_approval:
.. include:: /partials/common.rst

.. meta::
   :description: The approvals process helps automatically detect fake new user accounts. Cheaters won’t get through the system.

Referrals Approval
==================

Talkable referral engine determines if the friend is a valid person based on fraud settings configuration. 
The incentive engine then decides if the reward should be given based on incentive criteria. Here is a common example:

#. The advocate shares a link with a friend

#. The friend clicks on the referral link and claims their coupon

#. The friend makes a referral purchase using the coupon they just claimed

#. Talkable first checks whether the friend is valid and only then the incentive decides whether the reward should be paid out.
   At this stage Talkable validates whether the friend was a valid person and not a self-referral (per fraud settings configuration).

#. If the referral is valid, Talkable approves it with a preset delay (ie. of 1-2 days)
   which is determined by the ”pending referrals auto-approval delay” field (under fraud settings).
   See recommendations below as to why it is best practice to set a delay.

#. As soon as the referral gets approved, Talkable passes it to the incentive engine which in turn checks whether the reward should be issued per campaign rules setup.
   Rules like a minimum order subtotal amount or new/existing customer check may block the reward from being issued even if the referral is approved.

#. If the incentive criteria are passed, the advocate gets a referral reward issued to them by email as a coupon or store credit, depending on your setup.

   |

In a perfect world every advocate would receive their reward immediately after a legitimate referral purchase to shorten the feedback loop for advocating and to encourage a repurchase.

However, if you have strong marketing offers on products that are inherently resellable and generous return policies you open yourself up to gaming by not monitoring your approvals policy.

.. epigraph::
  **Example:** You sell a product online and offer a strong discount ($100) in your referral program for new users.
  The product you sell is a home good that is easily re-sellable online.
  You also offer a generous 30-day return policy. In this case, marketing fraudsters may generate fake new user accounts,
  make purchases using 1-time credit cards, collect the reward as an advocate, and then return the items,
  thereby getting “free” money by gaming your referral program.

How can your referral management process help to automatically combat this system?

In the above case, if you ensured that your return policy window was shorter
then your referral approval window (i.e. if the referral is approved in 31 days,
after the 30-day return policy) then you would ensure
that no one would be able to game your system.

You may implement address fraud checks bypassing address information
at checkout, which requires an integration update. You may also be able
to configure a returns API to automatically check for returns of your product
before crediting a reward.

General Approval Policy Recommendations
---------------------------------------

The safest programs fall into either of these categories:

#. Referrals are managed through the `Referrals API </api_v2/referrals.html>`_ in a fully-automated fashion.
   This way, whenever the return happens, the referral can be voided through the API.
   As a result, no advocate rewards will be issued from that referral.

#. If the number of referrals is small enough to manage them manually,
   it is recommended to set the ”pending referrals auto-approval delay”
   to an optimal value which gives your team adequate time to resolve referrals manually.
   All referrals that weren’t resolved manually will be automatically approved by Talkable.
   There is also a separate delay for flagged referrals: they should ideally be automatically voided
   because flagged policies usually catch fraudulent referrals.

   |

If a fully-automated API solution isn’t possible, it is recommended to use automatic referral resolution
so that Talkable automatically approves pending referrals and voids flagged referrals for you.
To mitigate possible marketing fraud while still maintaining an automatic approval process
we suggest the following guidelines:

#. Investigate your ”median return time”. You may have a 60 days return policy but find that 70% of returns are made in the first 10 days.
   In this case, you can set the pending referrals auto-approval delay to be 10 days - instantly covering 70% of cases - and then manually monitor
   the aggregate data on returns after 10 days to see if there’s an uptick in returns.
   This generally results in better program performance with near-identical fraud attempts. Also, it’s easier to spot increases in fraud.
   For example, if you begin to see a lot of returns after the 10-day mark you’ll know to investigate further.
   You have created a situation where it’s now easier to identify fraudsters without affecting the vast majority of your customers.

#. Use single-use coupon codes for rewards. Legally speaking coupon codes are easier to revoke, have an expiration date,
   and can have restrictions for minimum order values that will prevent users from attempting to defraud your program.

#. Manually check in on your referral program on a monthly or quarterly basis, or if you see any suspicious increases in certain activities.
   Using the ”Flagged” property of our fraud detection system can allow you to view referrals that are suspicious and
   get a feel for what types of behavior may be occurring. Additionally, by tracking your data you can identify patterns in fraudulent behavior and take action.

#. Update your program as necessary. Be wary of marketing offers that may be combined to get larger discounts on your site.
   Do not be afraid to make changes in your approvals policy. If necessary, move to manual approvals of your program for a short period of time to diagnose any issues
   and then re-configure your approval process and fraud settings to address those issues.

   |

Configuring your referral auto-resolution system is a balance between ensuring a positive experience for advocates and ensuring that you protect your business from marketing offer fraud.
We expose a spectrum of options to meet your business needs.
Where your business falls on the spectrum depends on your product market, the relative value of gaming your program for resale, and the resources you wish to allocate to ensure a fair system.

If you have further questions feel free to `reach out to our team <https://www.talkable.com/contact>`_.
We have years of experience in referral program design and can help you weigh the costs and benefits.
