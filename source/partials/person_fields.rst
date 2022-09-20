* **email** — |person|’s email address
* **phone_number** — |person|’s phone number (optional)
* **first_name** — |person|’s first name (optional)
* **last_name** — |person|’s last name (optional)
* **username** — |person|’s username (optional)
* **sub_choice** — subscription choice (optional, present only if the form
  included subscription checkbox)
* **subscribed_at** — date |person| has subscribed (deprecated; use ``opted_in_at`` instead)
* **opted_in_at** — date |person| has subscribed (optional)
* **phone_opted_in_at** — date |person| has subscribed with email (optional)
* **unsubscribed_at** — date |person| has unsubscribed with phone number (optional)
* **custom_properties** — hash of |person|’s custom properties (optional)
* **is_loyalty_member** — whether the |person| participates in loyalty program
* **loyalty_member** — details of the |person| as a loyalty program participant (optional)
* **referral_counts** — referral counts of |person| as |advocate|

  * **total** — created referrals count
  * **approved** — approved referrals count
  * **pending** — count of waiting for approval referrals

* **gender** [deprecated]
