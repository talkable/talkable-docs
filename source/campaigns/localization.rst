.. _campaigns/localization:
.. include:: /partials/common.rst

Localization
############

Each template can be localized.
Localization is not a part of the view template. It is stored in campaign allowing multiple campaign to use same template with different locazation.

Campaign localization is done using a liquid filter `localize`:

.. code-block:: liquid

    {{ "offer_title" | localize: 'Get [[incentives.referrer.descrition]]' }}

After adding this filter call to the template, go to campaign page and click "Localization" from the navigation menu:

.. image:: /_static/img/campaign-localization.jpg

Any campaign that uses view with `localize` call have this data appeared.
Now you are able to change the default value to something else like `Obten [[incentives.referrer.descrition]]` (Spanish)

Campaign Localization is copied when campaign is copied, so you are able to use the following flow:

1. Create Campaign
2. Build templates with localization support
3. Make a copy of the compaign
4. Translate lozalization in a copy to different language.
