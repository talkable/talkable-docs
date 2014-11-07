.. _campaigns/views/offers_show:
.. include:: /partials/common.rst

.. _advocate_share_page_view:

Advocate Share Page
-------------------

Here |advocate| shares an offer with his |friend|\s. Explain the value proposition
to |advocate| and |friend|, that both will receive an exclusive discount.

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

..

Note ``share_email_reminder`` checkbox — this is :ref:`friend_share_email_reminder_view`
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

.. note::

   Do not change ``name`` and ``class`` attributes, otherwise
   functionality won't work. `js-` class prefix means it is used in Talkable API.

Related tutorials for this View:

- :ref:`tutorials_instant_reward`
- :ref:`tutorials_cloudsponge`
- :ref:`tutorials_multiple_email_fields`
- :ref:`tutorials_linkedin`
