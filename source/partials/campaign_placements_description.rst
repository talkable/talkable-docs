Campaign Placements are the places (pages) on your site where the Campaigns are shown to your customers.

The list of all Campaign Placements can be found by going to the All Site Settings page from the header Menu (top right corner) and choosing the Placements section:

.. image:: _static/img/campaign_placements/path.png

Managing Placements
-------------------

By default you already have all types of Placements created automatically.
Campaigns that you create will attach to one of these Placements based on their types.
If you want you can create a new Standalone Placement for your site matching another URL and attach another
Standalone Campaigns there.

.. note::
  Placements are strictly tied to their Campaign types.
  You cannot attach Post Purchase Campaign to Standalone Placement because it expects Campaigns that are going to be embedded not being shown as a popup.

Priority
--------

The Placements in the list are ordered by priority. In order to show a Campaign, Talkable matches
the URL of a Campaign Placement inclusion (marked as “Shown on”) and a URL that comes with each request that
users initiate, for example: `https://[your-site]/share`. Whenever multiple Campaign Placements fit the requested URL
Talkable picks the first Placement that sits up top out of the suitable ones. Other Placements that sit below it are
ignored in this case.

Visibility
----------

It is possible to indicate on which specific pages the Campaigns attached to the Placement should or should not be shown.
It allows you to show the Campaign on all pages of your site except few specified in the "Hidden on" section, for example.
Also, you can use :ref:`regular expressions<advanced_features/reg_ex>` to select pages you want to not show Talkable campaigns on.

Custom Property Criteria
------------------------

A Placement can have a set of criteria defined based on :ref:`custom properties <advanced_features/passing_custom_data>`.
If all of the criteria are met, the placement will show a campaign.

The criteria can be defined using one of the following operators:

- `eq`
- `not_eq`
- `regex` (performs a case-insensitive match)

.. note::
  Custom Property Criteria require integration version 5.1.4 or higher to work.

Container Name
--------------

It is possible to update the container name by requesting assistance from the Talkable team.
The current DIV id value for each Event Category can be found on the Placements page.

By default, the DIV id is:

* `talkable-offer` for `affiliate_member` event category which includes: Standalone, Standalone Dashboard, Floating Widget, Gleam;
* `talkable-post-purchase` for `purchase` event category which includes: Post Purchase;
* `talkable-claim-by-name` for `claim_by_name_popup` event category which includes: Claim By Name;
* `talkable-email-capture-offer` for `email_capture_popup` event category which includes: Conversion Popup;
* `talkable-loyalty` for `loyalty_dashboard` and `loyalty_widget` event categories which include: Loyalty Dashboard and Loyalty Widget.

.. note::
   Container name changes require integration version 5.3.0 or higher to work.

|hr|

Referral Placements
~~~~~~~~~~~~~~~~~~~

Standalone
^^^^^^^^^^

Campaign will show up on the standalone page on your site, for example: |br|
`https://[your-site]/share`.
|br|
Campaign will be rendered as an inline block in a corresponding Talkable DIV tag.

:ref:`Learn more about Standalone Placement <campaigns/campaign_placements/standalone>`

Post Purchase
^^^^^^^^^^^^^

Campaign will show up on a successful purchase made by the customer on your site.
Usually this is an order confirmation page after checkout.
The campaign will look like a popup with an overlay and a close button.

:ref:`Learn more about Post Purchase Placement <campaigns/campaign_placements/post_purchase>`

Floating Widget
^^^^^^^^^^^^^^^

Campaign will show up on every page as a floating button in a corner of the screen so customers are able to access
Talkable campaigns from anywhere on your site.
Clicking on a Floating Widget Campaign expands the full Campaign view that looks like a popup with an overlay
and a close button.

:ref:`Learn more about Floating Widget Placement <campaigns/campaign_placements/floating_widget>`

Claim by Name Widget
^^^^^^^^^^^^^^^^^^^^

Campaign will show up as a floating button in a corner of the screen on the cart or checkout page on your site,
for example: |br|
`https://[your-site]/cart`.
|br|
Clicking on a Claim by Name widget opens a popup with an overlay and a close button.

:ref:`Learn more about Claim by Name Placement <campaigns/campaign_placements/claim_by_name>`

Gleam
^^^^^

Campaign will show up on every page as a floating bar that shows your customers their coupon codes
after they have been rewarded within any other of your Talkable Campaigns.

:ref:`Learn more about Gleam Placement <campaigns/campaign_placements/gleam>`

Loyalty placements
~~~~~~~~~~~~~~~~~~

Loyalty Dashboard
^^^^^^^^^^^^^^^^^

Campaign will show up on the loyalty page on your site, for example: |br|
`https://[your-site]/loyalty`.
|br|
Campaign will be rendered as an inline block in a corresponding Talkable DIV tag.

:ref:`Learn more about Loyalty Dashboard Placement <campaigns/campaign_placements/loyalty_dashboard>`

Loyalty Widget
^^^^^^^^^^^^^^

Campaign will show up on every page as a floating widget that allows your customers to convert their points into coupons.

If a customer is not signed in, the widget prompts them to join the loyalty program.

:ref:`Learn more about Loyalty Widget Placement <campaigns/campaign_placements/loyalty_widget>`

.. note::
  When both Loyalty Dashboard and Loyalty Widget are matched on the same URL, only Dashboard will be shown.

Campaigns Rotating
~~~~~~~~~~~~~~~~~~

It is worth mentioning that you can also attach multiple Campaigns into one Placement.
In this case Talkable will always show only one Campaign based on a random rotation.
This mechanism is useful if you want to compare which Campaign has higher referral conversion rate by changing
Incentives or other referral pieces in the other Campaign.
