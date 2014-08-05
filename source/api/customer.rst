.. _api/customer:
.. include:: /partials/common.rst

Customer API
============

.. include:: /partials/note_preliminary_api.rst

Retrieving Customer Referral Information
----------------------------------------

.. code-block:: url

   GET https://www.talkable.com/api/v1/sites/<site_slug>/customers/<customer_email>/stats.json?api_key=<api_key>

Get information about a customer and the status of their referrals.

.. raw:: html

   <h3>Parameters</h3>

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   api_key           Your API key. You can manage your API key in the Account
                     Settings.
   customer_email    The customer's email address.
   ================= ========================================================

.. raw:: html

   <h3>Response codes</h3>

* 200 OK - Everything worked as expected
* 404 Not Found - The requested item doesn't exist

.. raw:: html

   <h3>Sample request</h3>

This is a sample request for a subscription that was referred from another subscriber.

.. code-block:: url

   GET https://www.talkable.com/api/v1/sites/my-store/customers/customer%40example.com/stats.json?api_key=CRljoG5Glb8xeNCv1NO

.. code-block:: javascript

   {
     "total_rewards_earned": "$0.00",
     "customer_id": "2",
     "first_share_date": "2011-03-07T04:59:49Z",
     "share_link": "http://www.curebit.com/x/kLxLY",
     "email": "customer@example.com",
     "total_rewards_paid": "$0.00",
     "last_share_date": "2011-03-09T19:48:21Z",
     "total_rewards_unpaid": "$0.00",
     "first_redeem_date": null,
     "total_clicks": 1,
     "share_facebook_link": "http://www.curebit.com/x/jA52z",
     "last_redeem_date": null,
     "total_shares": 2,
     "share_twitter_link": "http://www.curebit.com/x/O71gp",
     "created_at": "2011-03-06T20:59:44-08:00",
     "total_redeems": 0,
     "share_email_link": "http://www.curebit.com/x/4GZTs"
   }

.. container:: hidden

   .. toctree::
