.. _advanced_features/referrals_approval:
.. include:: /partials/common.rst

.. meta::
   :description: The approvals process helps automatically detect fake new user accounts. Cheaters won’t get through the system.

Referrals Approval
==================

In a perfect world every advocate would receive their reward immediately
after a legitimate referral purchase to shorten the feedback
loop for advocating and to encourage a repurchase.

However, if you have strong marketing offers on products that are inherently
resellable and generous return policies you open yourself up to gaming
by not monitoring your approvals policy.

.. epigraph::
  **Example:** You sell a product online and offer a strong discount ($100) in your
  referral program for new users. The product you sell is a home good
  that is easily re-sellable online. You also offer a generous 30 day
  return policy. In this case marketing fraudsters may generate
  fake new user accounts, make purchases using 1 time credit cards,
  collect the reward as an advocate, and then return the items,
  thereby getting “free” money by gaming your referral program.

How can your approvals process help to automatically combat this system?

In the above case if you ensured that your returns policy window was shorter
than your approvals window (i.e. if you approved at 31 days,
after the 30 day return policy) then you would ensure
that no one would be able to game your system.

You may implement address fraud checks by passing address information
at checkout, which requires an integration update. You may also be able
to configure a returns api to automatically check for returns of your product
before crediting a reward.

General Approval Policy Recommendations
---------------------------------------

The safest programs either make the investment in automatic approval
verifications via api for returns and pass additional data for algorithmic
address checking as part of their integration or are smaller companies
with a lower number of transactions on higher value products
who can use manual approvals.

However, a large segment of customers are unable to make these sometimes
large upfront investments in program security or
due to the volume of transactions are unable to afford
manual review of the rewards. To mitigate against possible marketing
fraud while still maintaining an automatic approval process
we suggest the following guidelines:

#. Investigate your “median return time”.
   You may have a 60 days return policy but find that 70% of returns
   are made in the first 10 days. In this case you can set the automatic
   approval time to be 10 days - instantly cover 70% of cases - and then
   manually monitor the aggregate data on returns post 10 days
   to see if there’s any uptick in returns. This generally results in
   better program performance with near identical fraud attempts.
   Also, it’s easier to spot increases - in fraud if you begin to see
   a lot of returns after the 10 day mark you know to investigate further.
   You have created a situation where it’s now easier to identify fraudsters
   without affecting the vast majority of your customers.

#. Use coupon codes for rewards.
   Legally speaking coupon codes are easier to revoke, have an expiration date,
   and can have restrictions for minimum order values that will prevent users
   from attempting to defraud your program.

#. Manually check in on your referral program on a monthly or quarterly basis,
   or if you see any suspicious increases in certain activities.
   Using the “Flagged” property of our fraud detection system can allow you
   to view referrals that are suspicious and get a feel for
   what types of behavior may be occurring. Additionally,
   by tracking your data you can identify patterns in fraud behavior and
   take action.

#. Update your program as necessary. Be wary of marketing offers
   that may be combined to get larger discounts on your site.
   Do not be afraid to make changes in your approvals policy.
   If necessary, move to manual approvals of your program for a short
   period of time to diagnose any issues and then re-configure your approval
   process and fraud settings to address those issues.

   |

Configuring your approvals policy is a balance between ensuring a positive
experience for advocates and ensuring that your protect your business from
marketing offer fraud. We expose a spectrum of options to meet your
business needs. Where your business falls on the spectrum depends on
your product market, the relative value of gaming your program for resale,
and the resources you wish to allocate to ensuring a fair system.

If you have further questions feel free to `reach out to team <https://www.talkable.com/contact>`_
Our Professional Services team has years of experience in program design
and can help you weigh the costs and benefits.
