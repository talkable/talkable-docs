.. _integration/loyalty/auto_enrollment:
.. include:: /partials/common.rst

.. meta::
   :description: Find out how to auto-enroll loyalty members.

Auto-Enrollment
===============

Talkable allows to enroll users to loyalty without showing the loyalty dashboard page.

There are a couple of ways to do that:

* :ref:`Post-Purchase Enrollment`

* :ref:`Enrollment via JS Integration`

.. _Post-Purchase Enrollment:

Post-Purchase Enrollment
~~~~~~~~~~~~~~~~~~~~~~~~

Enroll users to loyalty after they make a purchase.
A setting to enable this behavior can be found under **Site settings** → **Loyalty settings** → **General** → **Auto-enrollment**.

.. _Enrollment via JS Integration:

Enrollment via JS Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enroll users to loyalty without showing the campaign using `join_loyalty`.

.. note::
   `join_loyalty` is available since integration version 4.5.9.

Code Example:
-------------

.. code-block:: js

   window._talkableq.push(["authenticate_customer", {email: "loyalty@talkable.com"}]);
   window._talkableq.push(["join_loyalty", {}]);
