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
For example, this could be used for enrolling users during registration or login.

Don't forget to include a consent checkbox that would inform your user that they are about to join the loyalty program.

.. note::
  `join_loyalty` is available since integration version 4.5.9.

Code Example #1:
----------------

Use `authenticate_customer` to store current user data.

When you call `join_loyalty`, you can pass empty object since Talkable will have access to the data from `authenticate_customer`.

.. tip::
  `authenticate_customer` data can also be reused by other integration functions.

.. code-block:: js

  window._talkableq.push(["authenticate_customer", {
    email: "loyalty@talkable.com", // required for `join_loyalty`
    phone_number: '+12025551111',
    first_name: "John",
    last_name: "Smith",
    custom_properties: {},
    customer_id: "11111"
  }]);
  window._talkableq.push("join_loyalty", {})

Code Example #2:
----------------

Pass loyalty member data directly to `join_loyalty`.

.. note::
  Arguments passed with `join_loyalty` override respective arguments from `authenticate_customer`.

.. code-block:: js

  window._talkableq.push(["join_loyalty", {
    email: "loyalty@talkable.com", // required
    phone_number: '+12025551111',
    first_name: "John",
    last_name: "Smith",
    custom_properties: {},
    customer_id: "11111"
  }]);
