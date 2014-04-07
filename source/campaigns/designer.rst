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
tablets. Since Curebit integration is based on ``iframe`` it is not
possible to change its size from within of the iframe that’s why Signup
and Share pages should always be of the same size.

For Post-purchase campaign Advocate Share Page should look like a modal window
cause it integrates right to the checkout page after user makes a
purchase (most common size is 800x500px):

.. image:: /_static/img/liquid/designer/image2.png
   :alt: Advocate Share Page like a modal

.. note::
   Overlay cannot be customized.

Friend Claim Page size does not matter cause it hosts on Curebit site
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
