.. _saas:
.. include:: /partials/common.rst

SaaS Integrations
#################

.. include:: /partials/note_enterprise_integration.rst

SaaS integration is abstracted from E-Commerce since you need to create referrals based on your specific business logics while E-Commerce can work only with store purchases. With such abstraction you can register Talkable Event with just a few parameters:

* **Event Category** to describe what type of action was made. For example: "User Registered". All Events appear inside Events Report where you can sort/filter/segment them based on the Event Category or based on any other data you pass along.
* **Event Number**. This is a unique action ID that will be stored in Talkable.

Basic Integration
-----------------

Below is the basic sample code for registering an Event with only required fields:

.. code-block:: html

  <script>
    // Globally available Talkable queue array that you populate all data to
    var _talkableq = _talkableq || [];

    // Talkable Event Data object where you set the data you are going to pass
    var talkableEventData = {
      event_number: '100011',
      event_category: 'Signups'
    };

    // Registering an Event at Talkable
    _talkableq.push(
      ['init', { site_id: 'YOUR_TALKABLE_SITE_ID' }],
      ['register_event', talkableEventData]
    );
  </script>
  <script src="|integration_url|" type="text/javascript"></script>

Keep in mind to set your Talkable site ID/slug and simply place the script into your page between opening and closing ``BODY`` tag. |br|
You can find a site slug right in the URL, it usually looks like talkable.com/sites/``your-site-slug``. |br|
The code above registers an Event and shows :ref:`advocate_signup_page_view` as a result. |br|
When the Event is registered successfully it appears inside Events Report. |br|

.. include:: /partials/integration_head.rst

|hr|

Advanced Integration
--------------------

In addition to our basic required dataset we allow you to pass us a lot more data and parameters you might need. Learn what each parameters does from the comment lines bellow:

.. code-block:: html

  <!-- Begin Talkable integration code -->
  <script>
    // Globally available Talkable queue array that you populate all data to
    var _talkableq = _talkableq || [];

    // Talkable Event Data object where you set the data you are going to pass
    var talkableEventData = {
      event_number: '100011', // REQUIRED - a unique ID of the Event
      event_category: 'Signups', // REQUIRED - Event Category that the Event will belong to
      email: 'customer@gmail.com', // OPTIONAL, RECOMMENDED - customer email the Event is associated with. If you pass an email the customer will be logged in with it immediately and as a result they will see Advocate Share Page instead of a Signup. It is a good practice to always pass an email not to ask customers to login themselves.
      campaign_tags: ['default'], // OPTIONAL - Campaign tags used to target specific campaign for the offer
      subtotal: '23.97', // OPTIONAL - if the Event has a value (paid subscription for example) always pass it along, you can then analyze your total sales numbers inside Talkable Reports
      coupon_code: 'SAVE20', // OPTIONAL - provide a coupon code if the customer applied it
      customer_id: '1234567890', // OPTIONAL - internal customer ID, for tracking
      first_name: 'Name',  // OPTIONAL - Customer First Name
      last_name: 'Surname',  // OPTIONAL - Customer Last Name
      // OPTIONAL - show an offer inline instead of a popup
      // iframe: {
      //   // container: "id-example", // Tell Talkable where to insert the iframe (ID attribute)
      //   width: '100%', // These are standard HTML attributes, feel free to add as many you need
      //   height: '400'
      // },
      // loader: 'display: none;', // OPTIONAL - change a popup preloader style with CSS, or hide it completely
      // OPTIONAL - additional customer properties, in case you want to use some additional data inside Campaign Views
      // person_custom_properties: {
      //     key1: 'value1', // String value
      //     key2: '123.2' // Numeric value
      // },
      // traffic_source: 'Signup page' // OPTIONAL - indicate person traffic source. Can be used as segmentation parameter in reports.
    };

    // Registering an Event at Talkable
    _talkableq.push(
      [
        'init',
        {
          site_id: 'YOUR_TALKABLE_SITE_ID' // REQUIRED - Talkable Site ID/slug.
          // If you are using live ENV and test ENV you might need to switch between two sites based on a current location host:
          // site_id: window.location.host == 'www.site.com' ? 'site' : 'site-testing'
          // ,server: 'https://www.talkable.com' // OPTIONAL - your custom domain, needs to be setup as an alias to talkable.com (Enterprise clients only)
        }
      ],
      ['register_event', talkableEventData] // Pass Event to Talkable
    );
  </script>
  <script src="|integration_url|" type="text/javascript"></script>
  <!-- End Talkable integration code -->

.. include:: /partials/integration_head.rst

