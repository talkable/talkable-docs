.. _campaigns/editor/variables:
.. include:: /partials/common.rst

.. meta::
  :description: Variables show you dynamic data such as Campaign tag, Advocate info, etc.

.. _editor_variables:

Variables
=========

Variables are used to show dynamic data like Campaign tag, Advocate info, etc.
|br|
All Variables are enclosed into ``{{ }}`` which means
`Liquid Output <https://shopify.dev/api/liquid#liquid-syntax>`_.

Each Campaign View has its own set of Variables located inside Editor
navigation:

.. image:: /_static/img/editor/vars-menu-item.png
  :alt: Variables: menu item

|br|

Each Variable is represented with Name, Liquid notation, Value:

.. image:: /_static/img/editor/vars-variable.png
  :alt: Variables: variable

* Name describes meaning of the Variable
* Notation explains how to write Variable inside Template/Styles editor area
* Value shows what this particular Variable results with (Value may be
  different between preview and production scenarious)

|br|

There are also variables marked as deprecated, those will be deleted in the future, so please do not use them.

List of deprecated variables:

* {{ advocate_offer.manual_signup }}
* {{ campaign_setup.tiers[0].id }}
* {{ campaign_setup.tiers[0].name }}
* {{ campaign_setup.tiers[0].threshold }}
* {{ campaign_setup.tiers[0].localized_range }}
* {{ campaign_setup.tiers[0].multiplier }}
* {{ campaign_setup.tiers[0].icon_url }}
* {{ campaign_setup.tiers[0].active }}


|br|
|hr|

.. _editor_variables_advocate_info:

{{ advocate_info }}
-------------------

**Available in**: all Views |br|
**Type**: ``Object``

Personal data for |advocate|.

.. container:: ptable

  ==================== ========================= ==================================================================
  Property             Value                     Description
  ==================== ========================= ==================================================================
  email                "affiliate@example.com"   Advocate email he is registered with
  first_name           "John"                    Advocate first name provided on Signup
  last_name            "Smith"                   Advocate last name provided on Signup
  external_customer_id "1jsh17136"               Advocate unique ID passed by Merchant to :ref:`Talkable Integration
                                                 <integration/custom/integration_components/initialization_script>` as ``customer_id``
  sub_choice           false | true              Advocate custom parameter which can be used to pass additional
                                                 data to Advocate Signup/Share Page
  purchases_count      0                         Advocate number of tracked store purchases
  ==================== ========================= ==================================================================

|br|

{{ advocate_origin }}
---------------------

**Available in**: all Views |br|
**Type**: ``Object``

|origin| data for |advocate|.

.. container:: ptable

  ============================== ================================= =============================================================
  Property                       Value                             Description
  ============================== ================================= =============================================================
  id                             1234567890                        Advocate origin id
  new_customer                   false | true                      Advocate is a new customer or not
  created_at                     "2016-07-27T00:00:00.000+03:00"   Time when Advocate origin was created
  event_category                 "purchase"                        Advocate origin event category
  coupon_codes                   ["AD_DISCOUNT"]                   Coupon codes that are used in Advocate origin
  ip.address                     "52.6.41.1"                       Advocate IP address
  ip.qa                          false | true                      Shows if the IP address is listed as QA
  ip.location.country            "United States"                   Advocate geolocation country based on their IP address
  ip.location.city               "San Jose"                        Advocate geolocation city based on their IP address
  ip.location.country_code       "US"                              Advocate geolocation country code based on their IP address
  ip.location.subdivision_1_code "VA"                              Region-portion of the |iso3166| code for the 1st level region
                                                                   associated with the IP address
  ip.location.subdivision_1_code ""                                Region-portion of the |iso3166| code for the 2nd level region
                                                                   associated with the IP address
  product.sku                    "AJ7292-002"                      Product SKU
  product.title                  "Nike Air VaporMax 95"            Product title
  product.url                    "https://bit.ly/2IPp0rX"          Product URL
  product.image_url              "https://bit.ly/2GuVAMQ"          Product image URL
  product.description            "Cool sneakers"                   Product description
  product.custom_properties      {"price": "190"}                  Product custom properties
  ============================== ================================= =============================================================

|br|

{{ coupon_code }}
-----------------

**Available in**: Friend Claim Page, Advocate Redemption Email, Advocate Reward
Paid Email |br|
**Type**: ``String``

Coupon Code is given to a person as a Reward based on Incentive (condition of
giving out the Reward).

When you want to use this Variable always keep in mind who you want to
show it to because it has a scope:

* for Views which name starts with |advocate| it means Advocate Coupon Code
* for Views which name starts with |friend| it means Friend Coupon Code

.. image:: /_static/img/editor/vars-friend-coupon-code.png
  :alt: Variables: friend coupon code

|br|

Make sure Incentives are correct:

* If its ``single-use`` Coupon Code, make sure Coupon List exist and it has
  enough coupons and they are valid in terms of uniqueness and validity
* If its ``multi-use`` Coupon Code, make sure it has a correct value

.. image:: /_static/img/editor/vars-coupon-list.png
  :alt: Variables: coupon list

|hr|

{{ incentives }}
----------------

**Available in**: all Views |br|
**Type**: ``Object``

Reflects entire Campaign Incentives list including. This object can include
several Incentives which are also objects.

Here is an example of ``{{ incentives }}`` Variable with two incentives:
|advocate| and |friend|:

.. code-block:: javascript

  {
    advocate: {
      amount: 10.0,
      description: "$10",
      percentage: false
    },
    friend: {
      amount: 100.0,
      description: "100%",
      percentage: true
    }
  }

And here is an example of using ``{{ incentives }}`` values:

.. code-block:: liquid

  Give your friend {{ incentives.friend.description }} OFF!

Which outputs:

.. code-block:: text

  Give your friend 100% OFF!

.. list-table::
  :widths: 25 25 50
  :header-rows: 1

  * - Property
    - Value
    - Description
  * - Liquid slug
    - "referrer"
    - Incentive identifier
  * - amount
    - 50.0
    - Incentive amount (float)
  * - description
    - "$50"
    - Formatted Incentive including currency and amount
  * - percentage
    - true | false
    - Type of Incentive amount: fixed or percentage
  * - required_actions
    - 0
    - Number of required actions to trigger reward (i.e. 2 purchases
      needed to trigger reward)
