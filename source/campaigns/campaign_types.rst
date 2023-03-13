.. _campaigns/campaign_types:
.. include:: /partials/common.rst

.. meta::
   :description: Motivate customers to share your products with their Friends from anywhere on your site.

Campaign Types
==============

Encourage customers to share with their friends from anywhere on your site.

Invite
------

Invite campaigns allow site visitors to share with their friends from anywhere
on your site. Invite campaigns are both powerful and versatile. Multiple Invite
campaigns can be run simultaneously for maximum results.

.. image:: /_static/img/campaign_types/invite.png
   :alt: Campaign Type - Invite
   :class: is-minimal

Advocate Dashboard
------------------

The Advocate Dashboard allows the Advocate to see a complete overview of their
shares and rewards. Seeing an overview of their activity makes Advocates more
motivated to share. Advocate Dashboards also reduce Customer Service inquiries
as customers can see statuses directly from the dashboard.

.. image:: /_static/img/campaign_types/dashboard-type.png
   :alt: Campaign Type - Dashboard
   :class: is-minimal

Reward Gleam
------------

A Reward Gleam improves the on-site conversion rate by assisting Friends and
Advocates in using their coupons to purchase. When the Friend or Advocate
receives a reward and visits your website the coupon code is captured. The code
will be highlighted in the Reward Gleam at the bottom of the page.

.. image:: /_static/img/campaign_types/gleam.jpg
   :alt: Campaign Type - Reward Gleam
   :class: is-minimal

Leaderboard
-----------

A Leaderboard turns referrals into a competition. Advocates are ranked on a
Leaderboard page based on the number of successful referrals. After an allotted
time period, top performers can be identified and rewarded with a grand prize.

.. image:: /_static/img/campaign_types/leaderboard.png
   :alt: Campaign Type - Leaderboard
   :class: is-minimal

Tiered Rewards
--------------

A Tiered Rewards campaign incentivizes Advocates to share with multiple friends
as they are rewarded for subsequent successful referrals. By setting reward
goals for Advocates, they are more likely to increase their share rate.

.. image:: /_static/img/campaign_types/tiered_rewards.png
   :alt: Campaign Type - Tiered Rewards
   :class: is-minimal

.. _campaigns/claim_by_name:

Claim by Name
-------------

A Claim by Name campaign is a part of the name sharing setup for referral campaigns.
The setup consists of the campaign(s) where the personal name sharing channel is enabled
(the Advocate campaign) and the Claim by Name campaign (the Friend campaign).
The Advocate can share their name and describe the referral offer via any channel they prefer,
and the Friend can then claim the reward by entering the Advocate's personal name in the Claim by Name popup.

.. note::
   Claim by Name campaign does not offer any incentives on its own. Both the Advocate and the Friend rewards
   should be specified in the name sharing campaign (i.e. the campaign with personal name sharing channel enabled).
   Similarly, the funnel metrics are also tracked within the Advocate campaign.

Personal name sharing channel is available as a configuration localization on Advocate share page
in all new campaign templates.

.. note::
   You need to have the Claim by Name campaign launched to see the "Advocate share page channel personal name" localization.

If you don't have the localization in your campaign code, you can add it manually in the HTML & CSS editor mode.

.. code-block:: liquid

  {% assign advocate_share_page_channel_personal_name = "advocate_share_page_channel_personal_name" | localize: trait: "boolean", default: "Disabled" %}

.. image:: /_static/img/campaign_types/claim_by_name.png
   :alt: Campaign Type - Claim by Name
   :class: is-minimal
