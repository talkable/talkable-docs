.. _campaigns/site_placements/invite:
.. include:: /partials/common.rst

.. _invite_campaign:

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

First of all make sure you completed :ref:`Talkable JS integration initialization <ecommerce/custom>`.
Invite campaign integration does not require any data to be passed to Talkable since it only acts as the referral loop opener (referral is not created at this point).

The only requirement for it is a page on the site where it is going to placed. It is recommended that this page is always available to anyone on your site, even not logged in customers.

Once you have created the page below is an example of the basic Invite campaign integration:

.. include:: /samples/standalone/basic.rst

.. note::

  You can place <script> tag anywhere in the HEAD or BODY, however keep in mind that the DIV container tag should be placed into a proper place, this is where Talkable campaign iframe will live.

Overriding Customer Data
------------------------

In case you need to override customer data include `customer` object in addition to the rest of the data:

.. code-block:: html

  <!-- Place Talkable Container into appropriate place in the DOM -->
  <div id="talkable-invite"></div>

  <script>
    var _talkable_data = {
      // campaign_template: {
      // ...
      // },
      customer: {
        email: 'overridden@example.com',
        first_name: 'OverriddenName',
        last_name: 'OverriddenSurname'
      }
    };

    _talkableq.push(['register_affiliate', _talkable_data]);
  </script>

.. container:: hidden

  .. toctree::

