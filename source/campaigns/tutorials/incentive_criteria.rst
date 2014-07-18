.. _campaigns/tutorials/incentive_criteria:
.. include:: /partials/common.rst

Incentive Criteria
------------------

When you create an incentive for Advocate or Friend, you can set its trigger condition.

Condition is processed by |liquid| and the result should evaluate to ``true``
for incentive to be triggered.

If condition is left blank, it is assumed to be ``true``.

.. raw:: html

   <h4>Example</h4>

If you want to reward Advocate only if Friend is a new customer and used |br|
Curebit single-use coupon at checkout, the right trigger condition would be:

.. image:: /_static/img/incentive-criteria-1.png
   :alt: Incentive Trigger Criteria

If condition evaluates to anything else than ``true`` or ``false``, the value
it returns will be visible in Referrals Report.

This way, you can know which part of a condition was the reason Advocate didn't
get a reward:

.. image:: /_static/img/incentive-criteria-2.png
   :alt: Incentive Trigger Criteria

.. image:: /_static/img/incentive-criteria-3.png
   :alt: Referrals Report
