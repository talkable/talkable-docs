.. raw:: html

   <h2>Incentive types</h2>

Incentives can be of 3 following general types.

* **Rebate** (`rebate`) — monetary reward, certain amount of money that should
  be paid out to a customer with a given email. The merchants’ payment system
  should handle the payment.
* **Coupon code** (`discount_coupon`) — a discount coupon is issued to user.
  Talkable handles distributing this type of incentives.
* **Non-monetary** (`other`) — used when a campaign has a non-monetary rebate
  like *"Free T-shirt"* or *"One Month Free"*. This should be handled on the
  merchant’s side. More information on the reward is specified in
  `incentive_description`.
