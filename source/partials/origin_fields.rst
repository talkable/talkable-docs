* **type**

  * *"Purchase"* for post-purchase placement
  * *"AffiliateMember"* for standalone, floating widget, or gleam placements
  * *"Event"* for post-event placement (such as a signup/share page which triggers a
      referral campaign)

* **id** — unique identifier of the origin event
* **email** — email address of the person
* **customer_id** — unique external identifier of a customer who triggered the origin event
* **traffic_source** — traffic source of the origin event
* **ip_address** — IP address of the origin event

*For Purchase:*

 * **order_number** — unique identifier of the Purchase
 * **subtotal** — order subtotal for the Purchase
 * **currency_iso_code** — currency code of the Purchase, defaults to the Site's currency
 * **coupon_code** — coupon codes used with the Purchase (separated by ``,`` if multiple)
 * **order_date** — date of the Purchase

*For Event:*

 * **event_category** — identifier of an action that trigger the Event (e.g. ``app_installed``)
 * **event_number** — unique identifier of the Event within the associated **event_category**
 * **subtotal** — optional monetary attribute of the Event
 * **currency_iso_code** — currency code of the Event, defaults to the Site's currency
 * **coupon_code** — coupon codes used with the Event (separated by ``,`` if multiple)
