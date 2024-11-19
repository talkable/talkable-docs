.. _advanced_features/multi_currency:
.. include:: /partials/common.rst

.. meta::
   :description: Talkable supports working with multiple currencies within the same site.

Multi-currency
==============

By default, Talkable works in a single-currency mode. The main currency is chosen during the account setup.

However, the multi-currency mode can be enabled for a site. In multi-currency mode, the referral campaigns allow
Advocates and Friends to choose their preferred currency, and the incentives can be configured to offer different
rewards based on the preferred currency. Every purchase and/or event should have a currency specified.
The dashboard and reports can be filtered by currencies, and the values can be converted to a currency of your choice.

.. note::

   Please contact your Customer Success Manager to enable multi-currency. Note that in this mode,
   the integration should pass currency data with every purchase.

Passing currency with the purchase or event
-------------------------------------------

Currency is required to be specified if multi-currency mode is enabled for a site.

Please pass the currency using the `currency_iso_code` argument to the `register_purchase` function.
The code must be in `ISO 4217 format <https://www.iso.org/iso-4217-currency-codes.html>`_, e.g. "USD".

:ref:`More on the integration of purchases <integration/custom/integration_components/post_purchase_script>`

Incentives for different currencies
-----------------------------------

In multi-currency mode, the following incentive details can be configured per currency:

* incentive amount
* coupon list or multi-use coupon
* subtotal minimum and maximum

A reward for an Advocate or a Friend will be issued based on their preferred currency. If none specified,
the main site currency will be used.

.. image:: /_static/img/advanced_features/multi_currency_incentive.png

Preferred currency
------------------

Talkable allows storing an Advocate's or Friend's preferred currency. The selected currency can be accessed in |liquid|
in the `[[ preferred_currency ]]` variable.

.. image:: /_static/img/advanced_features/multi_currency_advocate_offer.png

Passing visitor's preferred currency
....................................

If the preferred currency of the visitor is known, it can be passed as customer data to render the referral campaign
with the currency pre-selected:

.. code-block:: javascript

   _talkableq.push(['authenticate_customer', {
     email: '',
     currency: 'AUD' // Currency should be an international 3-letter code as defined by the ISO 4217 standard
   }]);

Currency can also be provided directly in any of the following function calls,
overriding the `authenticate_customer` data:

  - `register_affiliate`
  - `register_purchase`
  - `register_event`

For example:

.. code-block:: javascript

   var _purchase_data = {
     purchase: {
       order_number: '',
       subtotal: '',
       currency_iso_code: 'AUD' // currency of the purchase
     },
     currency: 'AUD', // preferred currency of the person, used to show suitable incentive information in the campaign
   };
   _talkableq.push(['register_purchase', _purchase_data]);

.. note::

   Passing `currency` is available in integration version 5.2.1 or higher.

Currencies on dashboard
-----------------------

Dashboard tiles have two helpful configuration options for multi-currency setup:

* filter events by currencies ("Segment Currency")
* convert all amounts to one currency ("Reporting Currency")

.. image:: /_static/img/advanced_features/multi_currency_dashboard_tile.png

.. note::

   Conversion rate for a specific currency is actualized daily (data taken from
   `open exchange rates <https://openexchangerates.org>`_) and cached for the accuracy of historical data.
   So a purchase amount is converted according to its creation date's conversion rate.

Currencies in reports
---------------------

Several tools can be used for multi-currency sites to make reporting more flexible.

Available options in **Metrics Aggregation Report**:

* segmentation by currencies
* filter by the currency of the purchase/event
* select a currency to convert the amounts to

.. image:: /_static/img/advanced_features/multi_currency_mar.png
  :width: 300

.. note::

   If a currency to convert to is not specified, the site currency is used for conversion.

Available options in **Purchases** and **Events** reports:

* filter by the currency of the purchase/event
* select a currency to convert the amounts to

.. note::

   The options list in the currency filter consists of all the currencies passed to Talkable
   along with the purchases/events. If you can't find a currency in the list, it means Talkable never received
   a purchase/event with such currency.

Shopify discounts
-----------------

At checkout, Shopify converts these fixed-amount discounts into the customer’s local currency using the store's
defined currency settings. The conversion adheres to the exchange rates Shopify provides, ensuring customers see
discounts in their familiar currency, enhancing transparency and trust during international transactions.

For example:

* A fixed discount of **$10 USD** will display as **€9 EUR** if the conversion rate at the time of checkout is 1 USD = 0.9 EUR.

Shopify performs this conversion dynamically based on the customer's selected currency, simplifying the shopping
experience for international buyers. For more details, refer to Shopify's guide on
`international pricing and discounts <https://help.shopify.com/en/manual/international/pricing/discounts>`_.

**We proactively manage price rule values, such as:**

* Discount Amounts
* Prerequisite Subtotal Ranges

If an exchange rate changes significantly, our system automatically recalculates these values to ensure pricing rules
remain fair and aligned with the intended value of the discount. This adjustment process minimizes manual updates for
merchants and prevents discrepancies in pricing across currencies.

.. note::

    Our product uses **own exchange rates**, which are updated automatically every 24 hours
