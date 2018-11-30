.. _api_v2/referrals:
.. include:: /partials/common.rst

Referrals
=========

The Talkable Referrals API allows referrals to be approved or voided. 

.. raw:: html

   <h2>Example use cases for the Referrals API</h2>

.. raw:: html

**Voiding referrals after a purchase is returned or cancelled:**

* A company who wants to ensure an |Advocate| does not receive referral Rewards if the |Friend| returns their purchase. To prevent the |Advocate| from receiving their referral reward, this company would call the Talkable Referrals API with ``{"status": "voided"}`` after the |Friend| order is canceled.  

.. raw:: html

**Approving Referrals only after a specific CRM Event:**

* A company who wants to approve referral rewards only after the |Friend| order has reached a certain state (ie, 'shipped’, or ‘no longer refundable’) can control this Referral Approval with the Talkable Referrals API. This company would call the Talkable Referrals API with ``{"status": "approved"}`` after the |Friend| order reaches the desired state




.. note:: There is no need to filter the orders for which the Talkable Referrals API is called. Call Talkable’s Referrals API for all purchases, not just those associated with a referral purchase. Talkable will decide which order numbers are tied to referrals. |br| |br| Also: Inside ‘Fraud Settings’ exists two options for Referrals Approval configuration. When ‘Automatic’ Referrals Approvals selected, eligible Referrals will be approved a fixed number of hours or days (per configuration) after the |Friend| Purchase and/or Conversion Event. When ‘Manual’ Referrals Approval is selected, referral rewards will only be paid out after either the Talkable Referrals API is called with ``{"status": "approved"}`` or after an Admin has approved the referral from inside the Talkable Customer Service Portal.



|br|

.. code-block:: text

   PUT /origins/<origin_slug>/referral

Updates referral's status.

.. note:: Approved or voided referrals cannot be changed to the opposite state.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   origin_slug       If origin is a *Purchase*:

                     ``order_number``, e.g.:
                     ``"B00K2EOONI"``

                     If origin is an *Event*:

                     ``event_category``:``event_number``, e.g.:
                     ``"newsletter_subscription:42"``

   data              JSON object with ``status`` property.

                     E.g. ``{"status": "approved"}`` or  ``{"status": "voided"}``

   ================= ========================================================

Example
-------

Approve a Referral
..................

.. code-block:: bash

   curl -H "Content-Type: application/json" \
        -X PUT \
        -u i9uil7nQgDjucCiTJu: \
        -d '{"site_slug":"my-store","data":{"status":"approved"}}' \
        https://www.talkable.com/api/v2/origins/B00K2EOONI/referral
