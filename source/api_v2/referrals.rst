.. _api_v2/referrals:
.. include:: /partials/common.rst

.. meta::
   :description: The Talkable Referrals API allows referrals to be approved or to be voided.

Referrals
=========

The Talkable |api_v2_referrals| allows referrals to be approved or voided.

.. raw:: html

   <h2>Example use cases for the Referrals API</h2>

**Voiding referrals after a purchase is returned or canceled:**

* A company who wants to ensure an |advocate| does not receive referral Rewards
  if the |friend| returns their purchase. To prevent the |advocate| from receiving
  their referral reward, this company would call the Talkable |api_v2_referrals| with
  ``{"status": "voided"}`` after the |friend| order is canceled.

**Approving Referrals only after a specific CRM Event:**

* A company who wants to approve referral rewards only after the |friend| order
  has reached a certain state (ie, 'shipped’, or ‘no longer refundable’) can
  control this Referral Approval with the Talkable |api_v2_referrals|. This company
  would call the Talkable |api_v2_referrals| with ``{"status": "approved"}`` after
  the |friend| order reaches the desired state.

.. note::

   There is no need to filter the orders for which the Talkable |api_v2_referrals| is
   called. Call Talkable’s |api_v2_referrals| for all purchases, not just those
   associated with a referral purchase. Talkable will decide which order numbers
   are tied to referrals.

   Also: Inside ‘Fraud Settings’ exists two options for Referrals Approval
   configuration. When ‘Automatic’ Referrals Approvals selected, eligible
   Referrals will be approved a fixed number of hours or days (per configuration)
   after the |friend| Purchase and/or Conversion Event. When ‘Manual’ Referrals
   Approval is selected, referral rewards will only be paid out after either the
   Talkable |api_v2_referrals| is called with ``{"status": "approved"}`` or after an
   Admin has approved the referral from inside the Talkable Customer Service
   Portal.
