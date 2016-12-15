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

Below is an example of registering an Event and showing Campaign for :ref:`Post Purchase <campaigns/campaign_placements/post_purchase>` Placement as a result:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <div id="talkable-offer"></div>

  <script>
    var _talkable_data = {
      event: {
        event_number: '100011', // Required - unique Event id
        event_category: 'signups' // Required - Event category
      },
      campaign_tags: ['post-purchase'] // Loads Post Purchase campaign with tag "post-purchase"
    };

    // Passing Event to Talkable
    _talkableq.push(['register_event', _talkable_data]);
  </script>

The code above registers an Event and shows :ref:`advocate_signup_page_view` as a result. |br|
When the Event is registered successfully it appears inside Events Report. |br|

|hr|

.. raw:: html

  <h2>Showing Different Campaign</h2>

In the example above we show Campaign for :ref:`Post Purchase <campaigns/campaign_placements/post_purchase>` Placement as a result of Event registration.
However you can show any other Talkable Campaign instead since there are many of them.
Here is an example how to show Campaign for :ref:`Standalone <campaigns/campaign_placements/standalone>` Placement

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <div id="talkable-offer"></div>

  <script>
    var _talkable_data = {
      event: {
        event_number: '100011', // Required - unique Event id
        event_category: 'signups' // Required - Event category
      },
      campaign_tags: ['invite'] // Loads Invite campaign with tag "invite"
    };

    // Passing Event to Talkable
    _talkableq.push(['register_event', _talkable_data]);
  </script>

.. note::

  Talkable JS integration library inserts the iframe into a container DIV with id="talkable-offer".
  Campaign Tags are show either on Campaigns listing page below each campaign's name or right on Details page
  of any campaign, inside "Integration" area.

.. raw:: html

  <h2>Advanced Features</h2>

Here is a full list of :ref:`Advanced Talkable features <optional>`.
