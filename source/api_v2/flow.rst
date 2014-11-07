.. _api_v2/flow:
.. include:: /partials/common.rst

Flow
====

Initial Origin
--------------

Invite |advocate| to referral program at some point by creating an :ref:`Origin <api_v2/origins>` and obtaining :ref:`Offer <api_v2/offers>` to share.

Share Screen
------------

Display options for |advocate| to share with their |friend|\s.

**For Social Share**

- Retrieve unique links for each channel for :ref:`Offer <api_v2/offers>` (`claim_urls` interpolation)
- After |advocate| have shared, make corresponding request to :ref:`Shares <api_v2/shares>` endpoint

**For Email Share**

- Ask |advocate| for recipients (and additional information) and make request to :ref:`Shares <api_v2/shares>` endpoint

Claim Screen
------------

In order for |friend| to get referred, they go to the Claim (or Landing) page by following the share URL.

This is last step before |friend| proceeds to your site or app.

- Edit your :ref:`Friend Claim Page <campaigns/views/offers_claim>` template or disable it for immediate redirect
- Edit the Destination URL in *Extra* window

Tips:

- You may pass any data through GET parameters of URL
- You may want to pass the `visitor_uuid` variable to your site or app and store it somewhere in order to later pass it with :ref:`Origin <api_v2/origins>`

Closing Origin
--------------

Once any user makes an action which implies possible close of a referral chain, send an :ref:`Origin <api_v2/origins>`. Please include `uuid` in this request if possible.

For example, if |friend| makes a purchase on your site or installs your app — |advocate| needs to be rewarded, and this is achieved with creating :ref:`Purchase or Event <api_v2/origins>` which gets linked to previously created |advocate| offer.
