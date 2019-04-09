* **email** — person’s email address
* **first_name** — person’s first name
* **last_name** — person’s last name
* **username** — person’s username (optional)
* **sub_choice** — subscription choice (optional, present only if the form
  included subscription checkbox)
* **subscribed_at** — date person has subscribed (deprecated; use opted_in_at instead)
* **opted_in_at** — date person has subscribed (optional)
* **unsubscribed_at** — date person has unsubscribed (optional)
* **custom_properties** — hash of person’s custom properties (optional)
* **referral_counts** - subhash of |advocate|'s referral counts

  * **total** — created referrals count
  * **approved** — approved referrals count
  * **pending** — count of waiting for approval referrals

