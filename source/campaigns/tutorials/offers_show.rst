.. _campaigns/tutorials/offers_show:
.. include:: /partials/common.rst

.. meta::
   :description: Instant reward campaign lets you reward your brand Advocate immediately — right after a referral link to a Friend was sent.

Advocate Signup/Share Page
-------------------

.. _tutorials_instant_reward:

Instant Reward
..............

Instant reward campaign is used when we need to reward RR immediately
after he shares. If RR redemption email is turned on it will be sent
right after successful share. The most popular share channel is
Facebook.

To make instant reward work you need to use FB App share instead of a
default sharer.php.
Also make sure **RR social sharing incentive** is set.

After that we need to setup Advocate Signup/Share Page with the following markup:

.. include:: /samples/liquid/offers_show/instant_reward_basic.rst

If you need to hide/show some information when shared and copy code on
click here is more advanced setup:

.. include:: /samples/liquid/offers_show/instant_reward_advanced.rst

.. _tutorials_cloudsponge:

CloudSponge Integration
.......................

.. include:: /samples/liquid/offers_show/cloudsponge.rst

**CloudSponge and Custom Domain**

CloudSponge integration is bound to specific domain. In order to use it with
custom domain you’ll need to obtain separate ``domain_key``.

#. Go to `CloudSponge <https://www.cloudsponge.com/>`_
#. Add new domain, use your custom domain as domain name
#. Copy & Paste new ``domain_key`` to your template

.. _tutorials_multiple_email_fields:

Multiple Email Fields
.....................

.. include:: /samples/liquid/offers_show/multiple_emails.rst

.. _tutorials_linkedin:

LinkedIn
........

**Separate Wording**

.. include:: /samples/liquid/offers_show/linkedin_opengraph.rst

**Basic Setup**

.. include:: /samples/liquid/offers_show/linkedin_basic.rst

**Advanced Setup**

.. include:: /samples/liquid/offers_show/linkedin_advanced.rst
