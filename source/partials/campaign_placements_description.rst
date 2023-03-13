Campaign Placements are the places (pages) on your site where the Campaigns are shown to your customers.

The list of all Campaign Placements can be found by going to the All Site Settings page from the header Menu (top right corner) and choosing the Placements section:

.. raw:: html

  <img src="../_static/img/campaign_placements/path.png" />

**Managing Placements**.
By default you already have all types of Placements created automatically.
Campaigns that you create will attach to one of these Placements based on their types.
If you want you can create a new Standalone Placement for your site matching another URL and attach another
Standalone Campaigns there.

.. note::
  Placements are strictly tied to their Campaign types.
  You cannot attach Post Purchase Campaign to Standalone Placement because it expects Campaigns that are going to be embedded not being shown as a popup.

**Priority**.
The Placements in the list are ordered by priority. In order to show a Campaign, Talkable matches
the URL of a Campaign Placement inclusion (marked as “Shown on”) and a URL that comes with each request that
users initiate, for example: `https://[your-site]/share`. Whenever multiple Campaign Placements fit the requested URL
Talkable picks the first Placement that sits up top out of the suitable ones. Other Placements that sit below it are
ignored in this case.

**Visibility**.
It is possible to indicate on which specific pages the Campaigns attached to the Placement should or should not be shown.
It allows you to show the Campaign on all pages of your site except few specified in the "Hidden on" section, for example.
Also, you can use :ref:`regular expressions<advanced_features/reg_ex>` to select pages you want to not show Talkable campaigns on.

|hr|

.. raw:: html

  <h2>Referral Placements</h2>

  <h3>Standalone</h3>

Campaign will show up on the standalone page on your site, for example: |br|
`https://[your-site]/share`.
|br|
Campaign will be rendered as an inline block in a corresponding Talkable DIV tag.

:ref:`Learn more about Standalone Placement <campaigns/campaign_placements/standalone>`

.. raw:: html

  <h3>Post Purchase</h3>

Campaign will show up on a successful purchase made by the customer on your site.
Usually this is an order confirmation page after checkout.
The campaign will look like a popup with an overlay and a close button.

:ref:`Learn more about Post Purchase Placement <campaigns/campaign_placements/post_purchase>`

.. raw:: html

  <h3>Floating Widget</h3>

Campaign will show up on every page as a floating button in a corner of the screen so customers are able to access
Talkable campaigns from anywhere on your site.
Clicking on a Floating Widget Campaign expands the full Campaign view that looks like a popup with an overlay
and a close button.

:ref:`Learn more about Floating Widget Placement <campaigns/campaign_placements/floating_widget>`

.. raw:: html

  <h3>Claim by Name Widget</h3>

Campaign will show up as a floating button in a corner of the screen on the cart or checkout page on your site,
for example: |br|
`https://[your-site]/cart`.
|br|
Clicking on a Claim by Name widget opens a popup with an overlay and a close button.

:ref:`Learn more about Claim by Name Placement <campaigns/campaign_placements/claim_by_name>`

.. raw:: html

  <h3>Gleam</h3>

Campaign will show up on every page as a floating bar that shows your customers their coupon codes
after they have been rewarded within any other of your Talkable Campaigns.

:ref:`Learn more about Gleam Placement <campaigns/campaign_placements/gleam>`

.. raw:: html

  <h2>Loyalty Placements</h2>

  <h3>Loyalty Dashboard</h3>

Campaign will show up on the loyalty page on your site, for example: |br|
`https://[your-site]/loyalty`.
|br|
Campaign will be rendered as an inline block in a corresponding Talkable DIV tag.

:ref:`Learn more about Loyalty Dashboard Placement <campaigns/campaign_placements/loyalty_dashboard>`

.. raw:: html

  <h3>Loyalty Widget</h3>

Campaign will show up on every page as a floating widget that allows your customers to convert their points into coupons.

If a customer is not signed in, the widget prompts them to join the loyalty program.

:ref:`Learn more about Loyalty Widget Placement <campaigns/campaign_placements/loyalty_widget>`

.. note::
  When both Loyalty Dashboard and Loyalty Widget are matched on the same URL, only Dashboard will be shown.

.. raw:: html

  <h3>Claim by Name</h3>

By default, campaign will be shown only on /checkout page. This type of campaign allows customers to fill in advocate username and get a reward.

:ref:`Learn more about Claim by Name Placement <campaigns/campaign_placements/claim_by_name>`

|hr|

.. raw:: html

  <h2>Campaigns Rotating</h2>

It is worth mentioning that you can also attach multiple Campaigns into one Placement.
In this case Talkable will always show only one Campaign based on a random rotation.
This mechanism is useful if you want to compare which Campaign has higher referral conversion rate by changing
Incentives or other referral pieces in the other Campaign.
