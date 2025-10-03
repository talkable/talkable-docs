.. _campaigns/localization:
.. include:: partials/common.rst

.. meta::
   :description: You can localize your referral campaign. Use the same template with different localization.

Localization
############

Each template can be localized.
Localization is not a part of the view template. Default Talkable campaigns are comming with localization now. It is stored in campaign allowing multiple campaign to use same template with different localization and ability to edit Copy of a campaign outside of liquid editor (making interface significantly easier for marketer).

Campaign localization is done using a liquid filter `localize`:

.. code-block:: liquid

    {{ "offer_title" | localize: 'Get [[incentives.referrer.description]]' }}

You can add this filter in the Campaign Editor section under HTML & CSS, and it will appear in the Copy tab:

.. image:: /_static/img/campaign-localization.png

Any campaign that uses view with `localize` call have this data appeared.
Now you are able to change the default value to something else like `Obten {{incentives.referrer.description}}` (Spanish)

Campaign Localization is copied when campaign is copied, so you are able to use the following flow:

1. Create Campaign
2. Build templates with localization support
3. Make a copy of the campaign
4. Translate localization in a copy to different language.

Campaigns with phone input have country automatically detected based on user IP:

.. image:: /_static/img/phone-input.png
