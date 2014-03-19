.. _liquid/standard:
.. include:: /partials/common.rst

Designer guide
==============

Web view size
~~~~~~~~~~~~~

Make sure signup page canvas size is equal to the offer page, because
this is a next screen referrer sees right after, there should be a
smooth transition between these pages. Canvas size should be equal to a
main container width of your site:

.. figure:: /_static/img/liquid/designer/figure1.png
   :alt: Page canvas size

For mobile screens most common width is 320px, but we also support fluid
width with possibility to set it to 100% to support mobile devices and
tablets. Since Curebit integration is based on ``iframe`` it is not
possible to change its size from within of the iframe that’s why signup
and offer pages should always be of the same size.

For Post-purchase campaign offer page should look like a modal window
cause it integrates right to the checkout page after user makes a
purchase (most common size is 800x500px):

.. figure:: /_static/img/liquid/designer/figure2.png
   :alt: Offer page like a modal

.. note::
   Overlay cannot be customized.

Landing page size does not matter cause it hosts on Curebit site
entirely. Commonly this view looks like a modal window with customer
site loaded on the back:

.. figure:: /_static/img/liquid/designer/figure3.png
   :alt: Landing page

Most common modal size is 800x500px.

Email size
~~~~~~~~~~

Ideally email width is 580px for content:

.. figure:: /_static/img/liquid/designer/figure4.png
   :alt: Email size

Fonts
~~~~~

Using custom fonts as text allowed only for web views, **not emails**.
This is email clients restriction. If its needed, we can convert custom
font to images but it will not be editable through campaign editor and
each copy change will require more time. Here is a list of OS default
fonts http://www.ampsoft.net/webdesign-l/WindowsMacFonts.html

Also, for emails copy should be placed always on top of solid background
color, not image:

.. figure:: /_static/img/liquid/designer/figure5.png
   :alt: Solid color VS image

There are many options for embedding custom fonts, here are most popular
and solid ones:

1. Purchase web-compatible font on http://myfonts.com

.. figure:: /_static/img/liquid/designer/figure6.png
   :alt: myfonts.com

2. Purchase on http://typekit.com

3. Choose free Google Font http://www.google.com/fonts
