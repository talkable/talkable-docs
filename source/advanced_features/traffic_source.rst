.. _advanced_features/traffic_source:
.. include:: /partials/common.rst

.. meta::
   :description: While driving traffic to one of your campaigns, you can include a traffic source parameter as a URL query string. This will help to segment your reporting.

Segment With Traffic Source
===========================

When driving traffic to one of your campaigns, you can include a traffic source
parameter as a URL query string to help segment your reporting. This is helpful
when you are driving traffic from many different sources to the same campaign.
This makes sense to do for both on-site and off-site call to actions where you
want to specifically track your traffic source. For example, if you are driving
traffic on-site to your Standalone campaign both from your home page navigation
bar and from your footer template, and you wanted to see which one is more high
value and driving more traffic to your campaign, you could look at the different
traffic sources in reporting to clearly see this.

How to use the traffic_source parameter in a call to action:

Say you have a Standalone integration displaying a campaign on www.yoursite.com/share.
You could append the traffic_source parameter on to your footer call to action as seen below:

``www.yoursite.com/share?traffic_source=footer``

.. container:: hidden

   .. toctree::
