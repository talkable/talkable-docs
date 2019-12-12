.. _campaigns/editor/filters:
.. include:: /partials/common.rst

.. meta::
   :description: Standard Liquid filters that are available out of box.

Filters
-------

`Standard liquid filters`_ that are available out of box.

import\_font
............

Inserts the font declaration to the page.

.. code-block:: text

   {{ "My Font" | import_font }}

Returns:

.. code-block:: css

   @font-face {
      font-family: 'My Font';
      src: url('https://d2jjzw81hqbuqv.cloudfront.net/static_assets/files/174201/original/font.woff') format('woff'), url('https://d2jjzw81hqbuqv.cloudfront.net/static_assets/files/174202/original/font.woff2') format('woff2');
      font-weight: normal;
      font-style: normal;
   }

|hr|

asset\_url
..........

Inserts link for an uploaded asset.

.. code-block:: liquid

   {{ "image.jpg" | asset_url }}

Example: http://d2jjzw81hqbuqv.cloudfront.net/static_assets/files/745/original/offer-background.jpg

|hr|

simple\_format
..............

Formats plain text to have HTML formatting. E.g. replace ``\n`` with ``<br/>``.

.. code-block:: text

   {{ "Hello [[advocate_info.email]]\nHere is your reward." | simple_format | interpolate }}

Returns ``Hello John<br/>Here is your reward``.

|hr|

encode\_query\_argument
.......................

Encodes a string to be included in a URL.

.. code-block:: text

   http://example.com/?utm_campaign={{ "Campaign Name" | encode_query_argument }}

Returns ``Campaign%20Name``, so the URL will be
``http://example.com/?utm_campaign=Campaign%20Name``.

|hr|

probability\_by
...............

This filter returns ``true`` or ``false`` for a dataset based on the probability you request:

.. code-block:: liquid

   {{ 50 | probability_by: "param1", "param2", "param3" }}

``50`` returns ``true`` in 50% cases for requested dataset. This filter provides the same result for a particular
dataset.

.. note:: probability should be always an integer value between ``1`` and ``100``.

Here is another example that returns ``true`` only in 10% cases for the interpolation variable:

.. code-block:: liquid

   {{ 10 | probability_by: advocate_info.email }}

You can ommit passing any parameters and the result will be based on the Advocate offer. Also you may use ``probability`` as an alias which is a little shorter to write:

.. code-block:: liquid

   {{ 50 | probability }}

This example can be used in ``Email sending condition`` of Advocate Offer Email template to send email only in 33% cases:

.. code-block:: liquid

   {% assign send_email = 33 | probability %}

   {% if send_email %}
     true
   {% endif %}

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

Always returns the same number for a specific email, between 0 and 9.

|hr|

regexp\_captures
................

Parses input with a given regexp and returning
`regular expression captures <http://www.regular-expressions.info/brackets.html>`_
as an array.

.. code-block:: liquid

   {{ '12345678' | regexp_captures: '(....)(....)' | join: '-' }}
   {{ 'bogdan@example.com' | regexp_captures: '^([a-z]+)\@([a-z]+)\.([a-z]+)' | json }}

|hr|

ab\_test
........

A/B testing static text:

.. code-block:: liquid

   {{ "ab_test_identifier" | ab_test: "Label 1", "Label 2", "Label N" }}

A/B testing text with interpolation:

.. code-block:: liquid

   {{ "share_via_email_subject" | ab_test: "[[site_name]]",
      "Your friend [[advocate_info.email]] shared this deal with you" | interpolate }}

A/B testing an asset:

.. code-block:: liquid

   {{ "offer_background" | ab_test: "background-green.jpg", "background-red.jpg" | asset_url }}

A/B testing style:

.. code-block:: liquid

   <body style="background-color: {{ 'offer_background' | ab_test: '#d3d3d3', '#ff0000' }}">
     ...
   </body>

.. code-block:: liquid

   <h1 style="font-size: {{ 'title_size' | ab_test: '24px', '30px' }}">
     Sample Title
   </h1>

|hr|

date\_diff
..........

Return absolute difference between two dates in seconds.

Date is compared to current time if no argument is passed.

All dates are interpreted in context of the site time zone
unless time zone is specified.

.. code-block:: text

   {{ valid_until | date_diff }}
   {{ valid_until | date_diff: 'Apr 4, 2019' }}
   {{ '2019-09-01 08:30:00' | date_diff: current_time }}

|hr|

date\_greater\_than
...................

Return boolean that indicates whether a date is more recent
than another date.

All dates are interpreted in context of the site time zone
unless time zone is specified.

.. code-block:: liquid

   {{ current_time | date_greater_than: valid_until }}
   {{ valid_until | date_greater_than: '2019-09-01 08:30:00' }}

|hr|

date\_greater\_than\_or\_equal
..............................

Return boolean that indicates whether a date is the same as
or more recent than another date.

All dates are interpreted in context of the site time zone
unless time zone is specified.

.. code-block:: liquid

   {{ current_time | date_greater_than_or_equal: valid_until }}
   {{ valid_until | date_greater_than_or_equal: '2019-09-01 08:30:00' }}

|hr|

add\_time
.........

Add a specified amount of time to a date and return the result.

Time unit defaults to seconds.

Available time units (can be used in plural form as well):

* ``second``
* ``minute``
* ``hour``
* ``day``
* ``week``
* ``fortnight``
* ``month``
* ``year``

.. code-block:: liquid

   {{ valid_until | add_time: 42 }}
   {{ valid_until | add_time: 3, 'months' }}

|hr|

.. _liquid_filter_format_date:

format\_date
............

Format date for current localization.

Default format: Apr 04, 2014

Reference to all available formatting can be found in `strftime documentation`_

Reference to all available locales can be found in `rails-i18n documentation`_

.. _strftime documentation: http://apidock.com/ruby/DateTime/strftime
.. _rails-i18n documentation: https://github.com/svenfuchs/rails-i18n#available-locales

.. code-block:: liquid

   {{ valid_until | format_date }}
   {{ valid_until | format_date: format: "%Y-%m-%d" }}
   {{ valid_until | format_date: locale: "ru" }}
   {{ valid_until | format_date: format: "%Y-%m-%d", locale: "ru" }}
   {{ current_time | format_date }}

|hr|

human\_time\_ago
................

Transform given time to time ago in words.

If given time is yesterday, returns ``1 day``.

Reference to all available locales can be found in `rails-i18n documentation`_

.. code-block:: liquid

   {{ valid_until | human_time_ago }}
   {{ valid_until | human_time_ago: locale: "ru" }}
   {{ current_time | human_time_ago }}

|hr|

hours\_from\_time
.................

Alias `hours_from_now`

Calculate difference between two dates. By default calculates between specified time and current time.

.. code-block:: text

   {{ "Sun, 02 Jan 2000 10:00:00 PST" | hours_from_time: "Sat, 01 Jan 2000 10:00:00 PST" }}
   {{ "2015-03-27 17:53" | hours_from_time: "2015-03-27 15:53" }}

Next two examples is equivalent.

.. code-block:: liquid

   {{ friend_offer.valid_until | hours_from_time: current_time }}
   {{ friend_offer.valid_until | hours_from_now }}

Pretty useful example for email sending criteria to prevent sending mail when offer is about to expire.

.. code-block:: liquid

   {% if friend_offer.valid_until %}
     {% assign difference = friend_offer.valid_until | hours_from_now %}
     {% if difference > 24 %}
       true
     {% else %}
       false
     {% endif %}
   {% else %}
     true
   {% endif %}

|hr|

interpolate
...........

Allows inline string interpolation using [[ ]] syntax.

.. code-block:: text

   {{ "Get [[incentives.click.amount | money]] Off" | interpolate }}

|hr|

md5
...

Calculates the MD5 hash of the string.

.. code-block:: liquid

   {{ "foo" | md5 }}

Returns ``acbd18db4cc2f85cedef654fccc4a4d8``.

|hr|

money
.....

Formats number using current currency.

.. code-block:: liquid

   {{ "50" | money }}

Returns ``$50.00``.

Available options:

* ``unit``
* ``separator``
* ``delimiter``
* ``format``
* ``precision (integer)``
* ``strip_insignificant_zeros (boolean)``

.. container:: ptable

   ============================================================== ==============
   Example                                                        Result
   ============================================================== ==============
   ``{{ "100.11" | money: precision: 0 }}``                       ``$100``
   ``{{ "100.99" | money: precision: 0 }}``                       ``$101``
   -------------------------------------------------------------- --------------
   ``{{ "100.99" | money: strip_insignificant_zeros: true }}``    ``$100.99``
   ``{{ "100.90" | money: strip_insignificant_zeros: true }}``    ``$100.9``
   ``{{ "100.00" | money: strip_insignificant_zeros: true }}``    ``$100``
   -------------------------------------------------------------- --------------
   ``{{ "100" | money: unit: "€" }}``                             ``€100.00``
   ``{{ "100" | money: unit: "" }}``                              ``100.00``
   -------------------------------------------------------------- --------------
   ``{{ "10049.99" | money: separator: "_" }}``                   ``$10,049_99``
   ``{{ "10049.99" | money: delimiter: "_" }}``                   ``$10_049.99``
   -------------------------------------------------------------- --------------
   ``{{ "100" | money: format: "%n %u", unit: "zł" }}``           ``100.00 zł``
   ============================================================== ==============

|hr|

strip
.....

Removes leading and trailing blank symbols from the string.

.. code-block:: text

   {{ "    strip me " | strip }}

Returns ``strip me``.

|hr|

squish
......

Returns the string, first removing all whitespace on both ends of the string, and then changing remaining consecutive whitespace groups into one space each.

.. code-block:: text

   {{ "   foo   bar        baz " | squish }}

Returns ``foo bar baz``.

|hr|

tweet\_length
.............

Calculates a tweet length for the string.

.. code-block:: text

   {{ "wow this is a tweet http://example.com" | tweet_length }}

Returns ``43``.

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

|hr|

group\_by
.........

Group an array’s items by a given property.

.. code-block:: liquid

   {{ incentives | group_by: "amount" }}

|hr|

sort
....

Sort an array. Optional arguments for hashes: 1. property name 2. nils order (first or last).

.. code-block:: liquid

   {{ campaign_tags | sort }}
   {{ incentives | sort: "amount" }}
   {{ incentives | sort: "amount", "first" }}

|hr|

where
.....

Select all the objects in an array where the key has the given value.

.. code-block:: liquid

   {{ incentives | where: "amount", 10 }}

|hr|

localize
........

Returns a localized version of string from campaign localization.
Has optional argument that specifies a default value if campaign has no defined localization yet.
Supports nested interpolation with `[[  ]]`

.. code-block:: liquid

   {{ "welcome_message" | localize }}
   {{ "offer_title" | localize: "Get [[incentives.referrer.description]]" }}

Supports fixed variants for localization, user will be able to set localization value only from this list.
First value will be a default value, or you can set it using ``default`` option.

.. code-block:: liquid

   {{ "campaign_layout" | localize: "left", "right" }}
   {{ "header_size" | localize: "h1", "h2", "h3", "h4", default: "h2" }}

There is also boolean localization type. It has a strict requirement: exactly two variants which
determines boolean logics. The first variant is associated with ``true``, the last one — ``false``.
The first variant is set as default unless you change it to otherwise with a ``default``
option (see above for an example). Here is an example of how to use boolean localization:

.. code-block:: liquid

   {% assign responsive_font = 'fonts_size' | localize: 'Responsive', 'Fixed', trait: 'boolean' %}
   {% if responsive_font %}
     Responsive
   {% else %}
     Fixed
   {% endif %}

For more information see :ref:`Localization <campaigns/localization>` page.

|hr|

scale\_color
............

Returns a new adjusted color with scaled attributes.
Available attributes: `red`, `green`, `blue`, `saturation`, `lightness`, `alpha`

.. code-block:: text

   {{ "black" | scale_color: lightness: 50 }}
   {{ "rgb(256, 128, 0)" | scale_color: saturation: -10 }}

|hr|

adjust\_color
.............

Returns a new adjusted color based on the following attributes:

* `red` — changes only the Red color channel saturation. Allowed values: `-255`-`255`.
* `green` — changes only the Green color channel saturation. Allowed values: `-255`-`255`.
* `blue` — changes only the Blue color channel saturation. Allowed values: `-255`-`255`.
* `hue` — changes the hue of a color. Allowed values: `0`-`360`.
* `saturation` — changes the saturation of a color. Allowed values: `-100`-`100`.
* `lightness` — changes the lightness of a color. Allowed values: `-100`-`100`.
* `alpha` — changes the opacity of a color. Allowed values: `-1`-`1`.

.. code-block:: liquid

   {{ "red" | adjust_color: blue: 255 }}
   {{ "#000000" | adjust_color: alpha: -0.5 }}

|hr|

leaderboard
...........

Returns array of top advocates for Leaderboard campaigns.
Parameter can be number from 1 to 100 or 'advocate'.

If parameter is 'advocate' it will return rank info for current advocate.

It returns objects with next fields:

* ``leaderboard_rank`` - Advocate rank
* ``leaderboard_count`` - Number of approved referrals for specified period
* ``leaderboard_subtotal`` - Sum of advocate purchase subtotals for specified period
* also all fields from :ref:`advocate_info <editor_variables_advocate_info>` variable

.. code-block:: liquid

   {% assign leaders = "3" | leaderboard %}
   {% for leader in leaders %}
      <td>{{ leader.leaderboard_rank }}</td>
      <td>{{ leader.leaderboard_count }}</td>
   {% endfor %}

.. code-block:: liquid

   {% assign leader = "advocate" | leaderboard %}
   {{ leader.email }} - {{ leader.leaderboard_count }} - {{ leader.leaderboard_rank }}

|hr|

url2png
.......

Captures a snapshot of a website URL you pass to it. In case you need to
embed a snapshot of your website into Talkable campaign it is way better
to use this liquid filter instead of embedding an iframe since an image
is always lighter in size and takes less CPU performance to render on
a screen. Also, some websites restrict themselves from embedding through
an iframe so you can take ``url2png`` as a bulletproof solution for a
website snapshot.

Available options:

* ``ttl`` - "time to live" period for a screenshot before it gets refreshed, in seconds. Value example: ``86400``.
* ``viewport`` - Viewport dimensions. Value example: ``"640x480"``.
* ``custom_css_url`` - Custom CSS file that will be injected into a website in case you need to change a screenshot. Value example: ``"http://url2png.com/tests/css/test.css"``.
* ``fullpage`` - Attempts to capture entire document canvas. Value example: ``true``.

Here is how you can embed a screenshot of your website into a campaign view (``site_url`` returns your website URL that you set inside Site Settings):

.. code-block:: liquid

   <img src="{{ site_url | url2png }}" class="campaign-site-on-the-back" />

Refresh the screenshot every week:

.. code-block:: liquid

   <img src="{{ 'www.example.com' | url2png: ttl: 604800 }}" />

|hr|

barcode
.......

Represents any ``string`` as an array of boolean values: ``[true, false]`` in order to convert it into a barcode.
This filter strictly follows GS1-128 specification: https://en.wikipedia.org/wiki/GS1-128.

.. code-block:: liquid

   {% assign barcode = "X" | barcode %}

**Here is an example how to convert a coupon code into a barcode:**

HTML:

.. code-block:: liquid

   <table cellspacing="0" cellpadding="0" border="0">
     {% assign barcode = coupon_code | barcode %}
       <tr>
         {% for bar in barcode %}
           <!-- bar suppose to be true or false -->
           <td class="barcode-line is-{{ bar }}"></td>
         {% endfor %}
       </tr>
   </table>

SCSS:

.. code-block:: scss

   .barcode-line {
     height: 50px;
     width: 2px;
     &.is-true {
       background-color: black;
     }
   }

.. _Standard liquid filters: https://github.com/Shopify/liquid/wiki/Liquid-for-Designers#standard-filters

|hr|

barcode\_image
..............

Represents any ``string`` as barcode image in png.
This filter strictly follows GS1-128 specification: https://en.wikipedia.org/wiki/GS1-128.

It may take the following arguments: ``height``, ``xdim`` (thickness of the thinnest line), ``margin`` and ``bg_transparent``.

Default values are ``100`` for ``height``,  ``1`` for ``xdim``, ``0`` for ``margin`` and ``false`` for ``bg_transparent``.

The values are in pixels.

.. code-block:: liquid

   {{ coupon.code | barcode_image }}
   {{ coupon.code | barcode_image: height: 200 }}
   {{ coupon.code | barcode_image: xdim: 3 }}
   {{ coupon.code | barcode_image: height: 200, xdim: 3 }}
   {{ coupon.code | barcode_image: height: 200, xdim: 3, margin: 5 }}
   {{ coupon.code | barcode_image: height: 200, xdim: 3, margin: 5, bg_transparent: true }}

Returns a URL string.

|hr|

base64\_encode
..............

Converts given string into a base64 encoded string.

.. code-block:: text

   {{ "some string" | base64_encode }}

Returns ``c29tZSBzdHJpbmc=``

|hr|

base64\_decode
..............

Decodes given base64 encoded string.

.. code-block:: liquid

   {{ "c29tZSBzdHJpbmc=" | base64_decode }}

Returns ``some string``

|hr|

values
......

Takes a hash and returns the array of its values.

.. code-block:: liquid

   {% assign incentive_configs = incentives | values %}

Returns ``[{ad incentive config}, {fr incentive config}]``

|hr|

async\_rendering
................

Stores Liquid partial that can be later rendered via ``Talkable.loadLiquid`` function.

Example 1
~~~~~~~~~

Liquid

.. code-block:: liquid

  {{ "async_advocate_info" | async_rendering: 'template for rendering with data [[ advocate_info.email ]]' }}

JavaScript API call

.. code-block:: javascript

  Talkable.loadLiquid("async_advocate_info", function(rendered_template) {
    console.log(rendered_template);
  });

Rendered Liquid

.. code-block:: text

  "template for rendering with data advocate@example.com"

Example 2
~~~~~~~~~

Liquid

.. code-block:: liquid

  {{ 'async_dashboard_data' | async_rendering: some_key: "[[ dashboard.possible_rewards | money: strip_insignificant_zeros: true ]]", other_key: "[[ friend_info.purchases_count ]]" }}

JavaScript API call

.. code-block:: javascript

  Talkable.loadLiquid("async_dashboard_data", function(rendered_data) {
    console.log(rendered_data.some_key);
  });

Rendered Liquid

.. code-block:: text

  "$420"

Example 3
~~~~~~~~~

Liquid

.. code-block:: liquid

  {% capture some_liquid_block %}
  {% raw %}
  Whatever Liquid you would like to have
  {% endraw %}
  {% endcapture %}
  {{ 'async_liquid_reference' | async_rendering: some_liquid_block }}

JavaScript API call

.. code-block:: javascript

  Talkable.loadLiquid("async_liquid_reference", function(rendered_template) {
    console.log(rendered_template);
  });

Rendered Liquid

.. code-block:: text

  "Whatever Liquid you would like to have"

Example 4
~~~~~~~~~

Use ``json`` Liquid filter to transform deeply nested object structure into a valid JSON.

Liquid

.. code-block:: liquid

  {{ 'async_advocate_info' | async_rendering: '[[ advocate_info | json ]]' }}

JavaScript API call

.. code-block:: javascript

  Talkable.loadLiquid("async_advocate_info", function(rendered_template) {
    console.log(JSON.parse(rendered_template));
  });

Rendered Liquid

.. code-block:: javascript

  {
    "first_name": null,
    "last_name": null,
    "email": "advocate@example.com",
    "username": null,
    "external_customer_id": null,
    "opted_in_at": null,
    "sub_choice": false,
    "purchases_sum": 0.0,
    "purchases_count": 0,
    "events_count": 0,
    "events_count_by_category": {
      "friend_signup": 0,
      "purchase": 0
    },
    "referrals_count": 0,
    "referred_by": null,
    "custom_properties": {},
    "unsubscribed": false
  }

|hr|

events\_collection
..................

Collection of person’s events from the certain date (or for all time when ``from_time`` is not set).

.. code-block:: liquid

   {{ "purchase" | events_collection: from_time: "10/14/2018" }}

Returns

.. code-block:: javascript

  [
    {
      "coupon_codes": ["OFF5"],
      "created_at": "2019-05-22T15:53:41-07:00",
      "email": "ad@site.com",
      "order_number": 98237519,
      "subtotal": 100.0
    },
    {
      "coupon_codes": ["OFF5"],
      "created_at": "2019-05-22T15:53:41-07:00",
      "email": "ad@site.com",
      "order_number": 98237520,
      "subtotal": 200.0
    }
  ]

|hr|

rybbon
......

Takes a campaign key of a Rybbon Talkable campaign.
Makes a claim request within the scope of the given campaign and returns a gift claim link.
Requires Rybbon Access Key set up in Site Settings in order to work.

.. code-block:: liquid

   {{ "a9a3472f4ea858758e0cd686de8408e2" | rybbon }}

Returns ``https://www.rybbon.net/redeem.php?claimcode=ee645de47765bdbede751c8c6f08a619``

Accepts custom amount of reward for Rybbon campaigns with variable denomination. The minimum amount conforms to each specific Rybbon gift card restrictions. The maximum amount is 50.

.. code-block:: liquid

   {{ "a9a3472f4ea858758e0cd686de8408e2" | rybbon: amount: 13.5 }}

|hr|

tremendous
..........

Takes a campaign key of a Tremendous campaign.
Makes a claim request within the scope of the given campaign and returns a gift claim link.
Requires Tremendous Access Token set up in Site Settings in order to work.
Implies that there is only one funding source in the Tremendous account.

.. code-block:: liquid

   {{ "DEM8ULSSATK0" | tremendous }}

Returns ``https://www.tremendous.com/rewards/payout/reward123``
