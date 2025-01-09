.. _api_v2/origins:
.. include:: /partials/common.rst

.. meta::
   :description: The Talkable Origins API allows the registration of “off-site” or “backend” purchases, or CRM events. That means they can be used in the referral flow.

Origins
=======

The Talkable |api_v2_origins| allows the registration of ‘off-site’ or ‘backend’
purchases or CRM events so they can be used in the referral flow. This
functionality is generally utilized by businesses using subscription billing,
off-site transactions, or other off-site events.

.. note::

  The :ref:`standard front-end <integration/custom/overview>` Talkable
  integration will capture all one-time purchases happening on the client
  e-commerce site, but will not on its own capture purchases or CRM events
  happening on the backend. To do this, the |api_v2_origins| must be utilized to
  feed ‘off-site’ or ‘backend’ purchases or CRM events to Talkable.

.. raw:: html

  <h2>Example use cases for the Origins API</h2>

**Subscription:**

* A company whose customers sign up for a monthly service by making an initial
  ‘on-site’ payment, then are charged monthly on the backend for subsequent
  subscription payments. This company would like to reward |advocate| users
  (referrers) with a reward after their |friend| has been a member for three
  billing cycles.

  * Talkable’s :ref:`standard front-end <integration/custom/overview>`
    integration captures the initial ‘on-site’ payment.

  * For Talkable to reward the |Advocate| after the third billing cycle of the
    |friend| subscription, the Company must pass the subsequent subscription
    data to Talkable’s |api_v2_origins| using ``"type": "Event"``.

**Off-Site Events:**

* A company whose customers purchase product or perform events off-site. This
  company would like to reward |advocate| users (referrers) with a reward after
  their |friend| has purchased a product in the brick and mortar store, or
  attended an in-person appointment.

  * Talkable’s :ref:`standard front-end <integration/custom/overview>`
    integration captures an initial ‘on-site’ signup event if there is one.

  * For Talkable to reward the |advocate| after the in-person |friend| store
    purchase, or appointment attendance, the Company must pass the in-store
    purchase, or appointment attendance data to Talkable’s |api_v2_origins| with
    either ``"type": "Purchase"`` for a purchase or ``"type": "Event"`` for an
    appointment attendance.

**User Approval:**

* User approval use cases start with customers who need to submit an application
  by performing an initial ‘on-site’ sign-up event. This company would like to
  reward |advocate| users (referrers) with a reward after their |friend|
  application is approved.

  * Talkable’s :ref:`standard front-end <integration/custom/overview>`
    integration captures the initial ‘on-site’ application sign-up event.

  * In order for Talkable to reward the |advocate| after the |friend|
    application approval, the Company must pass the approval data to Talkable’s
    |api_v2_origins| using ``"type": "Event"``.
