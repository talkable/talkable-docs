.. _campaigns/editor/filters:
.. include:: /partials/common.rst

Filters
-------

`Standard liquid filters`_ that are available out of box.

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

simple\_format
..............

Formats plain text to have HTML formatting. E.g. replace ``\n`` with ``<br/>``.

.. code-block:: liquid

   {{ "Hello [[advocate_info.email]]\nHere is your reward." | simple_format | interpolate }}

Returns ``Hello John<br/>Here is your reward``.

|hr|

encode\_query\_argument
.......................

Encodes a string to be included in a URL.

.. code-block:: liquid

   http://example.com/?utm_campaign={{ "Campaign Name" | encode_query_argument }}

Returns ``Campaign%20Name``, so the URL will be
``http://example.com/?utm_campaign=Campaign%20Name``.

|hr|

rand\_by
........

Produces a random value which is always the same for specific parameters passed.
First parameter is a maximum random number.

Simple example:

.. code-block:: liquid

   {{ "100" | rand_by: "param1", "param2" }}

Always returns ``29``.

Interpolation as a parameter:

.. code-block:: liquid

   {{ "10" | rand_by: advocate_info.email }}

Always returns the same number for a specific email, between 0 and 10.

|hr|

.. _liquid_filter_split_test:

split\_test
...........

Split testing static text:

.. code-block:: liquid

   {{ "split_test_identifier" | split_test: "Label 1", "Label 2", "Label N" }}

Split testing text with interpolation:

.. code-block:: liquid

   {{ "share_via_email_subject" | split_test: "[[site_name]]",
      "Your friend [[advocate_info.email]] shared this deal with you" | interpolate }}

Split testing an asset:

.. code-block:: liquid

   {{ "offer_background" | split_test: "background-green.jpg", "background-red.jpg" | asset_url }}

Split testing style:

.. code-block:: html

   <body style="background-color: {{ 'offer_background' | split_test: '#d3d3d3', '#ff0000' }}">
     ...
   </body>

.. code-block:: html

   <h1 style="font-size: {{ 'title_size' | split_test: '24px', '30px' }}">
     Sample Title
   </h1>

|hr|

split\_test\_with\_probability
...........

Split testing static text with different probabilities:

.. code-block:: liquid

   {{ "split_test_identifier" | split_test_with_probability: "Label 1", 25,  "Label 2", 25,  "Label N", 50 }}

   {{ "split_test_identifier" | split_test_with_probability: "Label 1", 25,  "Label 2", 75 }}

Probability - integer value between 1 and 100

Split testing for text with interpolations or image assets works similar to the standard :ref:`split\_test <liquid_filter_split_test>`

|hr|

.. _liquid_filter_format_date:

format\_date
............

Format date for current localization.

Default format: Apr 04, 2014

Reference to all available formatting can be found in `strftime documentation`_

.. _strftime documentation: http://apidock.com/ruby/DateTime/strftime

.. code-block:: liquid

   {{ valid_until | format_date }}
   {{ valid_until | format_date: "%Y-%m-%d" }}
   {{ current_time | format_date }}

|hr|

interpolate
...........

Allows inline string interpolation using [[ ]] syntax.

.. code-block:: liquid

   {{ "Get [[incentives.click.amount | money]] Off" | interpolate }}

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

|hr|

strip
.....

Removes leading and trailing blank symbols from the string.

.. code-block:: liquid

   {{ "    strip me " | strip }}

Returns ``strip me``.

|hr|

tweet\_length
.............

Calculates a tweet length for the string.

.. code-block:: liquid

   {{ "wow this is a tweet http://example.com" | tweet_length }}

Returns ``42``.

|hr|

parse\_json
...........

Parses the JSON string source into a Liquid data structure.

.. code-block:: liquid

   {% assign var = '{"key": "value"}' | parse_json %}
   {{ var.key }}

Returns ``value``.

|hr|

claim\_url
..........

Returns channel-specific claim URL.

.. code-block:: liquid

   {{ "facebook" | claim_url }}
   {{ "linkedin" | claim_url }}
   {{ "twitter" | claim_url }}

.. _Standard liquid filters: https://github.com/Shopify/liquid/wiki/Liquid-for-Designers#standard-filters
