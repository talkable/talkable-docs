.. _optional/verification_digest:
.. include:: /partials/common.rst

Verification Digest
===================

Summary
-------

Purchases and events are passed via JavaScript to Talkable. It is possible to secure this data transmission by using Talkable's Verification Digest. The Verification Digest acts as a checksum which will ensure that any event or purchase that’s being registered is coming from the authorized source only. This process includes hashing a **salt** http://en.wikipedia.org/wiki/Salt_(cryptography) with the ordinary purchase data that’s being passed over. The salt will be a random string that is shared between the two parties and is kept private. Talkable provides a method that will allow you to encrypt your (salt + purchase data) combo via SHA-256 which will output the encrypted Verification Digest string which can then be passed freely over JavaScript which Talkable will use to authorize requests. Only when Talkable is able to successfully decrypt the verification digest with the shared salt will the data be registered.

| Documentation: http://docs.talkable.com/ecommerce/verification_digest.html
| Java Source: https://gist.github.com/bogdan/811591b1c7f36f3a28fb

Instruction
-----------

In order to take advantage of the verification digest, you will need to import the Java source above, or copy & make use of the public methods included.  The example Java Source above also contains an example on how to create the verification digest. As demonstrated below, you will call the verification_digest method and provide the salt + purchase order details. The returned digest can now be safely passed via JS to the verification_digest parameter which is passed as part of the order details object [as seen in `Passing a digest`_].

Generating a digest
-------------------

In the example code below we are simply calling the verification_digest method which takes parameters {salt/key, event type, order #, email, amount, coupons} and returns the hashed checksum which is used as the verification digest.

.. code-block:: java

    public static void main(String []args)
    throws UnsupportedEncodingException, NoSuchAlgorithmException {
      String[] codes = { "ONE", "TWO" };
      String digest = verification_digest("ef591fbbc527d77402d9a10dba92c195", "purchase",
          "100011", ”customer@example.com", "200.00", "2014-01-01T00:00:00+00:00", codes);
    }


Passing a digest
----------------

In the example code below we are passing Verification Digest string to Talkable in verification_digest parameter.

.. code-block:: javascript

    var _talkable_data = {
      purchase: {
        order_number: '100011', // REQUIRED - Order number
        subtotal: '23.97', // REQUIRED - Purchase Subtotal
        coupon_code: 'SAVE20' // REQUIRED - Coupon code used at checkout, multiple coupons allowed as JS array: ['SAVE20', 'FREE-SHIPPING']. Pass null if there is no coupon code.
      },
      customer: {
        email: 'customer@example.com'
      },
      verification_digest: '60a511b9d8d45fe2ea8568e21138f517761be05ffda693135c68c2ec551ee507'
    }

Digest generation algorithm
---------------------------

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
