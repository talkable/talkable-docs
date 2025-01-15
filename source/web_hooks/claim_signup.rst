.. _web_hooks/claim_signup:
.. include:: /partials/common.rst

.. meta::
  :description: Friend Email Gating Webhook notifies your endpoint that Friend email gating form was submitted.

Friend Email Gating Webhook
===========================

The Talkable Friend Email Gating Webhook notifies your endpoint that a Friend
Email Gating form was submitted (on Friend Claim Page).

Use cases for the Friend Email Gating Webhook include:

* Tracking when users select the checkbox to opt into your email newsletter
* Collection of data for Business Intelligence and analytics systems to track
  users who become Friends
* Sending automated ‘Thank You’ or 'Don’t forget to shop' emails after a Friend
  passes the email gating form

.. raw:: html

  <h2>When does Talkable call the Friend Email Gating Webhook?</h2>

Talkable Friend Email Gating Webhook is triggered any time an Friend Email
Gating form is submitted. This is the form a Friend completes after receiving
a share from an Advocate, and before receiving their discount code.

Friend Email Gating form example:

.. image:: /_static/img/friend_email_gating_form.png
  :alt: Friend Email Gating Form
  :class: is-minimal

.. raw:: html

  <h2>Payload parameters provided</h2>

The sample payload with parameters for Friend Email Gating Webhook is available here: `Friend Email Gating Webhook Payload <https://www.talkable.com/api-docs/index.html?urls.primaryname=webhooks%20api&urls.primaryName=Webhooks#/Friend%20Email%20Gating/post_your_api_claim_signup_web_hook_path>`_.

.. container:: hidden

  .. toctree::
