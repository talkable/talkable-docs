.. _android_sdk/integration/event:
.. include:: /partials/common.rst

Custom Events
=============

In addition to Signup and Purchase incentives, Talkable campaigns can utilize :ref:`custom events <advanced_features/events>` to issue rewards based on other actions performed by Advocates and Friends, such as purchasing a subscription, completing a game level, or simply visiting a certain place in your app. Register an event every time the user performs the desired action in your app.

An Event has two required properties: event category and event number. Please refer to :ref:`available properties <advanced_features/events/available_properties>` for a complete list of optional properties.

.. code-block:: java

     String eventNumber = "ev123789"; //must be unique for given category
     String eventCategory = "subscription_purchased";

     Event event = new Event(eventNumber, eventCategory);

     TalkableApi.createOrigin(event, new Callback2<Origin, Offer>() {...});

If you have a Talkable offer configured for this event, the Talkable campaign screen will be displayed as a result of calling the ``createOrigin`` method.

.. warning::

  Unlike the default :ref:`Standalone <android_sdk/integration/standalone>` and :ref:`Post Purchase <android_sdk/integration/post_purchase>` integrations, the event-based integration will not automatically use the default campaign tag (``android-invite`` or ``android-post-purchase`` respectively). To match your events to the desired Talkable campaign, you **must** specify the correct campaign tag when creating an event.

Customer data can be added to the registered event. Custom properties passed with the event will be added to the customer profile.

.. code-block:: java

     String email = "advocate@example.com";
     String firstName = "John";
     String lastName = "Smith";
     HashMap<String, String> customProperties = new HashMap<String, String>();
     customProperties.put("property_key", "property_value");
     Customer customer = new Customer(null, firstName, lastName, email, customProperties);

     String eventNumber = "ev123789";
     String eventCategory = "subscription_purchased";

     Event event = new Event(eventNumber, eventCategory);
     event.setCustomer(customer);

     TalkableApi.createOrigin(event, new Callback2<Origin, Offer>() {...});

Please refer to the :ref:`Integrating Events <advanced_features/events>` page to learn more about event-based campaigns.
