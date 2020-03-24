.. _web_hooks:
.. include:: /partials/common.rst

.. meta::
   :description: Webhooks are triggered by events on Talkable’s site.

Webhooks
########

Webhooks are "user-defined HTTP callbacks" triggered by events on Talkable’s
site. Subscribing to Talkable Webhooks allows you to receive notifications about
various events from Talkable, for example, when a Reward should be given, or
when a Friend or Advocate opts in to an email newsletter subscription.

After subscribing to a Webhook, your app can execute code immediately after
specific events occur in Talkable.

http://en.wikipedia.org/wiki/Webhook

Each Webhook in Talkable is defined with an HTTP URL to deliver Webhook data
(aka payload). This URL should be defined and implemented on the client’s site.

.. raw:: html

   <h2>Available Webhooks</h2>

Below is a user experience flow showing when Talkable Webhooks are called.
For more details concerning specific Talkable Webhooks, click the appropriate
Webhook type in the left-hand menu.

.. image:: /_static/img/flowchart_webhooks_1.png
   :alt: Webhooks Flowchart
   :class: is-minimal

.. note::

   The Reward Webhooks will only send if there is an associated incentive
   configured. For example, for the 'Reward Webhook' (reason = signup) to send,
   there must be a signup incentive configured in the campaign rules.

.. raw:: html

   <h2>Set Up</h2>

.. image:: /_static/img/menu_webhooks_screenshot.png
   :alt: Webhooks Menu Item
   :class: is-minimal

1. Set up and test Talkable Webhooks by navigating to **Menu** then **Webhooks**
2. Proceed to **Create New Webhook**
3. Choose a Webhook from the dropdown and provide your endpoint URL
4. From here, Send Sample, Edit, Delete or Create New
5. Take note of your Talkable security key. This key will be the same for all
   Talkable Webhooks on a given site. Talkable includes a key parameter in
   Webhooks which are unique to each site as a way to identify Talkable as
   an authorized server. Your Talkable Webhook security key can be found in
   the Webhook set up page.

Talkable Webhooks will trigger automatically based on associated events defined
by Webhook type.

.. raw:: html

   <h2>Testing</h2>

Testing webhooks can be accomplished with the help of Webhook Tester, an external
service that tests your post-receive messages.

1. Visit `Webhook Tester`_ and click **Copy** to copy the URL you are given.
2. Open your site on Webhooks set up page.
3. Click **New**.
4. Select webhook type.
5. Paste your Webhook Tester URL and save.
6. Click **Deliver Sample** near the webhook you want to test.
7. After you finish the implementation on your site **change Webhook Tester URL
   to the live URL** on your site.
8. Click **Deliver Sample** to test webhook with Live URL.

.. raw:: html

   <h2>Data</h2>

All Webhooks are delivered as an HTTP Post request with the main parameter
called payload. All data inside this parameter is encoded as JSON. Below is
a PHP parameter decode example:

.. code-block:: php

   json_decode($_POST["payload"])

.. raw:: html

   <h2>Parsing Timestamps</h2>

**Timestamp data type** is not a part of JSON standard. Timestamps
are passed as strings in |iso8601| compatible format. To function properly, ensure
your date parser is compatible to this standard. Java users go here: |br|
http://stackoverflow.com/questions/2201925/converting-iso8601-compliant-string-to-java-util-date

.. raw:: html

   <h2>Response Codes</h2>

Talkable considers a Webhook as "delivered successfully" when a site
server returns a **2xx response status**. Otherwise Talkable will continually
retry to deliver a Webhook after a set interval of time.

.. raw:: html

   <h2>HTTP Responses and Their Meanings</h2>

* 2xx: Success
* 200: OK
* 201: Created
* 202: Accepted
* 203: Non Authoritative Information
* 204: No Content
* 205: Reset Content
* 206: Partial Content

If you have a problem on your server, you can answer with code 500. If there is
some problem in our request (problem on Talkable’s side), you can answer
"400 Bad Request".

Talkable will retry delivery of Webhook if any other error code is received.

.. raw:: html

   <h2>Security Key</h2>

Talkable includes a ``key`` parameter in Webhooks which are unique to each site
as a way to identify Talkable as an authorized server. Your Talkable Webhook
security key can be found in the Webhook set up page.

.. raw:: html

   <h2>Type</h2>

The ``type`` parameter of a Webhook request can be used to identify which Webhook
is received without looking at the payload. This will be useful if you point multiple
Webhooks to the same URL; for instance, for data collection purposes.

Possible types are:

* ``referral_web_hook``
* ``create_coupon_web_hook``
* ``post_share_web_hook``
* ``offer_signup_web_hook``
* ``claim_signup_web_hook``
* ``reward_web_hook``
* ``unsubscribe_web_hook``
* ``check_unsubscribe_web_hook``
* ``event_web_hook``

.. raw:: html

   <h2>Site</h2>

Every Webhook has a ``site`` parameter that identifies which Talkable site sent
this request. This is useful if you have a multi-site setup or use a staging site.

.. raw:: html

   <h2>Whitelisting Talkable IPs</h2>

In case your servers are behind firewall, you may need to whitelist Talkable IP
addresses so webhooks can be delivered.  Pass list of these addresses to your network administrator:

* 100.26.94.244
* 18.207.91.200
* 184.73.206.68
* 23.21.155.129
* 3.226.56.48
* 3.82.131.34
* 34.195.139.227
* 34.197.54.191
* 34.226.253.236
* 34.231.104.179
* 34.234.27.220
* 35.169.186.170
* 35.171.77.58
* 35.173.174.244
* 50.17.244.178
* 52.2.244.36
* 52.22.0.55
* 52.44.214.85
* 52.45.68.245
* 52.6.41.1
* 52.7.94.243
* 54.162.235.87
* 54.164.128.44
* 54.208.14.192
* 54.86.208.153

.. raw:: html

   <h2>Compatibility and Versioning</h2>

Talkable Webhooks do not currently incorporate versioning. Current spec will not
be changed for all existing hooks. Note that Talkable may add additional data
elements to existing Webhooks, but should not remove or change existing data
elements.

|hr|
See available Webhooks on the navigation sidebar.

.. _`Webhook Tester`: https://webhook.site/

.. container:: hidden

   .. toctree::

      Create Coupons <web_hooks/create_coupon>
      Referral <web_hooks/referral>
      Reward <web_hooks/reward>
      Post Share <web_hooks/post_share>
      Advocate Signup <web_hooks/offer_signup>
      Friend Email Gating <web_hooks/claim_signup>
      Unsubscribe <web_hooks/unsubscribe>
      Check Unsubscribe <web_hooks/check_unsubscribe>
      Event <web_hooks/event>
