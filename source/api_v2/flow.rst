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

Each of these steps can be done individually or all together to achieve API integration

.. note::

   Offers created via API are not marked as shown and thus are not counted towards advocate impressions.

Initial Origin
--------------

Invite |advocate| to referral program at some point by creating an |api_v2_origin| and obtaining |api_v2_offer| to share.

Displaying and Sharing the Offer
--------------------------------

Display options for |advocate| to share with their |friend|\s.

**For Social Share**

- Retrieve unique links for each channel for |api_v2_offer| (`claim_urls` interpolation)
- After |advocate| have shared, make corresponding request to |api_v2_share_via_social_channel|

**For Email Share**

- Ask |advocate| for recipients (and additional information) and make request to |api_v2_share_via_email|

Claiming an Offer
-----------------

In order for |friend| to get referred, they go to the Claim (or Landing) page by following the share URL.

This is the last step before |friend| proceeds to your site or app.

- Edit your :ref:`Friend Claim Page <campaigns/views/offers_claim>` template or disable it for immediate redirect
- Edit the Destination URL in *Extra* window

**Important:**

You need to pass the visitor `uuid` variable to your site via the destination URL GET parameter and store it somewhere in order to later pass it with |api_v2_origin|

Example destination URL: `http://merchant.com?tkbl_cvuuid={{visitor_uuid}}&utm_source=talkable&...`

Submit Origin data to Talkable to generate the Referral
-------------------------------------------------------

Once any user makes an action that implies a possible close of a referral chain, send an |api_v2_origin|. Please include `uuid` in this request if possible.

For example, if |friend| makes a purchase on your site or installs your app — |advocate| needs to be rewarded, and this is achieved with creating :ref:`Purchase or Event <api_v2/origins>` which gets linked to previously created |advocate| offer.
