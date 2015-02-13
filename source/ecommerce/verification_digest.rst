.. _ecommerce/verification_digest:
.. include:: /partials/common.rst

Verification Digest
===================

Talkable is able to verificate each request comming from web browser.
It prevents fraud request from a potential attacker that can form a request to Talkable 
platform to register a event that doesn't exist on Merchant Side.

JS requests don't have any security by default and can be easily faked.
In order to verify each request there is a need to attach a "control sum" to each event registration request
with `verification_digest` parameter.

In order to do that merchant needs to pass us a control sum of the the request parameters that only matches only current parameters:

.. code-block:: javascript

    var _curebit_order_details = {
       order_number: '100011', // REQUIRED - Order number
       order_date: '2014-04-15T08:18:44+00:00', // REQUIRED - Order Date and Time (ISO 8601 formatted datetime)
       email: 'customer@example.com', // REQUIRED - Customer Email Address
       subtotal: '23.97', // REQUIRED - Purchase Subtotal
       coupon_code: 'SAVE20', // REQUIRED - Coupon code used at checkout, multiple coupons allowed as JS array: ['SAVE20', 'FREE-SHIPPING']. Pass null if there is no coupon code.
       ...
       verification_digest: '60a511b9d8d45fe2ea8568e21138f517761be05ffda693135c68c2ec551ee507'
    }


Control sum generation algorithm needs to be kept in secret from potential attacker.
That is why verifiction_digest should be generated only in backend.

In order to generate it, merchant needs to form a request verification string with request parameters and a "salt" and encode it with SHA-256 algorithm.
Salt is a secret key that can be obtained in site setting after enabling "Verification Digest" feature.
Example salt looks like:

3c34e72917aba5885f75f8ae300d195e

Here is example:
Suppose we have a purchase creation request with the following parameters:

* event_category: 'purchase'
* order_number: '100011'
* email: example@customer.com
* subtotal: 83.32
* order_date: 2014-01-01T15:30:24+00:00
* coupon_code: EFF-32 and FREE-SHIPPING (2 code for single purchase)

In this case:

* Verification String: `3c34e72917aba5885f75f8ae300d195e|100011|purchase|example@customer.com|83.32|2014-01-01T15:30:24+00:00|EFF-32,FREE-SHIPPING`
* Verfication Digest:  `23872240ee24867de082ce26c3baef821100e89be43d4d359f5c52fb4bad75b6`

If some of the parameters above is blank, than it should not be included in request verification string:

For example: if order_date is null, the request verification string looks like:

* Verification String: `3c34e72917aba5885f75f8ae300d195e|100011|purchase|example@customer.com|83.32|EFF-32,FREE-SHIPPING`
* Verfication Digest:  `a5dc18fcb8f53f20d935b1cd1e83b9967d51fc6297cfe1d90af4f6d78a7a484b`

If there is no coupons associated with a purchase, the request verification string looks like:

* Verification String: `3c34e72917aba5885f75f8ae300d195e|100011|purchase|example@customer.com|83.32|2014-01-01T15:30:24+00:00`
* Verfication Digest:  `9fb8c6ecfa1eb82a4ea91fe67cd1866ffda6271d956ddf2ce22b48b47fdaf53c`




