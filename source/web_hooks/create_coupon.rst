.. _web_hooks/create_coupon:
.. include:: /partials/common.rst

.. meta::
   :description: Create Coupon Webhook enables automatic coupon creation. That means you are no longer need to upload coupon lists into the Talkable platform manually.

Create Coupon Webhook
=====================

Talkable Create Coupon Webhook enables automatic coupon creation, which
eliminates the need to upload coupon lists into the Talkable platform manually.
Talkable creates unique coupon codes then passes those codes via the Create
Coupon Webhook to the client; it is then up to the client to enable these coupons
on their platform.

.. raw:: html

   <h2>When does Talkable call the Create Coupon Webhook?</h2>

Create Coupon Webhook is called when the quantity of available coupons drops
below a Talkable threshold.

This threshold is dynamically calculated based on the number of coupon codes
used by the client site in the last 21 days. The threshold ensures the Talkable
coupon lists will always hold enough available coupons to serve the site for 21
days, even if the integration were to break. The minimum threshold is 20 coupons.

When the number of coupons available to Talkable drops below the threshold,
Talkable will call the Create Coupon Webhook with a payload of 15 new coupons in
the background. If a user needs a coupon code, but there are no coupon codes
available, Talkable will generate one in the foreground and give it to the user
that requested it. In both cases, coupons are sent to the client endpoint as a
webhook and then inserted into the Talkable database only when a webhook returns
a successful response.

.. raw:: html

   <h2>Set Up</h2>

The Create Coupon Webhook will add coupons to a specific coupon list on Talkable’s
backend. These coupon lists must be set up in the Talkable campaign editor before
utilizing the Create Coupon Webhook. Follow the below instructions to set up a
coupon list for a campaign:

1. Navigate to **Campaigns** then select the campaign you would like to set up
   coupon list(s) for
2. Proceed to **Rules** then scroll down to **Incentives** section where
   incentives for both Advocate and Friend can be configured

.. image:: /_static/img/advocate_referral_incentive.png
   :alt: Edit Referral Incentives
   :class: is-minimal

3. Inside the Referral Incentive Editor choose the **Coupon code type: Single-use**
   then select an existing Coupon list or create a new coupon list by clicking
   **Manage Coupon Lists**.
4. Here you’ll be able to **Create New** and configure a Name, Expiration Date
   (optional), and Amount ($ or %)
5. Now go back to **Rules** → **Incentives** → **Edit** and select the
   **Reward Amount** associated with the list created in step 4 and select the
   newly created list
6. Optionally, select **Advanced Settings** for additional configuration parameters

.. note::

   Coupons created by the **Create Coupon Webhook** will be added to the coupon
   list associated with the referral campaign. Multiple referral campaigns can
   use the same or unique coupon lists. **Advocate** and **Friend** referral
   incentives can also use the same or unique coupon lists.

Once a single-use coupon code list is associated with a campaign, then the
Create Coupon Webhook can now be set up.
:ref:`Learn more about General Webhook Set Up Steps <web_hooks>`

.. raw:: html

   <h2>Payload parameters provided by Create Coupon Webhook</h2>

The sample payload with parameters for Create Coupon Webhook is available here: `Create Coupon Webhook Payload`_.

.. _Create Coupon Webhook Payload: https://www.talkable.com/api-docs/index.html?urls.primaryName=Webhooks#/Create%20Coupon%20Webhook/post_yourApiCreateCouponWebhookPath

.. container:: hidden

   .. toctree::
