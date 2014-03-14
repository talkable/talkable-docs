.. _api/purchase:
.. include:: /partials/common.rst

Purchase API
============

.. include:: /partials/note_preliminary_api.rst

Approve/Void Rewards for Purchases
----------------------------------

.. code-block:: url

   PUT https://curebit.com/api/v1/sites/<site_slug>/purchases/<order_number>/set_rewards_status?api_key=<api_key>&status=<status>

You can approve or void rewards for purchases that are waiting approval.

.. note::

   Approved or voided purchases can not be changed to the opposite state.

.. raw:: html

   <h3>Parameters</h3>

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Curebit Site ID. You can get this from your Curebit
                     dashboard after you log in and create a site.
   api_key           Your API key. You can manage your API key in the Account
                     Settings.
   order_number      Purchase Order number for the reward that needs to be
                     approved/voided.
   status            Reward status. (see possible statuses below)
   ================= ========================================================

.. raw:: html

   <h3>Statuses</h3>

.. container:: ptable

   ================= ========================================================
   Status            Description
   ================= ========================================================
   approved          Approve rewards and start payment procedure.
                     Referral is approved.
   voided            Voids any rewards that have not yet been paid.
                     Referral is voided. |br|
                     *It's impossible to void rewards that have already been
                     paid (e.g. Coupon on Landing Page for referred)*
   unrewarded        Voids any rewards that have not yet been paid.
                     Referral is not actually voided itself, but no reward
                     will be paid. |br|
                     *It's impossible to void rewards that have already been
                     paid (e.g. Coupon on Landing Page for referred)*
   ================= ========================================================

.. raw:: html

   <h3>Responses</h3>

.. container:: ptable

   ================= =============================== ========================================================
   HTTP Code         HTTP Body                       Description
   ================= =============================== ========================================================
   200 OK            ``{"success": true}``           Order found / status changed.
   200 OK            ``{"success": true,             Order does not have rewards.
                     "notice": "no rewards"}``
   400 Bad Request   ``{"success": false,            The "status" is wrong.
                     "error_messages": message}``
   403 Forbidden     ``{"success": false,            The request failed and no purchase's rewards were changed.
                     "error_messages": message}``
   404 Not Found     ``{"success": false,            The site could not be found by "site_slug".
                     "error_messages": "An exception
                     occurred. No site found by
                     site_slug: #{site_slug}"}``
   400 Bad Request   ``{"success": false,            The order could not be found by "order_number".
                     "error_messages": "Couldn't
                     find Purchase with order_number
                     = #{order_number}"}``
   ================= =============================== ========================================================

.. note::

   If purchase was not redeemed and does not have rewards it will return success as well.

Create Purchases
----------------

.. code-block:: url

   POST https://curebit.com/api/v1/sites/<site_slug>/purchases/create?api_key=<api_key>

.. raw:: html

   <h3>Parameters</h3>

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Curebit Site ID. You can get this from your Curebit
                     dashboard after you log in and create a site.
   api_key           Your API key. You can manage your API key in the Account
                     Settings.
   purchases         Array of JSON objects with following properties:

                     * email
                     * subtotal
                     * order_number
                     * order_date (in UTC time zone, or as a timestamp with timezone information)
                     * items (optional)

                     For example,

                     .. code-block:: javascript

                        [
                          {
                            "email": "1st_customer@mail.com",
                            "order_number": 1,
                            "order_date": "2014-03-13 12:49:54",
                            "subtotal": 500
                          },
                          {
                            "email": "2nd_customer@mail.com",
                            "order_number": 2,
                            "order_date": "2014-03-14 05:49:54",
                            "subtotal": 100,
                            "items": [
                              {
                                "price": 25,
                                "quantity": 4,
                                "product_id": "TSHIRT"
                              }
                            ]
                          }
                        ]
   ================= ========================================================

.. raw:: html

   <h3>Responses</h3>

.. container:: ptable

   ================= =============================== ========================================================
   HTTP Code         HTTP Body                       Description
   ================= =============================== ========================================================
   201 Created       ``{"success": true}``           Purchase created.
   400 Bad Request   ``{"success": false,            The "purchases" parameter is invalid.
                     "error_messages": message}``
   403 Forbidden     ``{"success": false,            The request failed and purchase wasn't created.
                     "error_messages": message}``
   404 Not Found     ``{"success": false,            The site could not be found by "site_slug".
                     "error_messages": "An exception
                     occurred. No site found by
                     site_slug: #{site_slug}"}``
   ================= =============================== ========================================================

.. toctree::
