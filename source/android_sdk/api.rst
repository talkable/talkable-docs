.. _android_sdk/api:
.. include:: /partials/common.rst

API
===

Talkable features are also available via API. So there are helper methods in Talkable SDK.
All methods are available in any place of your app (after :ref:`initialization <main_activity_setup>`).

Create visitor
--------------

It’s the simplest method. You don’t need anything to create `Visitor`.
But you can do anything you need with just create one.

  .. code-block:: java

    import com.talkable.sdk.TalkableApi;

    TalkableApi.createVisitor(new Callback1<Visitor>() {
        @Override
        public void onSuccess(Visitor apiVisitor) {
            // Process success
        }

        @Override
        public void onError(ApiError error) {
            // Process error
        }
    });

Create origin
-------------

You need to build `Origin` to create. There are three subclasses of this class. You need to build one of them.

Hierarchy
.........

    * `Origin` (Abstract)
        * `AffiliateMember`
        * `Event`
            * `Purchase`

Building Origin
...............

You need to build `Origin` using one of examples below:

.. code-block:: java

    // Building customer, required for all types
    String email = "advocate@example.com"; // Required
    String idInYourApp = "a8db7683-0f7f-407e-8d12-af2d501035c8"; // Use unique identifier from your system, optional
    String firstName = "John"; // Optional
    String lastName = "Smith"; // Optional
    Customer customer = new Customer(idInYourApp, firstName, lastName, email);

    // Building AffiliateMember
    AffiliateMember origin = new AffiliateMember();
    origin.setCustomer(customer); // Required

    // Building Event
    String eventNumber = "1"; // Required
    String eventCategory = "event-category"; // Required
    Double subtotal = 10.99; // Optional
    String[] coupons = {"EXAMPLE-CODE"}; // Optional

    Event origin = new Event(eventNumber, eventCategory, subtotal, coupons);
    origin.setCustomer(customer); // Required

    // Build purchase
    Double price = 10.99;
    Integer quantity = 1;
    String productId = "1";
    Item item = new Item(subtotal, quantity, productId);

    Double subtotal = price * quantity; // Required
    Integer orderNumber = 1; // Required
    Date orderDate = Calendar.getInstance().getTime(); // Required
    String[] coupons = {"EXAMPLE-CODE"}; // Optional

    Purchase origin = new Purchase(subtotal, orderNumber, orderDate, coupons);
    origin.setCustomer(customer); // Required
    origin.addItem(item); // Optional

API request
...........

You need built `origin` created in previous step to save in in Talkable.
If you have, you need call method like in the example below:

.. code-block:: java

    TalkableApi.createOrigin(origin, new Callback2<Origin, Offer>() {
        @Override
        public void onSuccess(Origin origin, Offer offer) {
            // Process success
        }

        @Override
        public void onError(ApiError error) {
            // Process error
        }
    });

Retrieve rewards
----------------

This methods is used for retrieving rewards for user. Example:

.. code-block:: java

    TalkableApi.retrieveRewards(new Callback1<Reward[]>() {
        @Override
        public void onSuccess(Reward[] rewards) {
            // Process success
        }

        @Override
        public void onError(ApiError error) {
            // Process error
        }
    });

If you need get only rewards with some status or for other than user UUID,
you need to pass this data to this method. Example:

.. code-block:: java

    Params params = new Params();
    params.put("status", "Paid"); // Optional
    params.put("visitor_uuid", "eb71e496-6567-41ec-a68c-49e96d101e0e"); // Some other uuid, optional
    TalkableApi.retrieveRewards(params, new Callback1<Reward[]>() {
        @Override
        public void onSuccess(Reward[] rewards) {
            // Process success
        }

        @Override
        public void onError(ApiError error) {
            // Process error
        }
    });

Retrieve offer
--------------

This method is used to get offer details by it’s short code. Example:

.. code-block:: java

    String shortUrlCode = "ABCXYZ";
    TalkableApi.retrieveOffer(shortUrlCode, new Callback1<Offer>() {
        @Override
        public void onSuccess(Offer newOffer) {
            // Process success
        }

        @Override
        public void onError(ApiError e) {
            // Process error
        }
    });

Create offer share
------------------

If you have your own sharing mechanism, you can create shares using API.
Firstly, you need to create offer using `registerOrigin <Create origin_>`_ method. Example:

.. code-block:: java

    OfferShare share = new OfferShare(offer, SharingChannel.OTHER);
    TalkableApi.createShare(share, new Callback2<OfferShare[], Reward>() {
        @Override
        public void onSuccess(OfferShare[] shares, Reward reward) {
            // Process success
        }

        @Override
        public void onError(ApiError e) {
            // Process error
        }
    });

.. container:: hidden

   .. toctree::
