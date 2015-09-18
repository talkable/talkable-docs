.. _ios_sdk/integration/standalone:
.. include:: /partials/common.rst

Standalone Campaign
===================

Let’s take a look at how the Standalone campaign integration looks. The main purpose of this type of campaign is to drive your users to invite their friends (to become Advocates) without being gated by a purchase beforehand.

Usually Standalone campaign look like a separate widget that people can access by clicking on the “Invite friends” button inside app navigation.

Once you’ve got a Standalone campaign set up inside Talkable you can integrate the campaign with the following line of code:

.. code-block:: objc

  #import <TalkableSDK/Talkable.h>
  ...
  [[Talkable manager] registerOrigin:TKBLAffiliateMember params:nil];
  ...
  
.. note::
  
  Make sure you have at least one live “SA” campaign with a default tag inside Talkable Site
  
Note that `params` are empty, in this case user will see the :ref:`Advocate Signup Page <campaigns/views/affiliate_members_new>`, which is used to collect the user’s email address. Your application may already know/have access to the user’s email, if so, you should pass this parameter which will automatically skip the SignUp Page in the flow and show the :ref:`Advocate Share Page <campaigns/views/offers_show>`. You have the ability to pass any custom data you think might be useful by using “person custom properties” to define any number of custom key/value pairs. For example, below we are creating and passing a custom key value pair of *eye color* = *green*. Any data passed through here will be accessible on a campaign level for segmentation or other logic.

.. code-block:: objc
  
  #import <TalkableSDK/Talkable.h>
  ...
  NSDictionary* params = @{
    TKBLAffiliateMemberKey: @{
      TKBLAffiliateMemberEmailKey: @”advocate@example.com”,
      TKBLAffiliateMemberFirstNameKey: @"John",
      TKBLAffiliateMemberLastNameKey: @"Smith",
      TKBLAffiliateMemberPersonCustomPropertiesKey: @{
        @"eye_color": @"brown"
      }
    }
  };
  ...
  [[Talkable manager] registerOrigin:TKBLAffiliateMember params:params];
  ...

.. container:: hidden

   .. toctree::
