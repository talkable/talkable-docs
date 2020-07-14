.. _api_v2/flow:
.. include:: /partials/common.rst

.. meta::
   :description: This flow helps to integrate with Talkable via API for a default store or service.

Referral Program via API
========================

This flow helps to integrate with Talkable via API for a default Store or Service.
It shows how you can do the following actions via API:

* Generate Talkable Offer
* Share An offer via Social Network or Email
* Build an Offer Claim Page on your side
* Let Talkable know about Purchase or Event to let it trigger the referral

Each of this steps can be done individualy or all together to achive API integration

Initial Origin
--------------

Invite |advocate| to referral program at some point by creating an :ref:`Origin <api_v2/origins>` and obtaining :ref:`Offer <api_v2/offers>` to share.

Displaying and Sharing the offer
--------------------------------

Display options for |advocate| to share with their |friend|\s.

**For Social Share**

- Retrieve unique links for each channel for :ref:`Offer <api_v2/offers>` (`claim_urls` interpolation)
- After |advocate| have shared, make corresponding request to :ref:`Shares <api_v2/shares>` endpoint

**For Email Share**

- Ask |advocate| for recipients (and additional information) and make request to :ref:`Shares <api_v2/shares>` endpoint

Claiming an Offer
-----------------

In order for |friend| to get referred, they go to the Claim (or Landing) page by following the share URL.

This is last step before |friend| proceeds to your site or app.

- Edit your :ref:`Friend Claim Page <campaigns/views/offers_claim>` template or disable it for immediate redirect
- Edit the Destination URL in *Extra* window

**Important:**

You need to pass the visitor `uuid` variable to your site via destination URL GET paramter and store it somewhere in order to later pass it with :ref:`Origin <api_v2/origins>`

Example destination URL: `http://merchant.com?tkbl_cvuuid={{visitor_uuid}}&utm_source=talkable&...`

Submit Origin data to talkable to generate the referral
-------------------------------------------------------

Once any user makes an action which implies possible close of a referral chain, send an :ref:`Origin <api_v2/origins>`. Please include `uuid` in this request if possible.

For example, if |friend| makes a purchase on your site or installs your app — |advocate| needs to be rewarded, and this is achieved with creating :ref:`Purchase or Event <api_v2/origins>` which gets linked to previously created |advocate| offer.
