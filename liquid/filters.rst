.. _liquid/standard:
.. include:: /partials/common.rst

Filters
==============

Liquid filters
--------------

`Standard liquid filters <https://github.com/Shopify/liquid/wiki/Liquid-for-Designers#standard-filters>`__ that are available out of box.

Curebit filters
---------------

asset\_url
~~~~~~~~~~

Insert link for a uploaded asset.

.. code-block:: html

    {{ "image.jpg" | asset_url }}

Example: http://d2jjzw81hqbuqv.cloudfront.net/static_assets/files/745/original/offer-background.jpg

direct\_asset\_url
~~~~~~~~~~~~~~~~~~

Asset URL without CDN. Required only for custom fonts to work.

.. code-block:: html

    {{ "font.woff" | direct_asset_url }}

interpolate
~~~~~~~~~~~

Allows inline string interpolation using %{} syntax.

.. code-block:: html

    {{ 'Get %{referrer_amount} Off' | interpolate }}

format\_date
~~~~~~~~~~~~

Format date for current localization.

.. code-block:: html

    {{ valid_until | format_date: "%Y-%m-%d" }}

split\_test
~~~~~~~~~~~

Split testing static text:

.. code-block:: html

    {{ 'split_test_identifier' | split_test: 'Label 1', 'Label 2', 'Label N' }}

Split testing text with interpolation:

.. code-block:: html

    {{ 'share_via_email_subject' | split_test: 'Get %{referred_amount} off %{site_name}',
       'Your friend %{referrer_email} shared this deal with you' | interpolate }}

Split testing an asset:

.. code-block:: html

    {{ 'offer_background' | split_test: 'background-green.jpg', 'background-red.jpg' | asset_url }}

simple\_format
~~~~~~~~~~~~~~

Formats plain text to have HTML formatting. E.g. replace ``\n`` with ``<br/>``.

.. code-block:: html

    {{ 'Hello %{referrer_email}\nHere is your reward.' | simple_format | interpolate }}

Returns ``Hello John<br/>Here is your reward``.

money
~~~~~

Formats number using current currency.

.. code-block:: html

    {{ "50" | money }}

Returns ``$50.00``.

Avaliable options: ``int precision``, ``bool strip_insignificant_zeros``.

.. code-block:: html

    {{ "100.11" | money: precision: 0 }}

Returns ``$100``.

.. code-block:: html

    {{ "100.99" | money: precision: 0 }}

Returns ``$101``.

.. code-block:: html

    {{ "100.99" | money: strip_insignificant_zeros: true }}

Returns ``$100.99``.

.. code-block:: html

    {{ "100.90" | money: strip_insignificant_zeros: true }}

Returns ``$100.9``.

.. code-block:: html

    {{ "100.00" | money: strip_insignificant_zeros: true }}

Returns ``$100``.
