.. _liquid/developer:
.. include:: /partials/common.rst
.. _Liquid: http://github.com/Shopify/liquid

Campaign Developer Guide
========================

Curebit Campaign is based on interaction between ``Advocate`` and ``Friend``:

- ``Advocate``: person, who shares an offer with his Friend(s)
- ``Friend``: person, who is invited to participate in Campaign by Advocate

.. image:: /_static/img/basics/sharing-process.png
  :alt: Sharing process

Each step of this interaction has its own ``View`` so developer can easily
change every singe step and customize its appearance and functionality based on
campaign requirements.

We use `Liquid`_ as a View template engine to provide a simple and quick way
to change campaign functionality and appearance.
|br| This choice was made mainly because of developers who are already
familiar with Liquid templating in Shopify.

To start editing Views simple visit ``Editor`` page from the Campaign dashboard.

|hr|

Advocate Signup Page
--------------------

Advocate referral program sign up page (only for ``Standalone Campaign``). On this page Advocate signs up by
entering his email address.
|br|
|br|

.. image:: /_static/img/basics/advocate-signup.png
  :alt: Advocate signup

Default template markup:

.. code-block:: html

  <form accept-charset="UTF-8" action="{{ create_affiliate_member_path }}" method="post">
    <input type="email" name="affiliate_member[email]" placeholder="Your Email Address" required />
    <input type="submit" value="Sign up" data-disable-with="Please wait" name="commit" />
  </form>

.. note:: do not change ``name`` and form ``action`` attributes, otherwise functionality won't work.

|hr|

Advocate Offer Page
-------------------

Here Advocate shares an offer with his friends. Explain the value proposition
to Advocate and Friend, that both will receive an exclusive discount.

Available share methods:

- Email sharing
- Social sharing (Facebook, Twitter, LinkedIn)
- Link sharing (direct link to the ``Friend Claim Page``)

|br|
|br|

.. image:: /_static/img/basics/advocate-offer-page.png
  :alt: Advocate offer page


|hr|

|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
|br|
Campaign Editor allows you to edit Liquid templates of various Web and Email
views, which are shown and sent for campaign visitors.

It also supports alternative templates: mobile for Web views and plain text for
Email.

CSS is editable and supports Liquid and SCSS.

.. note::

  There are two CSS stylesheets: for Web and Emails, shared between
  corresponding views.

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

