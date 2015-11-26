.. _ecommerce/custom:
.. include:: /partials/common.rst

Other Platform
==============

.. include:: /partials/note_enterprise_integration.rst

Site Placements
---------------

It is all about the referral loop. Define a place where do you want your customers see Talkable campaign at. This is a place from where they will be inviting their friends — we call it "opening the loop":
  1. On the order confirmation page after checkout
  2. On the standalone page that's always available to anyone
  3. Both **(recommended)**. The more places you integrate Talkable into the more boost you get from referrals channel.

1. Basic Integration
--------------------

Post Purchase
~~~~~~~~~~~~~

This is a **required** placement because it acts as both opener and closer of the referral loop. On your final checkout receipt page (which includes things like the customer's
order number or confirmation code) you will pass customer order data to Talkable. Passing order data is required in order to verify validity of referrals and exclude any possibility of fraud.

Below is an example of the very basic Post Purchase integration.

.. include:: /samples/ecommerce/custom/syncronous.rst

`Example of the Post Purchase integration <http://learn.talkable.com/docs/pp-basic>`_

Standalone
~~~~~~~~~~

This is an optional site placement which only acts as the referral loop opener. From here all your customers can invite their friends to participate in the referral program. There is no need to make a purchase in order to see Standalone campaign.

Usually this page has www.site.com/**invite** URL and is linked from the main site navigation at the top.

Below is an example of the very basic Standalone integration.

.. include:: /samples/standalone/basic.rst

|hr|

2. Advanced Integration
-----------------------

Here is a full list of things you can do with Talkable:

1. :ref:`Pass custom user data <optional/passing_custom_data>`
2. :ref:`Separate your users into segments with Traffic Source <optional/traffic_source>`

