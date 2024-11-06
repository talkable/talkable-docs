.. _advanced_features/rybbon:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate Rybbon with your Talkable system to generate gift claim links and manage campaign-specific rewards.

Rybbon
======

Overview
--------

This documentation provides a guide on integrating the Rybbon campaign with your Talkable system. By enabling this feature, you can generate gift claim links for users and customize reward amounts based on campaign settings.

.. note::
   Rybbon app must be installed and enabled for this integration to work.

Functionality
-------------

The Rybbon integration allows you to make a claim request within the scope of a specific campaign key and returns a gift claim link.

Example Usage
-------------

1. **Generating a Gift Claim Link**

   Takes a campaign key of a Rybbon Talkable campaign to generate a claim link.

   .. code-block:: liquid

      {{ "a9a3472f4ea858758e0cd686de8408e2" | rybbon }}

   This returns a link similar to:
   `https://www.rybbon.net/redeem.php?claimcode=ee645de47765bdbede751c8c6f08a619`

2. **Custom Reward Amount for Rybbon Campaigns**

Allows setting a custom reward amount for Rybbon campaigns with variable denomination. The minimum amount conforms to specific Rybbon gift card restrictions, and the maximum is 50.

.. code-block:: liquid

   {{ "a9a3472f4ea858758e0cd686de8408e2" | rybbon: amount: 13.5 }}

Limitations
-----------

- Minimum and maximum reward amounts vary based on the specific Rybbon gift card settings.
- Custom reward amounts must not exceed the maximum value of 50.

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.