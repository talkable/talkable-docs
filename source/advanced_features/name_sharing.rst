.. _advanced_features/name_sharing:
.. include:: /partials/common.rst

.. meta::
   :description: Talkable allows the Advocates to share referral offers by their names.

Name Sharing
============

There is a way to enable sharing referral offers by the |Advocate| name.

Name Sharing User Flow
----------------------

For users, the name sharing would proceed as follows:

1. The Advocate opens the referral offer share page.

2. The Advocate opts to share the offer by their personal name.

3. The Advocate confirms or edits their personal name [#f1]_.

4. The Advocate tells their personal name to their Friends in any way they find suitable.

5. The Friend visits site and opens the Claim by Name widget.

6. The Friend enters their email and the Advocate's name.

7. The Friend receives a Click Reward (if it was configured in the Advocate campaign).

----

.. [#f1] To be a valid personal name or code-word, it must be unique, between 3 and 50 characters
   in length, and can contain Latin letters, numbers, underscores as separators, or even spaces.
   It should not start with a number.

.. _advanced_features/name_sharing_setup:

Name Sharing Setup
------------------

To make name sharing work, at least two referral campaigns are required:

* one for |Advocate| (it can be any campaign that has a share page)
* one for |Friend| - a :ref:`Claim by Name campaign <campaigns/claim_by_name>`.

Personal name sharing channel is available as a configuration localization on Advocate share page
in all new campaign templates. It should be enabled so that the Advocate can enter/edit their name on a share page.

If you don't have the localization in your campaign code, you can add it manually in the HTML & CSS editor mode.

.. code-block:: liquid

  {% assign advocate_share_page_channel_personal_name = "advocate_share_page_channel_personal_name" | localize: trait: "boolean", default: "Disabled" %}

There can be multiple Advocate campaigns, as well as multiple Friend campaigns.
Upon a reward claim by a Friend, the newest offer from the respective Advocate will be matched.

.. important::
  Make sure to set up both advocate and friend incentives in the Advocate campaign. The Claim by Name campaign
  does not hold any incentive configuration and only serves to show a claim widget.

.. note::
  All advocate and friend metrics are counted toward the Advocate campaign.

Inline Widget
-------------

The Claim by Name campaign does not hold any incentive configuration and only serves to show a claim widget. There can be multiple campaigns with
the different offers and only one Claim by Name campaign, which will serve all these campaigns.

In the rules of the Claim by Name campaign there is an option to make the floating widget inline. This can be done in the Rules of the campaign:

.. image:: /_static/img/advanced_features/name_sharing_inline_widget_1.png
  :alt: Inline widget option

After that the campaign will be embedded in the page:

.. image:: /_static/img/advanced_features/name_sharing_inline_widget_2.png
  :alt: Inline widget

Once you enabled “Inline Widget”, ask client to add the following code for the inline campaign (container):

.. code-block:: html

  <div id=’talkable-claim-by-name’></div>

Without adding this code, the campaign won’t be visible.

Shopify Fast Checkout
---------------------

If Shopify theme uses shopping cart as a dynamic widget, you can integrate Claim by name campaign to show it in the cart by following these steps:

* Change placement rule to show campaign everywhere

* Enable option 'Inline Widget' in Campaign settings

* Add the following code to the Cart snippet in the Shopify theme (``Snippets/card.liquid``):

.. code-block:: html

  <div id=’talkable-claim-by-name’></div>

Interactions with the personal name-share link
----------------------------------------------

When Advocate creates a username, his personal name link gets updated as well, and vice versa.
However, the old personal name links that he shared before this change will still be valid.
