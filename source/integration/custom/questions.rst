.. _integration/custom/questions:
.. include:: /partials/common.rst

F.A.Q.
======

1. :ref:`Does the post purchase script need to capture all purchases or just
   Talkable purchases? <integration/custom/questions/post_purchase_capture>`

2. :ref:`How does referral tracking work? <integration/custom/questions/how_does_referral_tracking_work>`

3. :ref:`What does the Talkable integration do? <integration/custom/questions/what_does_the_talkable_integration_do>`

4. :ref:`How does Talkable know where to display content? <integration/custom/questions/talkable_know_where_to_display_content>`

5. :ref:`What do I, as a developer, need to do to complete integration? <integration/custom/questions/complete_integration>`

6. :ref:`How does the rewarding process work? <integration/custom/questions/rewarding_process_work>`

7. :ref:`How do I verify success? <integration/custom/questions/verify_success>`

.. _integration/custom/questions/post_purchase_capture:

**1.) Does the post purchase script need to capture all purchases or
just Talkable purchases?**

The post purchase script needs to capture all purchases. This not only
simplifies the integration by removing any logic you need to perform on
your end to determine if a purchase is referral related but is required
so that Talkable can perform referral tracking which happens after the
purchase is captured. Talkable also reports on referral related sales
metrics to display what % of total sales referrals is responsible for
along with other sales related metrics.

.. _integration/custom/questions/how_does_referral_tracking_work:

**2.) How does referral tracking work?**

Talkable automatically handles all referral tracking, so there’s nothing
special you need to do as a developer. Talkable tracks referrals by at
least 1 of 3 possible tracking methods: {cookie, coupon code, and
email}. The most common tracking method is cookie, so if your ecommerce
platform is unable to surface coupon code as a parameter to pass at
checkout, then that’s fine as Talkable will still be able to track the
referral.

.. _integration/custom/questions/what_does_the_talkable_integration_do:

**3.) What does the Talkable integration do?**

-  Displays Refer-A-Friend content inside a Talkable generated iframe
   either as an overlay or inline

-  Handles all button click events, and mobile responsive resizing

-  Tracks referral attribution automatically

-  Blocks self-referral and gaming of the system

-  Handles all other referral related logic and communications

   -  Decides where to show content on your website based on rules
      defined inside of the Talkable platform

   -  Sends referral p2p and reward emails on your behalf

.. _integration/custom/questions/talkable_know_where_to_display_content:

**4.) How does Talkable know where to display content?**

-  "Placements" refer to areas of your website where referral content
   should display. These rules are defined inside of the Placements
   section inside the Talkable platform.

   -  You can modify default placements, add additional placements, or
      create various inclusion or suppression rules in the Talkable
      Placements section. This allows for future placement modification
      with minimal to zero developer work required.

   -  See Talkable Placements documentation for more details:
      :ref:`Campaign Placements <campaigns/campaign_placements>`

-  Talkable looks at the URL to determine display as defined by rules in
   the Placements section. Most integrations will be able to use default
   placements where no modification is necessary inside the Talkable
   platform.

-  Default Placements:

   -  Share Widget Campaign: All pages (inclusion and exclusion rules
      can be defined)

   -  Post Purchase Popup Campaign: Checkout confirmation page where the
      post purchase integration script resides.

   -  Advocate Landing Page Invite Campaign: URL ending in "/share"

   -  Referral Dashboard Campaign: URL ending in "/referrals"

.. _integration/custom/questions/complete_integration:

**5.) What work do I, as a developer, need to do to complete
integration?**

-  Surface variables, plug into integration script, and copy into the
   appropriate locations.

-  Create HTML pages for Advocate Landing Page and Referral Dashboard
   and paste the Talkable Container DIV in the body

   -  Create a link to the Referral Dashboard from your user accounts
      section or drop down menu

-  Validate your integration to verify success

-  (optional) DNS configuration for referral link and email sending
   subdomain white labeling (ask your Talkable contact to enable this)

.. _integration/custom/questions/rewarding_process_work:

**6.) How does the rewarding process work?**

Referring Advocate Reward payout is configurable, it can be triggered
automatically based on any grace period delay, through API call when
considering returns, or through manual approval. Once a reward is
approved, Talkable sends an email that communicates/delivers the reward.
Most customers choose auto approval after a 24-48 delay, which requires
little to no attention.

:underline:`Here’s how reward flow and logic works:`

After Talkable tracks the referred purchase we run it through two sets
of filters: fraud filters, and then campaign qualifiers.

-  Fraud filters will check for things such as self referral, cross
   referral, similar email match, matching ip + device, matching
   shipping address, etc.

-  Campaign qualifiers are checked once fraud filters are passed. This
   contains the campaign referral logic that determines when a reward is
   due, such as: is the friend a new customer?, did the friend spend >
   $X?, etc.

:underline:`Reward approval`

Once a referred purchase is qualified in passing through both of these
filters, the reward is now in a pending state and ready to be
approved/paid. Most companies turn on auto reward approval which will
auto approve the reward after some grace period. Approval can be
configured via API if return rate is abnormally high, but considering
that standard Advocate reward redemption rate is between 20-30% this is
typically not necessary.

:underline:`API approval to account for returns`

The way this works is that you would ping Talkable on all orders that
reach some final valid or failed state. This uses lazy logic so you
don’t need to know if a purchase is referral related or not, Talkable
will determine this. So any order# you ping us with that’s not related
to a pending referral, we’ll gracefully ignore, and any order# we
recognize as related to a pending referral, we’ll take the appropriate
action.

.. _integration/custom/questions/verify_success:

**7.) How do I verify success?**

Refer to the section titled :ref:`Validating the Integration <integration/custom/validating_integration>`.
