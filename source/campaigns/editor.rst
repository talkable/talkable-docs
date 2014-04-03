.. _campaigns/editor:
.. include:: /partials/common.rst

Editor
======

Variables
---------

Each Curebit view has its own set of Variables which can be used in template.

Files
-----

Allows to upload and use images, fonts, etc for campaign purposes.

History
-------

Whenever view or stylesheet is updated editor saves changes in History.

Extra
-----

Allows to configure additional options for each view.

Filters
-------

`Standard liquid filters`_ that are available out of box.

.. raw:: html

   <h3>Curebit Filters</h3>

asset\_url
..........

Insert link for a uploaded asset.

.. code-block:: liquid

   {{ "image.jpg" | asset_url }}

Example: http://d2jjzw81hqbuqv.cloudfront.net/static_assets/files/745/original/offer-background.jpg

|hr|

direct\_asset\_url
..................

Asset URL without CDN. Required only for custom fonts to work.

.. code-block:: liquid

   {{ "font.woff" | direct_asset_url }}

|hr|

interpolate
...........

Allows inline string interpolation using %{} syntax.

.. code-block:: liquid

   {{ "Get %{referrer_amount} Off" | interpolate }}

|hr|

.. _liquid_filter_format_date:

format\_date
............

Format date for current localization.
Default format: Apr 04, 2014

.. code-block:: liquid

   {{ valid_until | format_date }}
   {{ valid_until | format_date: "%Y-%m-%d" }}

|hr|

split\_test
...........

Split testing static text:

.. code-block:: liquid

   {{ "split_test_identifier" | split_test: "Label 1", "Label 2", "Label N" }}

Split testing text with interpolation:

.. code-block:: liquid

   {{ "share_via_email_subject" | split_test: "%{site_name}",
      "Your friend %{referrer_email} shared this deal with you" | interpolate }}

Split testing an asset:

.. code-block:: liquid

   {{ "offer_background" | split_test: "background-green.jpg", "background-red.jpg" | asset_url }}

|hr|

simple\_format
..............

Formats plain text to have HTML formatting. E.g. replace ``\n`` with ``<br/>``.

.. code-block:: liquid

   {{ "Hello %{referrer_email}\nHere is your reward." | simple_format | interpolate }}

Returns ``Hello John<br/>Here is your reward``.

|hr|

money
.....

Formats number using current currency.

.. code-block:: liquid

   {{ "50" | money }}

Returns ``$50.00``.

Avaliable options: ``int precision``, ``bool strip_insignificant_zeros``.

.. code-block:: liquid

   {{ "100.11" | money: precision: 0 }}

Returns ``$100``.

.. code-block:: liquid

   {{ "100.99" | money: precision: 0 }}

Returns ``$101``.

.. code-block:: liquid

   {{ "100.99" | money: strip_insignificant_zeros: true }}

Returns ``$100.99``.

.. code-block:: liquid

   {{ "100.90" | money: strip_insignificant_zeros: true }}

Returns ``$100.9``.

.. code-block:: liquid

   {{ "100.00" | money: strip_insignificant_zeros: true }}

Returns ``$100``.

.. _Standard liquid filters: https://github.com/Shopify/liquid/wiki/Liquid-for-Designers#standard-filters
