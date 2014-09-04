.. _api_v2/metrics:
.. include:: /partials/common.rst

Metrics
=======

This API allows you to access Talkable metrics. Go to Reports -> Metric
descriptions to see the list of available metrics.

|br|

.. code-block:: url

   GET /metrics/<metric>

Returns a metric value.

.. container:: ptable

   ================= ========================================================
   Parameter         Description
   ================= ========================================================
   site_slug         Your Talkable Site ID. You can get this from your
                     Talkable dashboard after you log in and create a site.
   metric            Specific metric name
   start_date        Start of the period for which data is pulled, including
   end_date          End of the period for which data is pulled, including
   campaign_slugs    Optional: array of campaign slugs for which data
                     is pulled
   ================= ========================================================

Example
-------

.. code-block:: url

   GET https://www.talkable.com/api/v2/metrics/offers?site_slug=my-store&start_date=2014-09-01&end_date=2014-10-01&campaign_slugs[]=35944-api-campaign&api_key=i9uil7nQgDjucCiTJu

Sample response:

.. code-block:: javascript

   {
     "ok": true,
     "result": {
       "metric": 12345
     }
   }
