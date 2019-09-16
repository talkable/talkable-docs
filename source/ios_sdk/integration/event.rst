.. _ios_sdk/integration/event:
.. include:: /partials/common.rst

Custom Events
=============

In addition to Signup and Purchase incentives, Talkable campaigns can utilize :ref:`custom events <advanced_features/events>` to issue rewards based on other actions performed by Advocates and Friends, such as purchasing a subscription, completing a game level, or simply visiting a certain place in your app. Register an event every time the user performs the desired action in your app.

An Event has two required properties: event category and event number. Please refer to :ref:`available properties <advanced_features/events/available_properties>` for a complete list of optional properties.

.. code-block:: objc

  NSDictionary* params = @{
    TKBLCampaignTags: @"your-campaign-tag",
    TKBLEventKey: @{
      TKBLEventCategoryKey: @"subscription_purchased",
      TKBLEventNumberKey: [[NSUUID UUID] UUIDString] //must be unique for given category
    }
  };
  [[Talkable manager] registerOrigin:TKBLEvent params:params];

If you have a Talkable offer configured for this event, the Talkable campaign screen will be displayed as a result of calling the ``registerOrigin`` method.

.. warning::

  Unlike the default :ref:`Standalone <ios_sdk/integration/standalone>` and :ref:`Post Purchase <ios_sdk/integration/post_purchase>` integrations, the event-based integration will not automatically use the default campaign tag (``ios-invite`` or ``ios-post-purchase`` respectively). To match your events to the desired Talkable campaign, you **must** specify the correct campaign tag when creating an event.

Customer data can be added to the registered event. Custom properties passed with the event will be added to the customer profile.

.. code-block:: objc

  NSDictionary* params = @{
    TKBLCampaignTags: @"your-campaign-tag",
    TKBLEventKey: @{
      TKBLEventEmailKey: @"customer@example.com",
      TKBLEventCategoryKey: @"subscription_purchased",
      TKBLEventNumberKey: self.orderNumberField.text,
      TKBLEventPersonCustomPropertiesKey: @{
          @"property_key": @"property_value"
        }
      }
    }
  };
  [[Talkable manager] registerOrigin:TKBLEvent params:params];

Please refer to the :ref:`Integrating Events <advanced_features/events>` page to learn more about event-based campaigns.
