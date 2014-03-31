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

.. note:: Do not change ``name`` and form ``action`` attributes, otherwise functionality won't work.

|hr|

Advocate Offer Page
-------------------

Here Advocate shares an offer with his friends. Explain the value proposition
to Advocate and Friend, that both will receive an exclusive discount.

Available sharing methods:

- Email sharing
- Social sharing (Facebook, Twitter, LinkedIn)
- Link sharing (direct link to the ``Friend Claim Page``)

|br|
|br|

.. image:: /_static/img/basics/advocate-offer-page.png
  :alt: Advocate offer page

|br|

.. raw:: html

  <h3>Email sharing example:</h3>

.. code-block:: html

  <form action="#" class="js-share-via-email-form">
    <input type="text" value="" name="email_recipient_list" />
    <input type="text" value="" name="email_subject" />
    <textarea name="share_message"></textarea>
    <input type="checkbox" checked="checked" name="share_email_reminder" value="true" />
    <input type="submit" value="Send email" />
  </form>

|br|

.. raw:: html

  <h3>Facebook sharing example:</h3>

.. code-block:: html

  <a href="#" class="js-share-offer-via-facebook">
    Share on Facebook
  </a>

|br|

.. raw:: html

  <h3>Twitter sharing example:</h3>

.. code-block:: html

  <a href="{{ twitter_share_link }}">
    Share on Twitter
  </a>

|br|

.. raw:: html

  <h3>Share by link example:</h3>

.. code-block:: html

  <div data-clipboard-text="{{ short_url }}"
       data-copied-label="Copied!"
       data-placement="top"
       title="Click to Copy"
       class="js-share-by-link">
    Copy and share by link
  </div>

- ``data-clipboard-text`` — data to be copied to a user clipboard on click.
- ``data-copied-label`` — tooltip text after copying.
- ``data-placement`` — tooltip placement. Possible values: ``top``, ``right``, ``bottom``, ``left``.
- ``title`` — tooltip text on hover.

.. note:: Do not change ``name`` and ``class`` attributes, otherwise functionality won't work. `js-` class prefix means it is used in Curebit API.

|hr|

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

