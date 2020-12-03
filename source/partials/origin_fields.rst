* **type**

  * *"Purchase"* for post-purchase placement
  * *"AffiliateMember"* for standalone, floating widget, or gleam placements
  * *"Event"* for post-event placement (such as a signup page which triggers a
      referral campaign)

* **id** — unique identifier of the origin event
* **email** — email address of the |advocate| person
* **customer_id** - unique external identifier of a customer who triggered the origin event
* **traffic_source** — traffic source of the origin event
* **ip_address** - IP address of the origin event

*For Purchase:*

 * **order_number** - unique identifier of the Purchase
 * **subtotal** - order subtotal for the purchase
 * **coupon_code** - coupon code used with the purchase

*For Event:*

 * **event_category** - identifier of an action that trigger the Event (e.g. ``app_installed``)
 * **event_number** - unique identifier of the Event within the associated **event_category**
 * **subtotal** - optional monetary attribute of the Event
 * **coupon_code** - optional coupon code associated with the Event
