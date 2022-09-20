.. _android_sdk/integration/standalone:
.. include:: /partials/common.rst

Standalone Campaign
===================

Let’s take a look at how the Standalone campaign integration looks. The main purpose
of this type of campaign is to drive your users to invite their friends (to become Advocates)
without being gated by a purchase beforehand.

Usually Standalone campaign look like a separate widget that people can access by clicking on
the “Invite friends” button inside app navigation.

Once you’ve got a Standalone campaign set up inside Talkable you can integrate the campaign
with the following line of code:

.. code-block:: java

  import com.talkable.sdk.Talkable;
  ...

  Activity activity = this;
  AffiliateMember affiliateMember = new AffiliateMember();
  Talkable.showOffer(activity, affiliateMember, new TalkableErrorCallback<TalkableOfferLoadException>() {
      @Override
      public void onError(TalkableOfferLoadException error) {
          // Error handling. Note that it runs on non UI thread
      }
  });

  ...

.. note::

  Make sure you have at least one Live “SA” campaign inside Talkable Site with `android-invite` tag or the tag you specified

Note that `customer` is empty, in this case user will see the
:ref:`Advocate Signup Form <campaigns/views/offers_show>`, which is used to collect
the user’s email address. Your application may already know/have access to the user’s email,
if so, you should pass this parameter which will automatically skip the Signup Form in the
flow and show the :ref:`Advocate Share Form <campaigns/views/offers_show>`.

.. code-block:: java

  import com.talkable.sdk.Talkable;
  ...

  String email = "advocate@example.com"; // Required
  String idInYourApp = "a8db7683-0f7f-407e-8d12-af2d501035c8"; // Use unique identifier from your system, optional
  String firstName = "John"; // Optional
  String lastName = "Smith"; // Optional
  HashMap<String, String> customProperties = new HashMap<String, String>();
  customProperties.put("property_key", "property_value");
  Customer customer = new Customer(idInYourApp, firstName, lastName, email, customProperties);

  AffiliateMember affiliateMember = new AffiliateMember(customer);
  String campaignTag = "android-invite";
  affiliateMember.setCampaignTag(campaignTag);

  Activity activity = this;
  Talkable.showOffer(activity, affiliateMember, new TalkableErrorCallback<TalkableOfferLoadException>() {
      @Override
      public void onError(TalkableOfferLoadException error) {
          // Error handling. Note that it runs on non UI thread
      }
  });
  ...

.. container:: hidden

   .. toctree::
