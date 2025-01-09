.. _web_hooks/offer_signup:
.. include:: /partials/common.rst

.. meta::
   :description: Advocate Signup Webhook notifies your endpoint of an Advocate signup forms submission.

Advocate Signup Webhook
=======================

The Talkable Advocate Signup Webhook notifies your endpoint of an Advocate
Signup forms submission.

Use cases for the Advocate Signup Webhook include:

* Tracking when users select the checkbox to opt into your email newsletter
* Collection of data for Business Intelligence and analytics systems to track
  users who become Advocates
* Sending automated ‘Thank You’ emails after a user becomes an Advocate

.. raw:: html

  <h2>When does Talkable call the Advocate Signup Webhook?</h2>

Talkable Signup Webhook is triggered any time an Advocate Signup Form is
submitted. The Advocate Signup Form is the standard Name & Email (with optional
email subscription checkbox) fields a user submits before becoming an Advocate
and sharing an offer with Friends.

Advocate Signup Form example:

.. image:: /_static/img/advocate_signup_form_webhook.png
  :alt: Advocate Signup Form,
  :class: is-minimal

.. raw:: html

  <h2>Payload parameters provided for Advocate Signup Webhook</h2>

The sample payload with parameters for Advocate Signup Webhook is available here: `Advocate Signup Webhook Payload <https://www.talkable.com/api-docs/index.html?urls.primaryname=webhooks%20api&urls.primaryName=Webhooks#/Advocate%20Signup/post_your_api_advocate_signup_web_hook_path>`_.

.. container:: hidden

  .. toctree::
