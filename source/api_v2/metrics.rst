.. _api_v2/metrics:
.. include:: /partials/common.rst

.. meta::
   :description: This API allows you to access Talkable metrics.

Metrics
=======

This API allows you to access Talkable metrics. Go to Reports → Metric
descriptions to see the list of available metrics.

|br|

.. code-block:: text

   GET /metrics/<metric>

Returns a metric value which includes plain value, formatted value and result’s type.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   metric            Specific metric name.
   start_date        Start of the period for which data is pulled, inclusively.
   end_date          End of the period for which data is pulled, inclusively.
   campaign_ids      Optional: array of campaign ids for which data
                     is pulled. See the
                     :ref:`Campaigns API <api_v2/campaigns>`.
   campaign_tags     Optional: array of campaign tags for which data
                     is pulled. See the
                     :ref:`Campaigns API <api_v2/campaigns>`.
   campaign_status   Optional: campaign status for which data is pulled.

                     Options: `live`, `test`, `scheduled`, `disabled`.
   sharing_channels  Optional: array of specific sharing channels
                     for which data is pulled.

                     Options: `coupon`, `email`, `reminder`, `facebook`,
                     `facebook_sponsored`, `twitter`, `sms`, `linkedin`,
                     `other` or custom.
   traffic_sources   Optional: array of traffic sources for which data
                     is pulled.
   precision         Optional: integer value of precision for the result.
   mobile_visitor    Optional: boolean value. `true` - for only mobile visitors,
                     `false` - for only desktop visitors.
   ================= ========================================================

  |br|

  .. code-block:: text

    GET /metrics/<metric>/detalize

  Returns a metric value which includes plain value, formatted value, result’s type and all detalized information.

  .. container:: ptable

     ================= ========================================================
     Parameter         Description
     ================= ========================================================
     site_slug         Your Talkable Site ID. You can get this from your
                       Talkable dashboard after you log in and create a site.
     metric            Specific metric name.
     start_date        Start of the period for which data is pulled, inclusively.
     end_date          End of the period for which data is pulled, inclusively.
     detalize_by       JSON object with specific detalization parameters for
                       which data is pulled.

                       Options:
                        - `period: "day"/"week"/"month"/"quarter"`
                        - `sharing_channels: true`,
                        - `traffic_sources: true`,
                        - `event_categories: true`.
                        - `campaigns: true`
                        - `split_test: KEY_OF_A/B_TEST`
     campaign_ids      Optional: array of campaign ids for which data
                       is pulled. See the
                       :ref:`Campaigns API <api_v2/campaigns>`.
     campaign_tags     Optional: array of campaign tags for which data
                       is pulled. See the
                       :ref:`Campaigns API <api_v2/campaigns>`.
     campaign_status   Optional: campaign status for which data is pulled.

                       Options: `live`, `test`, `scheduled`, `disabled`.
     sharing_channels  Optional: array of specific sharing channels
                       for which data is pulled.

                       Options: `coupon`, `email`, `reminder`, `facebook`,
                       `facebook_sponsored`, `twitter`, `sms`, `linkedin`,
                       `other` or custom.
     traffic_sources   Optional: array of traffic sources for which data
                       is pulled.
     precision         Optional: integer value of precision for the result.
     mobile_visitor    Optional: boolean value. `true` - for only mobile visitors,
                       `false` - for only desktop visitors.
     ================= ========================================================

Example
-------

Offers metric
.............

.. code-block:: text

   GET https://www.talkable.com/api/v2/metrics/offers?site_slug=my-store&start_date=2014-09-01&end_date=2014-10-01&campaign_ids=35944,12345&campaign_tags=invite,test&campaign_status=live

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "plain": 1234,
       "formatted": "1234",
       "result_type": "number"
     }
   }

Revenue percentage metric with precision
........................................

.. code-block:: text

   GET https://www.talkable.com/api/v2/metrics/offers?site_slug=my-store&start_date=2014-09-01&end_date=2014-10-01&precision=2

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "plain": 34.35,
       "formatted": "34.35%",
       "result_type": "percent"
     }
   }

Average order value metric
..........................

.. code-block:: text

   GET https://www.talkable.com/api/v2/metrics/average_order_value?site_slug=my-store&start_date=2014-09-01&end_date=2014-10-01

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "plain": 5432,
       "formatted": "$5432",
       "result_type": "money"
     }
   }

Detalized metric
................

.. code-block:: text

  GET https://admin.talkable.com/api/v2/metrics/shares/detalize?site_slug=my-store&start_date=2019-12-25&end_date=2020-01-21&sharing_channels%5B%5D=Email&sharing_channels%5B%5D=SMS&detalize_by%5Bsharing_channels%5D=true&detalize_by%5Bperiod%5D=month

Sample response:

.. code-block:: javascript

  {
    "ok": true,
    "result": {
      "detalized": [
        {
          "formatted": "765",
          "period": "12/25/19 - 12/31/19",
          "plain": 765,
          "result_type": "number",
          "sharing_channel": "Email"
        },
        {
          "formatted": "567",
          "period": "1/1/20 - 1/21/20",
          "plain": 567,
          "result_type": "number",
          "sharing_channel": "Email"
        },
        {
          "formatted": "123",
          "period": "12/25/19 - 12/31/19",
          "plain": 123,
          "result_type": "number",
          "sharing_channel": "SMS"
        },
        {
          "formatted": "321",
          "period": "1/1/20 - 1/21/20",
          "plain": 321,
          "result_type": "number",
          "sharing_channel": "SMS"
        }
      ]
    }
  }
