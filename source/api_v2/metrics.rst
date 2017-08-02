.. _api_v2/metrics:
.. include:: /partials/common.rst

Metrics
=======

This API allows you to access Talkable metrics. Go to Reports -> Metric
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
   ================= ========================================================

Example
-------

Offers metric
.............

.. code-block:: text

   GET https://www.talkable.com/api/v2/metrics/offers?site_slug=my-store&start_date=2014-09-01&end_date=2014-10-01&campaign_ids=35944,12345&campaign_tags=invite,test&campaign_status=live&api_key=i9uil7nQgDjucCiTJu

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

   GET https://www.talkable.com/api/v2/metrics/offers?site_slug=my-store&start_date=2014-09-01&end_date=2014-10-01&precision=2&api_key=i9uil7nQgDjucCiTJu

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

   GET https://www.talkable.com/api/v2/metrics/average_order_value?site_slug=my-store&start_date=2014-09-01&end_date=2014-10-01&api_key=i9uil7nQgDjucCiTJu

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
