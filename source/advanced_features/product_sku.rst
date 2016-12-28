.. _advanced_features/product_sku:
.. include:: /partials/common.rst

Segment With Product SKU
========================

Sometimes there is a need to show a Campaign on Post Purchase Placement only to those customers who
purchased a particular product or a set of products. In this case you can put such a limitation inside Campaign Join Criteria.
To do that visit Campaign Details page -> Go into Rules -> Advanced -> Campaign Join Criteria field and put the following
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
The Campaign won't show for any other product purchased.

.. note::
  In order to use this Campaign Join Criteria you need to make sure that the SKU numbers are passed
  throught the integration first of all. To do that you need to go into Reports
  (top header navigation) -> Purchases -> Click on "Details" link of any purchase and make sure there is "Product Id"
  column with a valid "Product ID" value in place.
  If there is no such column or it is blank you cannot use this feature unless you pass the following instructions
  :ref:`Including Product Items <advanced_features/product_items>`.

Please |contact_us| if you have any questions.


.. container:: hidden

   .. toctree::
