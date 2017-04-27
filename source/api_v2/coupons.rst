.. _api_v2/coupons:
.. include:: /partials/common.rst

Coupons
=======

This API allows you to access and check coupons. See examples below.

|br|

.. code-block:: text

   GET /coupons/:code

Returns a coupon information.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   code              Coupon code
   ================= ========================================================

|br|

.. code-block:: text

   GET /coupons/:code/permission/:email

Checks if given coupon code belongs to given person.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   code              Coupon code
   email             Person’s email
   ================= ========================================================

Example
-------

Find a coupon by code
.....................

.. code-block:: text

   GET https://www.talkable.com/api/v2/coupons/COUPON_CODE?site_slug=my-store&api_key=i9uil7nQgDjucCiTJu

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "talkable_coupon": true,
       "coupon": {
         "id": 233,
         "code": "COUPON_CODE",
         "single_use": false,
         "expires_at": "2017-05-03T07:41:30.000-07:00",
         "amount": 10.0,
         "percentage_discount": false
       },
       "associated_reward": {
         "created_at": "2017-04-26T07:41:31.000-07:00",
         "person": {
           "personal_claim_url": "http://share.mystore.com/by/customer@example.com",
           "events_count": 0,
           "first_name": "John",
           "last_name": "Smith",
           "email": "customer@example.com",
           "username": null,
           "unsubscribed_at": null,
           "subscribed_at": null,
           "sub_choice": false,
           "gender": null
         },
         "campaign": {
           "id": 196,
           "name": "Deal for friends",
           "tag_names": ["invite"],
           "joinable_category_names": ["affiliate_member"],
           "origin_min_age": null,
           "origin_max_age": null,
           "new_customer": null,
           "slug": 196,
           "type": "Standalone Campaign",
           "is_active": true
         },
         "incentive": {
           "amount": 10.0,
           "description": "$10",
           "percentage": false,
           "incentive_type": "discount_coupon",
           "action_type": "click",
           "identifier": "click",
           "for_advocate": false,
           "for_friend": true,
           "criteria_config": {
             "new_customer": null,
             "allow_on_expired_offer": false,
             "allow_on_self_referral": false,
             "has_liquid_criteria": false
           },
           "coupon_expires_at": "2017-05-03T07:41:30.000-07:00"
         }
       }
     }
   }

When coupon was not given by Talkable:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "talkable_coupon": false
     }
   }

Check if a coupon belongs to a person
.....................................

.. code-block:: text

   GET https://www.talkable.com/api/v2/coupons/COUPON_CODE/permission/user@example.com?site_slug=my-store&api_key=i9uil7nQgDjucCiTJu

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "allowed": false,
       "talkable_coupon": true,
       "error_message": "This coupon code has been issued to another email address",
       "checks": {
         "coupon_unissued": false,
         "coupon_expired": false,
         "friend_offer_expired": false,
         "different_owner": true,
         "coupon_used": false,
       },
       "coupon": {
         "id": 233,
         "code": "COUPON_CODE",
         "single_use": false,
         "expires_at": "2017-05-03T07:41:30.000-07:00",
         "amount": 10.0,
         "percentage_discount": false
       },
       "associated_reward": {
         "created_at": "2017-04-26T07:41:31.000-07:00",
         "person": {
           "personal_claim_url": "http://share.mystore.com/by/customer@example.com",
           "events_count": 0,
           "first_name": "John",
           "last_name": "Smith",
           "email": "customer@example.com",
           "username": null,
           "unsubscribed_at": null,
           "subscribed_at": null,
           "sub_choice": false,
           "gender": null
         },
         "campaign": {
           "id": 196,
           "name": "Deal for friends",
           "tag_names": ["invite"],
           "joinable_category_names": ["affiliate_member"],
           "origin_min_age": null,
           "origin_max_age": null,
           "new_customer": null,
           "slug": 196,
           "type": "Standalone Campaign",
           "is_active": true
         },
         "incentive": {
           "amount": 10.0,
           "description": "$10",
           "percentage": false,
           "incentive_type": "discount_coupon",
           "action_type": "click",
           "identifier": "click",
           "for_advocate": false,
           "for_friend": true,
           "criteria_config": {
             "new_customer": null,
             "allow_on_expired_offer": false,
             "allow_on_self_referral": false,
             "has_liquid_criteria": false
           },
           "coupon_expires_at": "2017-05-03T07:41:30.000-07:00"
         }
       }
     }
   }

When coupon was not given by Talkable:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "allowed": true,
       "talkable_coupon": false
     }
   }

.. container:: hidden

   .. toctree::
