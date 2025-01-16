.. _advanced_features/segments:
.. include:: /partials/common.rst

.. meta::
   :description: While driving traffic to one of your campaigns, you can include a traffic source parameter as a URL query string. This will help to segment your reporting.

Segments
========

When driving traffic to one of your campaigns, you can include a segment
parameters to help segment your reporting.

Segment With Product SKU
------------------------

Sometimes there is a need to show a Campaign on Post Purchase Placement only to those customers who
purchased a particular product or a set of products. In this case you can put such a limitation inside Campaign Join Criteria.
To do that visit Campaign Details page → Go into Rules → Advanced → Campaign Join Criteria field and put the following
criteria in there:

.. code-block:: html

   {% assign available_items = "sku1,sku2" | split: "," %}
   {% assign user_items = advocate_origin.products | map: "product_id" %}
   {% assign result = false %}

   {% for available_item in available_items %}
     {% for user_item in user_items %}
       {% if user_item == available_item %}
         {% assign result = true %}
         {% break %}
       {% endif %}
     {% endfor %}
   {% endfor %}

   {{ result }}

Now only those customers who purchased a product with SKU of "SKU_GOES_HERE" will see a Campaign.
The Campaign won’t show for any other product purchased.

.. note::

   In order to use this Campaign Join Criteria you need to make sure that the SKU numbers are passed
   throught the integration first of all. To do that you need to go into Reports
   (top header navigation) → Purchases → Click on "Details" link of any purchase and make sure there is "Product Id"
   column with a valid "Product ID" value in place.
   If there is no such column or it is blank you cannot use this feature unless you pass the following instructions
   :ref:`Including Product Items <advanced_features/product_items>`.

Please |contact_us| if you have any questions.

Segment With Traffic Source
---------------------------

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

Custom Segments
---------------

For individual purchase segmentation, you have the option to utilize three custom segments: `segment1`, `segment2`, `segment3`.
Each of these segments can represent various criteria such as location, age group, traffic source, etc.
These segments offer flexibility in categorizing purchases based on different customer characteristics or transaction attributes.

Example of usage with `register_purchase`:

.. include:: /partials/purchase_script.rst

Example of usage with `authenticate_customer`:

 .. code-block:: javascript

       window._talkableq.push(['authenticate_customer', {
         email: '', // Email of the customer. Example: 'customer@example.com'
         first_name: '', // First name of the customer. Example: 'John'
         last_name: '', // Last name of the customer. Example: 'Doe'
         traffic_source: '', // The source of the traffic driven to the campaign. Example: 'facebook'
         segment1: '', // Custom segment (e.g., location, age group, source channel, platform, gender, interests).
         segment2: '', // Custom segment (e.g., location, age group, source channel, platform, gender, interests).
         segment3: '' // Custom segment (e.g., location, age group, source channel, platform, gender, interests).
       }]);

In this example, `segment1`, `segment2`, and `segment3` attributes are passed through `authenticate_customer` to enable segmentation without requiring an Origin creation.

.. note::

   Segments can also be passed in `register_affiliate`, `register_purchase`, and `register_event`, providing flexibility for different integration scenarios.

This approach simplifies custom data handling for customers, allowing for unified data across various methods and optimizing segmentation management without additional calls.
