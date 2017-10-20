.. _advanced_features/converting_into_localization:
.. include:: /partials/common.rst

Converting Into Localization
============================

If you don’t know what is Localization inside Talkable :ref:`read this article <campaigns/localization>`.

Few benefits you get out of using Localizations:

  1. It is extremely easy to set up an AB test if your copy is coded up as a Localization.
  2. For non-technical people it is easier to change the copy inside Localization Editor because they are afraid to code.

1. Visit Campaign Editor:

.. image:: /_static/img/advanced_features/campaign_navigation.png

2. Swith to HTML & CSS editor:

.. image:: /_static/img/advanced_features/campaign_navigation_html_css_editor.png

3. Find a View you would like to convert a static copy at:

.. image:: /_static/img/advanced_features/campaign_view_navigation.png

4. Find a copy that you’d like to convert into a Localization. You can hit `Cmd+F` (`Ctrl+F` on Windows) to search within HTML area.

Static copy is basically a piece of text that sits inside HTML & CSS Editor and usually looks like this:

.. code-block:: html

  <h1>
    Get {{ advocate_incentive.description }}.
  </h1>

A piece that we are going to extract into Localizations is just a copy, without HTML tags. To do that, simply wrap the text into a variable notation like so:

.. code-block:: html

  <h1>
    {{ "advocate_share_page_headline" | localize: "Get [[ advocate_incentive.description ]]." }}
  </h1>

5. Go back to Editor to see newly created Localization:

.. image:: /_static/img/advanced_features/campaign_localization_sidebar.png

.. raw:: html

  <h2>Few important things to remember</h2>

1. Don’t forget to change `{{` into `[[` inside interpolation variables, otherwise variables will lose its function and become just a plain text.
2. Keep in mind that `identifier` ("advocate_share_page_headline" in the example above) is a campaign-level Localization in fact, always remember to provide unique names for them, otherwise you will be overriding a value of one Localization.

.. warning::

   Talkable does not allow coding up Localizations within CSS area. If you want to move some CSS property into localizations use inline <style> tag inside HTML area.

Moving Subject Line Into Localization
-------------------------------------

It is highly unlikely that your campaign is not equipped with Subject line as a Localization, by default all newly created campaigns at Talkable already have it. In case your campaign does not please keep reading this section.

Subject line is unique because its default value is set on the Advocate Share Page along with other email sharing fields (email body, reminder checkbox value), not Friend Share email as it might sounded logical. Here is the plan:

  1. Create Subject Line as a Localization on the Advocate Share Page, provide its default value, it will be used inside `value` attribute of the "subject" form field:

    .. image:: /_static/img/advanced_features/subject_line_setup_inside_share_page.png

    .. code-block:: html

      <input name="email_subject" type="text" class="textfield" value="{{ 'friend_share_email_subject' | localize: 'Your friend [[ advocate_info.first_name ]] [[ advocate_info.last_name ]] gave you [[ friend_incentive.description ]]' | replace: '   ', ' ' | replace: '  ', ' ' }}" />

    This code creates new Localization named "Friend share email subject" that you are able to change on the Advocate Share Page.

  2. Navigate to Friend Share email |rarr| Extra fields to see Email Subject field:

    .. image:: /_static/img/advanced_features/campaign_editor_subject.png

  3. Put the following code in there:

    .. code-block:: liquid

      {% if custom_message_subject == blank %}
        {{ 'friend_share_email_subject' | localize }}
      {% else %}
        {{ custom_message_subject }}
      {% endif %}

    The code snippet above checks if the Advocate provided any Subject at all. If not we take default Subject copy so Friend Share email does not come with a blank subject.

Color As Localization
---------------------

Another example would be localizing font color of a headline, all copy at once, or a background color of a button. You can use `color` trait of a Localization for that.

  1. Navigate to HTML & CSS editor of the View you want to add a color Localization on:

    .. image:: /_static/img/advanced_features/campaign_navigation_html_css_editor.png

  2. At the very bottom of the HTML area add ``<style></style>`` tag with CSS that will override default styling of the element you want to localize:

    .. code-block:: text

      .button {
        background-color: {{ "advocate_share_page_button_color" | localize: "#f94d08", trait: "color" }};
        border-color: {{ "advocate_share_page_button_color" | localize: "#f94d08", trait: "color" }};
      }

    In the code example above we created new Color Localization with default HEX color `#f94d08` which is used for `background-color` and `border-color` CSS properties of `.button` selector. Whenever you set a new color inside Campaign Editor it will be changed across both places because we’re using the same Localization identifier in both places.

  3. New Color Localization appears under "Color" tab inside Campaign Editor:

    .. image:: /_static/img/advanced_features/editor_colors_tab.png

Image As Localization
---------------------

Localizing Image asset can be handy if you want to AB test it. Here is how to do that:

  1. Navigate to HTML & CSS editor of the View you want to add a color Localization on:

    .. image:: /_static/img/advanced_features/campaign_navigation_html_css_editor.png

  2. Inside HTML area find an image you want to localize. An image can be either within CSS or within HTML area (`<img />`, inline styles, etc.). If the image is set within CSS you need to extract it into HTML area using inline styles:

    .. code-block:: text

      <div class="container" style="background-image: url('{{ "share_page_background" | localize: "share-page-background.jpg", trait: "asset" }}');">
        ...
      </div>

    In the example above `share_page_background` is a name of an Image Localization. `share-page-background.jpg` is a name of an Asset (Files tab within HTML & CSS Editor).

  3. Now we can see newly created Image Localization under "Images" tab:

    .. image:: /_static/img/advanced_features/editor_images_tab.png

Custom Option (Configuration) Localization
------------------------------------------

In addition to localizing Images, Colors, and static copy Talkable allows you to build really advanced Localizations where you can AB test or switch between different visual layouts of campaign Views.

An example can be to create an AB test for Equal Emphasis (all 3 sharing channels look visually equal) vs. Email Emphasis where email sharing form stands out:

  .. image:: /_static/img/advanced_features/share_page_equal_emphasis.png
    :height: 250 px

  .. image:: /_static/img/advanced_features/share_page_email_emphasis.png
    :height: 250 px

In order to chieve this AB test we need to

  1. Build two separate layouts using CSS cascades to style all nested children within a container block that holds all the content:

    .. code-block:: text

      {% assign share_page_layout = "share_page_layout" | localize: "Equal Emphasis", "Email Emphasis" %}
      <div class="container is-{{ share_page_layout | downcase | split: " " | join: "-" }}">
        ...
      </div>

    The code above creates a local Liquid variable named `share_page_layout` and assigns `share_page_layout` Configuration Localization to it.
    Then we optimize the variable value to be set as an HTML `class` attribute (downcase, replace spaces with hyphens) and set it as a part of a `class` attribute.

  2. Now inside Campaign Editor we can see newly created Configuration Localization:

    .. image:: /_static/img/advanced_features/editor_configuration_tab.png

  3. Let’s switch back to HTML & CSS editor and start applying CSS styling to both layouts. Knowing their final classes inside HTML: `class="container is-equal-emphasis"` and `class="container is-email-emphasis"` we can easily style both layouts inside CSS area like so (SCSS is also allowed and is shown as an example for code simplicity):

    .. code-block:: scss

      .container {
        &.is-equal-emphasis {
          h1 {
            font-size: 48px;
          }
        }

        &.is-email-emphasis {
          h1 {
            font-size: 32px;
          }
        }
      }

    All other nested children can be styled following this pattern.

  4. Once you’re done with styling it is very easy to set up an AB test, just go back to Campaign Editor and click "Add A/B test variant" link. Once a Campaign goes Live it will start rotating both variants following AB test distribution rules (50:50 by default).

.. container:: hidden

   .. toctree::
