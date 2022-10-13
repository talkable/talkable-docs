.. _campaigns/views/offers_show:
.. include:: /partials/common.rst

.. meta::
   :description: Advocate Signup/Share Page - Combination of Signup and Share forms. Shows the value proposition to Advocate and Friend — they both will receive an exclusive discount.

.. _advocate_signup_share_page_view:

Advocate Signup/Share Page
--------------------------

Combining the Signup and Share page brings a smoother experience to our customers.

First we show Advocate Signup Form. Signup is skipped when we know the advocate or Email gating for advocate is disabled (by default - enabled).
On this page Advocate signs up by entering their email address and phone number(optional).

.. image:: /_static/img/basics/advocate-signup-form.png
   :alt: Advocate Signup Form

After signup, without reloading page, Advocate Share form is shown:

.. image:: /_static/img/basics/advocate-share-form.png
   :alt: Advocate Share form

Here |advocate| shares an offer with their |friend|\s. Explain the value proposition
to |advocate| and |friend|, that both will receive an exclusive discount.

Available sharing methods:

- Email sharing
- Social sharing (Facebook, Twitter, LinkedIn)
- Link sharing (direct link to the Friend Claim Page)

.. raw:: html

   <h4>Email sharing example:</h4>

|br|

.. image:: /_static/img/basics/advocate-share-via-email.png
   :alt: Advocate Share via Email Form

Note ``Send my friend a reminder e-mail in 3 days`` checkbox — this is :ref:`friend_share_email_reminder_view`
trigger.

.. raw:: html

   <h4>Facebook sharing example (simplified):</h4>

.. code-block:: html

   <a href="#" class="js-share-offer-via-facebook">
     Share on Facebook
   </a>

.. raw:: html

   <h4>Twitter sharing example (simplified):</h4>

.. code-block:: html

   <a href="{{ twitter_share_link }}">
     Share on Twitter
   </a>

.. raw:: html

   <h4>Share by link example (simplified):</h4>

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

.. note::

   Do not change ``name`` and ``class`` attributes, otherwise
   functionality won’t work. `js-` class prefix means it is used in Talkable API.

Related tutorials for this View:

- :ref:`tutorials_instant_reward`
- :ref:`tutorials_cloudsponge`
- :ref:`tutorials_multiple_email_fields`
- :ref:`tutorials_linkedin`
