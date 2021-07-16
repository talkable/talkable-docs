.. _integration/loyalty/integration_components:
.. include:: /partials/common.rst

.. meta::
   :description: Find the components of what Talkable is composed.

Integration Components
======================

Talkable Loyalty is composed of the following components:

1. `Initialization Script <Initialization Script_>`_

   **Script Location.** The Initialization script should be placed in the head template or some template
   that spans every page. All other integration components are dependent on the Init script.

   **Data Capture.** The Initialization Script should pass variables for logged in users:

    - Email

2. :ref:`Loyalty Dashboard`

3. :ref:`Loyalty Redeem Widget`

|hr|

.. _integration/loyalty/integration_components/initialization_script:

Initialization Script
~~~~~~~~~~~~~~~~~~~~~

The Initialization script should be placed in the head template or some
template that spans every page. Talkable JS library size is typically
around 20kB and causes no noticeable impact to your site’s loading time.
All other integration components are dependent on the Initialization
script.

.. code-block:: html

   <!-- Begin Talkable integration code -->
   <script async src="https://d2jjzw81hqbuqv.cloudfront.net/integration/clients/<YOUR-TALKABLE-SITE-ID>.min.js"></script>
   <script>
     window._talkableq = window._talkableq || [];
     window._talkableq.unshift(['init', { site_id: '<YOUR-TALKABLE-SITE-ID>' }]);

     window._talkableq.push(['authenticate_customer', {
       email: '' // required, loyalty program is only available to logged in users. Example: 'customer@example.com'
     }]);
   </script>
   <!-- End Talkable integration code -->

Initialization Script Notes
---------------------------

1. **Site ID.** You can obtain your Site ID by logging into the Talkable
   platform where Site ID is displayed on your Dashboard and URL as seen
   here:

   .. figure:: /_static/img/site_id.png
      :alt: Site ID

2. **Variables.** Use your dynamic variables to pass user details.

|hr|

.. _Loyalty Dashboard:

Loyalty Dashboard
~~~~~~~~~~~~~~~~~

Create a new HTML page with URL
path (`www.your-site.com/loyalty`), add the Talkable Container DIV in
the body of the page and show loyalty campaign with the JS API function:

.. code-block:: html

   <div id="talkable-loyalty"></div>
   <script>
     window._talkableq.push(['show_loyalty', {
       optin: true // optional, determines whether a customer agreed to participate in the loyalty program
     }]);
   </script>

Loyalty Dashboard Notes
-----------------------

1. The `Talkable Initialization Script <Initialization Script_>`_ must be
   present in your head template in order for the Loyalty Dashboard to work.

2. Talkable will inject loyalty content where Talkable Container
   resides in your DOM. Adding a new page is only a suggestion. The
   dashboard can be added inline inside your user accounts menu, however
   the dashboard content width for proper display is 980px.

3. Allow your users to reach the Loyalty Dashboard by adding a link
   from any place that makes sense considering your website configuration.
   Most common uses are links in the user accounts section, or from the user accounts menu.

4. `show_loyalty` optionally accepts `email`, `first_name`, `last_name`, and `custom_properties`,
   which override respective values from `authenticate_customer`. Email must be provided in either of the sources to
   show loyalty dashboard.

|hr|

.. _Loyalty Redeem Widget:

Loyalty Redeem Widget
~~~~~~~~~~~~~~~~~~~~~

Add Talkable container DIV element at the checkout
exactly where the loyalty points redemption widget should render, and call JS API function to render the widget:

.. code-block:: html

   <div id="talkable-loyalty"></div>
   <script>
     window._talkableq.push(['show_loyalty_redeem_widget', {}]);
   </script>

Loyalty Redeem Widget Notes
---------------------------

1. `show_loyalty_redeem_widget` optionally accepts `email` and `custom_properties`. If none provided, values will be
   taken from respective parameters of `authenticate_customer`. If email is not available from either of the sources,
   signup widget will be rendered instead.

|hr|

.. _Loyalty Actions:

Loyalty Actions
~~~~~~~~~~~~~~~

To register custom loyalty actions (e.g. completing surveys, adding reviews, uploading something on site),
use the following code:

.. code-block:: html

   <script>
     window._talkableq.push(['register_loyalty_action', {
       rule_identifier: '', // required, can be found in Campaign Rules -> Loyalty action configurations -> "identifier" field
       traffic_source: '' // optional
     }]);
   </script>

Loyalty Actions Notes
---------------------

1. `register_loyalty_action` optionally accepts `email` and `custom_properties`. If none provided, values will be
   taken from respective parameters of `authenticate_customer`. Email must be provided in either of the sources to
   register loyalty actions.
