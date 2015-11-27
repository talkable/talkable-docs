.. _optional/site_placements/invite:
.. include:: /partials/common.rst

Invite
======

Increase the number of new customers by giving anyone an opportunity to invite friends from a publicly available page on your site. This site placement only acts as the referral loop opener. From here all your customers can invite their friends to participate in the referral program.

Usually this page has www.site.com/**invite** URL and is linked from the main site navigation at the top.

Flow
----

.. image:: /_static/img/site_placements/invite.png
   :alt: Talkable campaign flow — Invite template,
   :class: is-minimal

Basic Integration
-----------------

Invite campaign integration does not require any data to be passed to Talkable since it only acts as the referral loop opener (referral is not created at this point).

The only requirement for it is a page on the site where it is going to placed. It is recommended that this page is always available to anyone on your site, even not logged in customers.

Once you have created the page below is an example of the basic Invite campaign integration:

.. include:: /samples/standalone/basic.rst

.. note::

  You can place <script> tag anywhere in the HEAD or BODY, however keep in mind that the DIV container tag should be placed into a proper place, this is where Talkable campaign iframe will live.

Authorizing Advocate
~~~~~~~~~~~~~~~~~~~~

If the customer email address is available always pass it in order to create smooth user experience and show :ref:`Advocate Share Page <campaigns/views/offers_show>` instead of :ref:`Advocate Signup Page <campaigns/views/affiliate_members_new>`. It is recommended to include first name and last name as well, this information can then be used to make campaign more personal to |Advocate| friends.

.. include:: /samples/standalone/basic-authorized.rst

.. note::

  Passing email address is a great way to ensure Advocate will always see their previos offer. Otherwise for each new signup with exact same email address Talkable creates new affiliate member without any sharing history.

.. container:: hidden

  .. toctree::

