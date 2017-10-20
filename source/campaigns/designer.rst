.. _campaigns/designer:
.. include:: /partials/common.rst

Designer
========

Web view size
-------------

Make sure Advocate Signup Page canvas size is equal to the Advocate Share Page, because
this is a next screen referrer sees right after, there should be a
smooth transition between these pages. Canvas size should be equal to a
main container width of your site:

.. image:: /_static/img/liquid/designer/image1.png
   :alt: Page canvas size

For mobile screens most common width is 320px, but we also support fluid
width with possibility to set it to 100% to support mobile devices and
tablets. Since Talkable integration is based on ``iframe`` it is not
possible to change its size from within of the iframe that’s why Signup
and Share pages should always be of the same size.

For Post-purchase campaign Advocate Share Page should look like a modal window
cause it integrates right to the checkout page after user makes a
purchase (most common size is 800x500px):

.. image:: /_static/img/liquid/designer/image2.png
   :alt: Advocate Share Page like a modal

.. note:: Overlay cannot be customized.

Friend Claim Page size does not matter cause it hosts on Talkable site
entirely. Commonly this view looks like a modal window with customer
site loaded on the back:

.. image:: /_static/img/liquid/designer/image3.png
   :alt: Friend Claim Page

Most common modal size is 800x500px.

.. _designer/email:

Email size
----------

Ideally email width is 480px for content:

.. image:: /_static/img/liquid/designer/email-width.png
   :alt: Email size

Fonts
-----

Using custom fonts as text allowed only for web views, **not emails**.
This is email clients restriction. If its needed, we can convert custom
font to images but it will not be editable through campaign editor and
each copy change will require more time. Here is a list of OS default
fonts http://www.ampsoft.net/webdesign-l/WindowsMacFonts.html

Also, for emails copy should be placed always on top of solid background
color, not image:

.. image:: /_static/img/liquid/designer/image5.png
   :alt: Solid color VS image

There are many options for embedding custom fonts, here are most popular
and solid ones:

1. Purchase web-compatible font on http://myfonts.com

.. image:: /_static/img/liquid/designer/image6.png
   :alt: myfonts.com

2. Purchase on http://typekit.com

3. Choose free Google Font http://www.google.com/fonts

.. _responsive-views:

Responsive view’s height
------------------------

Talkable campaigns can be integrated as a popup with overlay, or as an inline
block that sits somewhere in the middle between site header and footer. When
Talkable Campaign looks like a popup with overlay its size if always fixed to 100%
width and 100% height, it basically takes the entire screen and its size never gets
changed when a user resizes browser window (overlay will still take the entire screen size).

However, when Talkable Campaign is placed inline inside content area its size
depends on its internal content. The more content it holds the more higher it is.
Iframe has a known issue due to which browsers don’t change its height no matter how
much content it holds inside. By default all browsers set 150px height to all iframe
tags and add scrollbars if the internal content exceeds that size. Talkable Campaigns
are always of the correct size because of "Responsive iframe height" feature always
being enabled for such cases. No matter how much content Talkable iframe holds its
size will always be correct in order to look as expected without scrollbars. For this
reason, you might notice Talkable adds ``overflow: hidden;`` to the BODY tag — this CSS
property hides the scrollbars. At the same time, Talkable JS integration library always
ensures its height is correct by checking the size of the iframe content and setting it
in pixels to the Talkable iframe tag that holds it from the outside.

You are able to turn "Responsive iframe’s height" ON/OFF from within
``Campaign / Editor / Edit HTML & CSS / Extra / Responsive iframe’s height`` select box.
