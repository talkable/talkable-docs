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

.. [#f1] A personal name should be unique within a site and be 3 to 50 symbols long.
   It can only contain latin letters, and numbers.
   A personal name cannot begin with a number.

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
