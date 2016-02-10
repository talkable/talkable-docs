.. _saas:
.. include:: /partials/common.rst

SaaS Integrations
#################

.. include:: /partials/note_enterprise_integration.rst

SaaS integration is abstracted from :ref:`E-Commerce <ecommerce>` since you need to create referrals based on your specific business logics while E-Commerce can work only with store purchases. With such abstraction you can register Talkable Event with just a few parameters:

* **Event Category** to describe what type of action was made. For example: "User Registered". All Events appear inside Events Report where you can sort/filter/segment them based on the Event Category or based on any other data you pass along.
* **Event Number**. This is a unique action ID that will be stored in Talkable.

1. Add Talkable to Your Site
----------------------------

.. include:: /partials/initialization.rst

2. Add Talkable Campaigns
-------------------------

Below is an example of registering an Event and showing :ref:`post_purchase_campaign` campaign as a result:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <div id="talkable-post-purchase"></div>

  <script>
    var _talkable_data = {
      event: {
        event_number: '100011', // Required - unique Event id
        event_category: 'Signups' // Required - Event category
      },
      campaign_template: 'post-purchase' // Loads Post Purchase campaign with tag "post-purchase"
    };

    // Passing Event to Talkable
    _talkableq.push(['register_event', _talkable_data]);
  </script>

The code above registers an Event and shows :ref:`advocate_signup_page_view` as a result. |br|
When the Event is registered successfully it appears inside Events Report. |br|

|hr|

Showing Different Campaign
~~~~~~~~~~~~~~~~~~~~~~~~~~

In the example above we show :ref:`post_purchase_campaign` Campaign as a result of Event registration.
However you can show any other Talkable Campaign instead since there are 8 of them.
Here is an example how to show :ref:`invite_campaign`:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <div id="talkable-invite"></div>

  <script>
    var _talkable_data = {
      event: {
        event_number: '100011', // Required - unique Event id
        event_category: 'Signups' // Required - Event category
      },
      campaign_template: 'invite' // Loads Invite campaign with tag "invite"
    };

    // Passing Event to Talkable
    _talkableq.push(['register_event', _talkable_data]);
  </script>

.. note::

  Make sure that the Container (the DIV tag where Talkable iframe inserts to) ID corresponds to `campaign_template` value.
  Otherwise Talkable Campaign will be shown below your page content at the very bottom.

Correspondence between Container ID and `campaign_template`:

+----------------------------------+---------------------------------+-----------------------------------+
| Talkable Campaign                | Container ID                    | campaign_template                 |
+==================================+=================================+===================================+
| :ref:`post_purchase_campaign`    | `talkable-post-purchase`        | `post-purchase`                   |
+----------------------------------+---------------------------------+-----------------------------------+
| Post Purchase Full Screen Image  | `talkable-post-purchase`        | `post-purchase-full-bleed`        |
+----------------------------------+---------------------------------+-----------------------------------+
| :ref:`invite_campaign`           | `talkable-invite`               | `invite`                          |
+----------------------------------+---------------------------------+-----------------------------------+
| Invite Full Screen Image         | `talkable-invite`               | `invite-full-bleed`               |
+----------------------------------+---------------------------------+-----------------------------------+
| Advocate Dashboard               | `talkable-dashboard`            | `dashboard`                       |
+----------------------------------+---------------------------------+-----------------------------------+
| Every Visitor Popup              | `talkable-popup`                | `popup`                           |
+----------------------------------+---------------------------------+-----------------------------------+
| Floating Widget Popup            | `talkable-popup`                | `popup-trigger`                   |
+----------------------------------+---------------------------------+-----------------------------------+
| New Visitor Popup                | `talkable-popup`                | `new-visitor-popup`               |
+----------------------------------+---------------------------------+-----------------------------------+

Advanced Features
-----------------

Here is a full list of things you can do with Talkable:

.. toctree::
  :maxdepth: 1
  :glob:

  /optional/*
