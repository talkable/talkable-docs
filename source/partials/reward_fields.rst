* **id** — unique reward ID
* **amount** — amount of money to reward (null when non-monetary incentive is used)
* **email** — email of the person that got reward
* **person** — parameters describing the person that got reward

  .. include:: /partials/person_fields.rst

* **incentive** — type of incentive reward (`rebate`, `discount_coupon`, `other`)
* **incentive_description** — verbal reward explanation
* **reward_coupon_code** — Coupon code received by person as a reward (present if incentive equals `discount_coupon`)
* **origin** — contains data about the event that issued an offer

  .. include:: /partials/origin_fields.rst
