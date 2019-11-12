.. _campaigns/views/offers_claim:
.. include:: /partials/common.rst

.. meta::
   :description: Tell a Friend that every link they share will be rewarded.

.. _friend_claim_page_view:

Friend Claim Page
-----------------

|friend| lands here from :ref:`friend_share_email_view`. |br|
Explain him what special discount he will get when using this link. |br|
It’s recommended to show coupon code for the |friend| on this page
(and only on this page).

Frequently used Variables:

- Main |cta| should point to a merchant site to start shopping
  ``{{ proceed_to_merchant_path }}``. |br|
- To show coupon code use ``{{ coupon_code }}``.
- To show expiration date use ``{{ valid_until }}``.
  :ref:`Formatting options <liquid_filter_format_date>`.

|br|

.. image:: /_static/img/basics/friend-claim-page.png
   :alt: Friend Claim Page

.. code-block:: liquid

   {% if offer_active %}
     Copy your code: {{ coupon_code }}
     <a href="{{ proceed_to_merchant_path }}">Shop now</a>
     Offer is valid until {{ friend_offer.valid_until | format_date }}.
   {% else %}
     Offer expired.
     <a href="{{ proceed_to_merchant_path }}">Proceed without offer</a>
   {% endif %}

.. note::

   Do not change ``name`` and ``class`` attributes, otherwise
   functionality won’t work. `js-` class prefix means it is used in Talkable API.

Related tutorials for this View:

- :ref:`tutorials_email_gating`
- :ref:`tutorials_like_gating`
- :ref:`tutorials_zeroclipboard`
