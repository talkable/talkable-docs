.. _integration/standard/integration_components:
.. include:: /partials/common.rst

.. meta::
   :description: Find the components of what Talkable is composed.

Integration Components
======================

Talkable is composed of the following components:

1. :ref:`Initialization Script <integration/standard/integration_components/initialization_script>`

   **Script Location.** The Initialization script should be placed in the head template or some template
   that spans every page. All other integration components are dependent on the Init script.

   **Data Capture.** The Initialization Script should pass variables for logged in users:
    
   - Email
   - Phone Number
   - First Name
   - Last Name

2. :ref:`Post Purchase Script <integration/standard/integration_components/post_purchase_script>`

   **Script Location.** The Post Purchase script should be placed on the checkout confirmation page.

   **Script Dependency.** The Post Purchase script should be fired after the Initialization script.

   **Data Capture.** This script needs to capture purchase based details

   - Email of purchaser
   - Order Number
   - Subtotal (pre-tax, post-discount amount)
   - Coupon code(s) used at checkout (can accept an array of strings if you allow for multiple coupons to
     be applied at checkout)
   - Currency ISO code. It is required for multi-currency sites.
   - (optional) Shipping Address for additional fraud protection.
   - (optional) Shopping cart line items. This is only necessary if segmenting based on cart contents.
   - (optional) Segments (segment1, segment2, segment3). Custom attribute for segmenting purchases by value (e.g., location, age group, source channel, platform, gender, interests).

3. In case your business has one-time purchases and subscription model, or you are in SaaS
   business we recommend integrating through Events. :ref:`Learn more <advanced_features/events>`.

4. :ref:`Advocate Landing Page <integration/standard/integration_components/advocate_landing_page>`.

   Create an HTML page (URL path /share) with your standard site header and footer.
   Add the Talkable Container DIV in the body. This tells Talkable where to inject content.

5. :ref:`Referral Dashboard (my account) <integration/standard/integration_components/referral_dashboard>`.

   Similar to the advocate landing page, create an HTML page that’s linked to from a menu in user accounts.
   Add the Talkable Container DIV in the body. This tells Talkable where to inject content.

|hr|

.. _integration/standard/integration_components/initialization_script:

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
       email: '', // Optional - Email of the customer, if available. Example: 'customer@example.com'
       phone_number: '', // Optional - Customer's phone number. Example: '+12025551111'
       first_name: '', // Optional - First name of the customer. Example: 'John'
       last_name: '', // Optional - Last name of the customer. Example: 'Smith'
       traffic_source: '', // Optional - Traffic source that led to the campaign. Example: 'facebook'
       segment1: '', // Optional - Custom segment (e.g., location, age group, source channel, platform, gender, interests).
       segment2: '', // Optional - Custom segment (e.g., location, age group, source channel, platform, gender, interests).
       segment3: '' // Optional - Custom segment (e.g., location, age group, source channel, platform, gender, interests).
     }]);
   </script>
   <!-- End Talkable integration code -->

In this example, `segment1`, `segment2`, and `segment3` attributes are passed through `authenticate_customer` to enable segmentation without requiring an Origin creation.

.. note::

   Segments can also be passed in `register_affiliate`, `register_purchase`, and `register_event`, providing flexibility for different integration scenarios.

This approach simplifies custom data handling for customers, allowing for unified data across various methods and optimizing segmentation management without additional calls.

Initialization Script Notes
---------------------------

1. **Site ID.** You can obtain your Site ID by logging into the Talkable
   platform where Site ID is displayed on your Dashboard and URL as seen
   here:

   .. figure:: /_static/img/site_id.png
      :alt: Site ID

2. **Variables.** Use your dynamic variables to pass user details {email,
   first_name, last_name} if the user is logged in and the data
   exists. If the data does not exist, you can pass a null value or a
   blank string. If your website doesn’t have a user accounts section
   and this info is never available, it’s acceptable to completely omit
   the parameters, or pass empty strings.

|hr|

.. _integration/standard/integration_components/post_purchase_script:

Post Purchase Script
~~~~~~~~~~~~~~~~~~~~

The post purchase script should be placed on your checkout confirmation
page or any page that immediately follows checkout. All parameters can
be passed as strings. A Number can be passed for `subtotal`, however, if
using any calculation, you’re responsible for ensuring that some number is
passed where division by zero or `null` value does not occur.

.. include:: /partials/purchase_script.rst

Post Purchase Script Notes
--------------------------

1. Mandatory parameters must be passed or the purchase will not be
   passed to Talkable. Mandatory parameters are: `email`, `order\_number`,
   `subtotal`

2. `coupon_code` is not mandatory, but it's preferred to be passed via the script, since some of the fraud checks and referral tracking methods rely on those

3. Shipping parameters are optional but gives the added benefit of
   additional fraud protection

4. If you’re using a payment gateway that directs the user away from
   your domain, you should ensure that some auto return feature is
   enabled so that the user returns to the checkout confirmation page to
   allow the post purchase script to run.

5. If you’re using a tag manager :ref:`click here <integration/standard/integration_tag_manager>`.

6. If you need to pass shopping cart line items, to see the alternate
   post purchase integration script :ref:`click here <advanced_features/product_items>`.

7. For individual purchase segmentation, you have the option to utilize one of three custom
   segments: `segment1`, `segment2`, `segment3`.
   These segments can represent various criteria such as location, age group, traffic source, etc.

.. note::

   All PII params support data encryption. Find more about :ref:`Params Encryption <advanced_features/params_encryption>`.

.. _integration/standard/integration_components/advocate_landing_page:

Advocate Landing Page
~~~~~~~~~~~~~~~~~~~~~

Create a new HTML page with URL path (`www.your-site.com/share`) and add the Talkable Container DIV
in the body of the page between your standard site header and footer:

.. note::
   The Talkable Container DIV id can be changed upon request to the Talkable team.
   The current DIV id value for each Event Category can be found on the Placements page.

.. code-block:: html

   <div id="talkable-offer"></div>

Advocate Landing Page Notes
---------------------------

1. The Talkable Initialization script must be present in your head
   template in order for the advocate landing page to work

2. Talkable will inject referral content where Talkable Container
   resides in your DOM

3. URL Path: If you can’t use URL path `www.your-site.com/share` then
   you’ll need to update the Site Placements section inside of Talkable
   for the Invite Advocate Landing Page to match the exact URL path that
   you intend to use via
   `https://www.admin.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/placements:`

   .. figure:: /_static/img/placement_edit.png
      :alt: Placement Edit

|hr|

.. _integration/standard/integration_components/referral_dashboard:

Referral Dashboard
~~~~~~~~~~~~~~~~~~

Similar to the Advocate Landing Page, create a new HTML page with URL
path (`www.your-site.com/referrals`) and add the Talkable Container DIV in
the body of the page:

.. note::
   The Talkable Container DIV id can be changed upon request to the Talkable team.
   The current DIV id value for each Event Category can be found on the Placements page.

.. code-block:: html

   <div id="talkable-offer"></div>

Referral Dashboard Notes
------------------------

1. The :ref:`Talkable Initialization Script <integration/standard/integration_components/initialization_script>` must be present in your head
   template in order for the referral dashboard to work

2. Talkable will inject referral content where Talkable Container
   resides in your DOM. Adding a new page is only a suggestion. The
   dashboard can be added inline inside your user accounts menu, however
   the dashboard content width for proper display is 980px.

3. **URL Path.** If you don’t host on `www.your-site.com/referrals` then
   you’ll need to update the Site Placements section inside of Talkable
   for the Dashboard Placement to use the exact URL path you intend to
   host the Referral Dashboard on via
   `https://www.talkable.com/sites/<YOUR-TALKABLE-SITE-ID>/placements`

4. **Linking to the Referral Dashboard.** Allow your users to reach the
   Referral Dashboard by adding a link from any place that makes sense
   considering your website configuration. Most common uses are links in
   the user accounts section, or from the user accounts menu.

5. **Host on a page that’s only accessible behind login.** The Referral
   Dashboard contains semi-sensitive information about an Advocate’s
   referral history. If you don’t have user logins, then the Referral
   Dashboard can be configured to display partially obfuscated data for
   public access.

.. container:: hidden

 .. toctree::

    Alternate Post Purchase Script for cart line item passing <alternate_post_purchase>
    Integrating with a Tag Manager <integration_tag_manager>
