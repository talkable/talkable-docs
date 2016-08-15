.. _optional/converting_into_localization:
.. include:: /partials/common.rst

Converting Static Copy Into Localization
========================================

If you don't know what is Localization inside Talkable :ref:`read this article <campaigns/localization>`.

Few benefits you get out of using Localizations:

  1. It is extremely easy to set up an AB test if your copy is coded up as a Localizatio
  2. For non-technical people it is easier to change the copy inside Localization Editor because they are afraid to code.

1. Visit Campaign Editor:

.. image:: /_static/img/optional/campaign_navigation.png

2. Swith to HTML & CSS editor:

.. image:: /_static/img/optional/campaign_navigation_html_css_editor.png

3. Find a View you would like to convert a static copy at:

.. image:: /_static/img/optional/campaign_view_navigation.png

4. Find a copy that you'd like to convert into a Localization. You can hit `Cmd+F` (`Ctrl+F` on Windows) to search within HTML area.

Static copy is basically a piece of text that sits inside HTML & CSS Editor and usually looks like this:

.. code-block:: html

  <h1>
    Get {{ advocate_incentive.description }}.
  </h1>

A piece that we are going to extract into Localizations is just a copy, without HTML tags. To do that, simply wrap the text into a variable notation like so:

.. code-block:: javascript

  <h1>
    {{ "headline" | localize: "Get [[ advocate_incentive.description ]]." }}
  </h1>

5. Go back to Editor to see newly created Localization:

.. image:: /_static/img/optional/campaign_localization_sidebar.png


Few important things to remember
--------------------------------

  1. Don't forget to change `{{` into `[[` inside interpolation variables, otherwise variables will lose its function and become just a plain text.
  2. Keep in mind that `identifier` ("headline" in the example above) is a campaign-level Localization in fact, always remember to provide unique names for them, otherwise you will be overriding a value of one Localization.

.. warning::

   Talkable does not allow coding up Localizations within CSS area. If you want to move some CSS property into localizations use inline <style> tag inside HTML area.

.. container:: hidden

   .. toctree::

