.. _web_hooks/post_share:
.. include:: /partials/common.rst

.. meta::
  :description: Post Share Webhook provides notification of share events performed within a referral campaign workflow.

Post Share Webhook
==================

Talkable Post Share Webhook provides notification of a share event performed within a referral campaign workflow. Use cases for the Post Share Webhook include:
  - Sending automated 'Thank You' email to an Advocate for performing a share
  - Any event that should be triggered when a user shares
  - Data for Business Intelligence and analytics systems

.. raw:: html

  <h2>When does Talkable call the Post Share Webhook?</h2>

Talkable Post Share Webhook is triggered any time an |advocate| (referrer) shares offer details with a |friend| (referee) via the corresponding form provided by campaign workflow. Which includes any time:
  - An advocate shares with a Friend via Email or any other channel from inside a referral campaign workflow
  - An Advocate copies a share link from a referral campaign workflow share screen

Note: the Post Share Webhook triggers every time a share occurs. For example,
if an Advocate shares with a Friend via email (or any channel), then shares with
a second Friend via email (or any channel), the Post Share Webhook will be
triggered twice.

.. raw:: html

  <h2>Payload parameters provided for Post Share Webhook</h2>

The sample payload with parameters for Post Share Webhook is available here: `Post Share Webhook Payload <https://www.talkable.com/api-docs/index.html?urls.primaryname=webhooks%20api&urls.primaryName=Webhooks#/Post%20Share/post_your_api_post_share_web_hook_path>`_.

.. note::

  ``origin.email`` contains the email saved at the moment when the campaign is
  first shown to the Advocate. It could be ``null``. For the most up-to-date
  information about the Advocate, use ``sharer_info`` property which is updated
  with the email address the Advocate has entered on the Advocate Signup/Share Page.
