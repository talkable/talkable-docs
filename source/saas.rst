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
    // Talkable Event Data object where you set the data you are going to pass
    var _talkable_data = {
      event: {
        event_number: '100011', // Required - unique Event id
        event_category: 'Signups' // Required - Event category
      },
      campaign_template: {
        name: 'post-purchase' // Loads Post Purchase campaign with tag "post-purchase"
      }
    };

    // Passing Event to Talkable
    _talkableq.push(['register_event', _talkable_data]);
  </script>

The code above registers an Event and shows :ref:`advocate_signup_page_view` as a result. |br|
When the Event is registered successfully it appears inside Events Report. |br|

|hr|

Advanced Integration
--------------------

In addition to our basic required dataset we allow you to pass us a lot more data and parameters you might need. Learn what each parameters does from the comment lines bellow:

.. code-block:: html

  <!-- Talkable iframe container, you are free to control its place in the DOM -->
  <div id="talkable-post-purchase"></div>

  <!-- Begin Talkable integration code -->
  <script>
    // Talkable Event Data object where you set the data you are going to pass
    var _talkable_data = {
      event: {
        event_number: '100011', // REQUIRED - a unique ID of the Event
        event_category: 'Signups', // REQUIRED - Event Category that the Event will belong to
        subtotal: '23.97', // OPTIONAL - if the Event has a value (paid subscription for example) always pass it along, you can then analyze your total sales numbers inside Talkable Reports
        coupon_code: 'SAVE20', // OPTIONAL - provide a coupon code if the customer applied it
        traffic_source: 'Signup page' // OPTIONAL - indicate person traffic source. Can be used as segmentation parameter in reports.
      },
      customer: {
        email: 'customer@gmail.com', // OPTIONAL, RECOMMENDED - customer email the Event is associated with. If you pass an email the customer will be logged in with it immediately and as a result they will see Advocate Share Page instead of a Signup. It is a good practice to always pass an email not to ask customers to login themselves.
        customer_id: '1234567890', // OPTIONAL - internal customer ID, for tracking
        first_name: 'Name',  // OPTIONAL - Customer First Name
        last_name: 'Surname', // OPTIONAL - Customer Last Name
        // OPTIONAL - additional customer properties, in case you want to use some additional data inside Campaign Views
        person_custom_properties: {
          key1: 'value1', // String value
          key2: '123.2' // Numeric value
        }
      },
      campaign_template: { name: 'post-purchase' },
      // campaign_tags: ['custom'], // OPTIONAL - Campaign tags used to target specific campaign for the offer, use it instead of campaign_template
      // iframe: { // OPTIONAL - any valid HTML attributes can go in here
      //   container: 'talkable-post-purchase', // Tell Talkable where to insert the iframe (this is HTML id attribute value)
      //   width: '100%' // These are standard HTML attributes, feel free to add as many you need
      // }
    };

    // Pass Event to Talkable
    _talkableq.push(['register_event', _talkable_data]);
  </script>
  <!-- End Talkable integration code -->

|hr|

Advanced Features
-----------------

Here is a full list of things you can do with Talkable:

.. toctree::
  :maxdepth: 1
  :glob:

  /optional/*

