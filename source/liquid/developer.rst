.. _liquid/developer:
.. include:: /partials/common.rst
.. _Liquid: http://github.com/Shopify/liquid

Campaign Developer Guide
========================

Curebit Campaign is based on interaction between ``Advocate`` and ``Friend``:

- Advocate: person, who shares an offer with his Friend(s)
- Friend: person, who is invited to participate in Campaign by Advocate

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

.. _developer/advocate signup page:

Advocate Signup Page
--------------------

Advocate referral program sign up page (only for Standalone Campaign). On this page Advocate signs up by
entering his email address.
|br|
|br|

.. image:: /_static/img/basics/advocate-signup.png
  :alt: Advocate signup

.. raw:: html

  <h4>Default template markup:</h4>

.. code-block:: html

  <form accept-charset="UTF-8" action="{{ create_affiliate_member_path }}" method="post">
    <input type="email" name="affiliate_member[email]" placeholder="Your Email Address" required />
    <input type="submit" value="Sign up" data-disable-with="Please wait" name="commit" />
  </form>

.. note:: Do not change ``name`` and form ``action`` attributes, otherwise functionality won't work.

|hr|

.. _developer/advocate share page:

Advocate Share Page
-------------------

Here Advocate shares an offer with his friends. Explain the value proposition
to Advocate and Friend, that both will receive an exclusive discount.

Available sharing methods:

- Email sharing
- Social sharing (Facebook, Twitter, LinkedIn)
- Link sharing (direct link to the Friend Claim Page)

|br|
|br|

.. image:: /_static/img/basics/advocate-offer-page.png
  :alt: Advocate Share Page

|br|

.. raw:: html

  <h4>Email sharing example:</h4>

.. code-block:: html

  <form action="#" class="js-share-via-email-form">
    <input type="text" value="" name="email_recipient_list" />
    <input type="text" value="" name="email_subject" />
    <textarea name="share_message"></textarea>
    <input type="checkbox" checked="checked" name="share_email_reminder" value="true" />
    <input type="submit" value="Send email" />
  </form>

.. _developer/friend share email reminder checkbox:

Note ``share_email_reminder`` checkbox — this is :ref:`developer/friend share email reminder`
trigger.

|br|

.. raw:: html

  <h4>Facebook sharing example:</h4>

.. code-block:: html

  <a href="#" class="js-share-offer-via-facebook">
    Share on Facebook
  </a>

|br|

.. raw:: html

  <h4>Twitter sharing example:</h4>

.. code-block:: html

  <a href="{{ twitter_share_link }}">
    Share on Twitter
  </a>

|br|

.. raw:: html

  <h4>Share by link example:</h4>

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

.. note:: Do not change ``name`` and ``class`` attributes, otherwise
  functionality won't work. `js-` class prefix means it is used in Curebit API.

Related tutorials for this view:

- :ref:`tutorials/instant reward`
- :ref:`tutorials/cloudsponge`
- :ref:`tutorials/multiple email fields`
- :ref:`tutorials/linkedin`

|hr|

.. _developer/advocate offer email:

Advocate Offer Email
--------------------

This email is sent to Advocate on sign up. Explain the value proposition
and encourage Advocate to share using the buttons.

- For Standalone Campaign it triggers when Advocate signs up.
- For Post-Checkout Campaign it triggers when Advocate makes store purchase.
  It is not recommended to use this email here since it may look spammy.

Main CTA should point to an Advocate Share Page — ``{{ share_page_url }}``.

|br|

.. image:: /_static/img/basics/advocate-offer-email.png

.. include:: /partials/developer_email_note.rst

|hr|

.. _developer/friend share email:

Friend Share Email
------------------

This email is sent by Advocate to his Friends from the
:ref:`developer/advocate share page`. |br|
The main purpose of this email is to invite a Friend by showing a personal
Share Message from Advocate along with a unique Friend Claim Page link. Some
information about offer itself is recommended.

Frequently used Variables:

- Main CTA should point to a :ref:`developer/friend claim page` — ``{{ short_url }}``.
- To show Email Share Message from Advocate use ``{{ custom_message_body }}``.

|br|

.. image:: /_static/img/basics/friend-share-email.png
   :alt: Friend Share Email

.. include:: /partials/developer_email_note.rst

|hr|

.. _developer/friend share email reminder:

Friend Share Email Reminder
---------------------------

This email is triggered only if Friend Share Email Reminder checkbox was checked
on the :ref:`developer/advocate share page` when sharing. |br|
By default reminder email sends out in 72 hours after sharing if Friend didn't
use his Offer (i.e. didn't make a store purchase using coupon code).

Main CTA should point to a Friend Claim Page — ``{{ short_url }}``. |br|
To change email trigger delay open ``Editor`` / ``Extra fields`` for the
particular email.

|br|

.. image:: /_static/img/basics/friend-share-email-reminder.png
   :alt: Friend Share Email Reminder

.. include:: /partials/developer_email_note.rst

|hr|

.. _developer/friend claim page:

Friend Claim Page
-----------------

Friend lands here from :ref:`developer/friend share email`. |br|
Explain him what special discount he will get when using this link. |br|
It's recommended to show coupon code for the Friend on this page
(and only on this page).

Frequently used Variables:

- Main CTA should point to a merchant site to start shopping
  ``{{ proceed_to_merchant_path }}``. |br|
- To show coupon code use ``{{ coupon_code }}``.
- To show expiration date use ``{{ valid_until }}``.
  :ref:`Formatting options <liquid_filter_format_date>`.

|br|

.. image:: /_static/img/basics/friend-claim-page.png
   :alt: Friend Claim Page

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

