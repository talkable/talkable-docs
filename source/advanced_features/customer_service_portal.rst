.. _advanced_features/customer_service_portal:
.. include:: /partials/common.rst

.. meta::
   :description: Customer Service Portal

Customer Service Portal
=======================

Explore full  details for each individual customer and their referral journey, manage their rewards and deliver
excellent customer service.

Overview
--------

**Logging In**

Once you are logged into your Talkable account, navigate to the Customer Service Portal in the top navigation.

.. image:: /_static/img/advanced_features/customer_service_portal/logging.png

**Logging In**

Navigating to the Customer Service Portal

The Customer Service Portal provides a simple search box that will allow you to search by 4 criteria:

- **Advocate email**: the email of the user who shared with their Friend.
- **Friend email**: the email of the user who received a share email.<br>
- **Friend order number**: the order number of Friend purchase.<br>
- **Data Capture The Initialization ScCoupon code**: the single-use coupon code that the Friend applied during
  checkout.<br>

Example Customer Service Portal post login:

.. image:: /_static/img/advanced_features/customer_service_portal/login.png



Terminology
-----------

**Referral**

This is a connection between an Advocate (who invites) and a Friend who completed a referral purchase from the
Advocate’s invite (a share). A referral will not be created unless the following 3 pieces are known: Advocate Email,
Friend Email, and a Purchase made by a Referred Friend. Each referral is passed through several fraud checks
(configured inside Fraud Settings). As a result of the fraud checks each referral status can be:

 1. **In progress**: Talkable referral engine is processing the referral. Such action usually takes less than a second
    so it is highly unlikely that you will see this status. No rewards are issued at this point.

 2. **Pending**: a referral is pending approval. Talkable referral engine can either approve referrals automatically
    with some delay (optionally) or leave this decision to the user (manual, not recommended as it leads to
    backlogged referrals). Thus, if the referral fraud checks were passed successfully each referral stays in Pending
    status until they are approved automatically based on the auto-approval delay configuration (configured inside Fraud
    Settings). No rewards are issued at this point.

 3. **Flagged**: due to having many different options to configure referral fraud checks, it is not always possible to
    set up automatic resolution for each referral. For such cases, you may want to Flag referrals that are in a so
    called grey area, where the chance of fraud is around 50% and it is impossible to make the decision automatically.
    All flagged referrals are added to a queue for manual resolution and can be accessed inside CSP → Referrals.
    No rewards are issued at this point.

 4. **Approved**: this is a valid referral status which either gets set by the Talkable referral engine with automatic
    approval or by a user in case of manual resolution. Flagged referrals can also turn to approved since they are
    resolved manually. All rewards associated with the referral are then passed to the next stage to verify if they
    can be issued.

 5. **Voided**: this status is set by a user manually if they decide a referral is invalid and there should be no
    rewards issued as a result. Only pending and flagged referrals can be voided. Talkable referral engine cannot set
    this status automatically. All rewards associated with the referral are getting blocked as a result.

 6. **Blocked**: when some fraud checks are failed Talkable referral engine blocks the referral immediately. All rewards
    associated with the referral are getting blocked as a result.

 7. **Unblocked**: this status gets set manually by a user if they decide to approve the referral in case it was blocked
    automatically (due to some fraud checks failed) but the user thinks it is a valid referral after checking it
    manually. All rewards associated with the referral are then passed to the next stage to verify if they can be issued.

**Reward**

This is what the person gets as a result of some action (incentive). Available reward statuses:

- **Pending**: the reward is awaiting referral approval. The referral can either be approved manually or automatically,
  depending on your configuration.

- **Waiting for coupon**: there are not enough coupons left to pay the reward. The reward will remain in a 'waiting'
  status until more coupons will be uploaded into the associated coupon list.

- **Given**: the reward was paid to the person but Talkable does not have information as to whether it was used or not.
  Most likely it was not yet used.

- **Blocked/No reward**: there was no reward created either because the associated referral was blocked according to
  Fraud Settings or because of other reasons: incentive criteria has blocked it, or the person was blacklisted.


Use case #1: Where do I find referrals?
---------------------------------------

1.1 **Person Lookup**

When a customer calls in, often their first question is: “I’ve referred my Friend but haven’t received my reward.”

The first step is to check to see if the referral exists in our system, which can be done simply by entering Advocate
or Friend’s email inside Person Lookup.

In this example Stephanie (Advocate), ``stephanie***@ganleywestside.com``, has called in to check on the status of her
reward for referring her Friend Levi ``*****levi@yahoo.com``.

Here are the steps we’re going to take:

1. Enter in Stephanie’s email address and press ‘Search’.
2. Scroll down and see if we see a referral for her Friend Levi.
3. See if the reward has qualified, when it qualified, and if she should have received an
   email.

.. image:: /_static/img/advanced_features/customer_service_portal/lookup.png
(After entering in Stephanie’s email the screen populates with information associated with her email address.)


1.2 **Referral details**

.. image:: /_static/img/advanced_features/customer_service_portal/click_to_referral_details.png
(Notice that the screen is divided into 2 main sections. The bottom section has 7 tabs referencing additional sections.
We’ll get to those later. For now, we’re interested in “Referrals” and want to scroll down to find Levi, and see
what’s happening with that referral. Click on “Details”.)


Here’s a closeup on Levi’s record:

.. image:: /_static/img/advanced_features/customer_service_portal/referral_details.png

What we discovered: the referral is valid because there was no fraud detected, meaning  that Stephanie and Levi are
different people. We can also see that Levi used the coupon code at checkout.

Let’s also expand fraud filters section to check the details:

.. image:: /_static/img/advanced_features/customer_service_portal/fraud_filters.png

This looks like a valid referral. Let’s move on to Use case #2.


Use case #2: Where is Advocate reward?
--------------------------------------

Advocates will receive an email with their reward for each qualified Friend they refer. In most cases this email will
contain a coupon or gift card code that the Advocate can redeem. In order to check on the status of a particular
reward, all we have to do is see if the email has been sent to the Advocate.

Here are the steps we will take:

1. Enter in Stephanie’s email (if not entered already).
2. Navigate to “Emails” tab.
3. Look for “Advocate Reward Paid Email”.
4. Click on Details.
5. Provide information to the customer from the details page.

.. image:: /_static/img/advanced_features/customer_service_portal/email_details.png

2.1 **Email delivery**

Navigate to ‘Emails’ tab after entering in Stephanie’s email. The “Emails” tab shows all emails sent to the Advocate
about the referral program. Look for the “Advocate Reward Paid Email”. There may be multiple emails like this.

.. image:: /_static/img/advanced_features/customer_service_portal/email_delivery.png

To ensure we find the desired email we need to go back to the referral details and see a referral approval date:

.. image:: /_static/img/advanced_features/customer_service_portal/approve_date.png