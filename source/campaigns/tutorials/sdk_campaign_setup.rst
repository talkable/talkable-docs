.. _campaigns/tutorials/sdk_campaign_setup:
.. include:: /partials/common.rst

.. meta::
   :description: Complete guide for setting up Talkable campaigns to work with iOS and Android SDKs, including native sharing, mobile optimization, and campaign tags.

SDK Campaign Setup
==================

This guide explains how to set up Talkable campaigns to work seamlessly with iOS and Android mobile SDKs. 

When creating campaigns for mobile SDKs, you need to configure specific settings that differ from standard web campaigns. This includes:

- Campaign tags for SDK targeting
- Native sharing channels for mobile devices
- Mobile-optimized layouts and user experience
- Platform-specific sharing options

Campaign Tags
-------------

Campaign tags are essential for SDK integration as they determine which campaigns are displayed when the SDK makes a request.

Default Campaign Tags
~~~~~~~~~~~~~~~~~~~~~

Each SDK uses default tags based on the campaign type:

.. list-table::
   :header-rows: 1
   :widths: 20 25 25 30

   * - Platform
     - Campaign Type
     - Default Tag
     - SDK Code
   * - iOS
     - Standalone
     - ``ios-invite``
     - Default behavior
   * - iOS
     - Post Purchase
     - ``ios-post-purchase``
     - Default behavior
   * - Android
     - Standalone
     - ``android-invite``
     - Default behavior
   * - Android
     - Post Purchase
     - ``android-post-purchase``
     - Default behavior

.. note::
   **Event-based integration** does not use default tags. You **must** specify campaign tags explicitly 
   when using custom events. See :ref:`iOS Custom Events <ios_sdk/integration/event>` and 
   :ref:`Android Custom Events <android_sdk/integration/event>` for details.

Custom Campaign Tags
~~~~~~~~~~~~~~~~~~~~

You can specify custom tags for more control over which campaigns are shown:

**iOS Example:**

.. code-block:: objc

   [[Talkable manager] registerOrigin:TKBLAffiliateMember params:@{TKBLCampaignTags: @"your-custom-tag"}];

**Android Example:**

.. code-block:: java

   AffiliateMember affiliateMember = new AffiliateMember(customer);
   affiliateMember.setCampaignTag("your-custom-tag");

**Campaign Configuration:**

1. Navigate to **Campaign → Rules → Tags**
2. Add your custom tag (e.g., ``your-custom-tag``)
3. Ensure the campaign status is **Live** or **Test**

.. tip::
   Use custom tags when running multiple campaigns simultaneously or when you want to 
   show different campaigns to different user segments.

Native Sharing for Mobile
--------------------------

Native sharing allows users to share offers using their device's built-in sharing capabilities, providing access to all installed apps (Messages, WhatsApp, Instagram, etc.).

Enabling Native Sharing
~~~~~~~~~~~~~~~~~~~~~~~~

To enable native sharing in your campaign:

**1. Configure Mobile View Options**

Add or update the following localization:

.. code-block:: liquid

   {% assign mobile_share_page_sharing_channels = "mobile_share_page_sharing_channels" | localize: "All", "Native Sharing only" %}

**Options:**

- ``"All"`` - Shows traditional sharing channels (SMS, Email, etc.) plus a "Share more" button for native sharing
- ``"Native Sharing only"`` - Shows only a native share button (recommended for mobile-first experiences)

**2. Add Native Sharing Localizations**

Add these localizations to your campaign:

.. code-block:: liquid

   {% assign native_sharing_cta = "native_sharing_cta" | localize: "Share with friends" %}
   
   {% assign native_share_title = "native_share_title" | localize: "Special offer from [[ site_setup.name ]]" %}
   
   {% assign native_share_description = "native_share_description" | localize: "Get [[ friend_incentive.description ]] off at [[ site_setup.name ]]" %}

**3. Add Native Share Button**

Add this button to your share page template:

.. code-block:: liquid

   <a href="#" class="button is-native js-share-native">
     <span class="button-icon is-native">
       <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
         <circle cx="12" cy="5" r="2"/><circle cx="12" cy="12" r="2"/><circle cx="12" cy="19" r="2"/>
       </svg>
     </span>
     <span class="button-text">{{ native_sharing_cta }}</span>
   </a>

**4. Add JavaScript Implementation**

Add this JavaScript to handle native sharing:

.. code-block:: javascript

   function native_share(title, url, description) {
     if (navigator.share) {
       navigator.share({
         title: title,
         text: description,
         url: url
       }).then(function () {
         Talkable.shareSucceeded("native_share");
       }).catch(function (error) {
         console.error("Error sharing:", error);
       });
     } else {
       // Fallback for browsers without Web Share API
       alert("Native sharing is not supported on this device");
     }
   }

   $(".js-share-native").click(function(e) {
     e.preventDefault();
     native_share(
       "{{ 'native_share_title' | localize }}", 
       "{{ 'native_share' | claim_url }}", 
       "{{ 'native_share_description' | localize }}"
     ); 
   });

.. note::
   Native sharing uses the **Web Share API**, which is supported on:
   
   - iOS Safari 12.2+
   - Android Chrome 61+
   - Android Firefox 71+
   - WebView components in iOS and Android SDKs
   
   It is **not** supported on most desktop browsers.

Mobile View Modes
-----------------

The SDK campaigns support two mobile view optimization modes:

Default Mode
~~~~~~~~~~~~

Shows all enabled sharing channels in standard order:

.. code-block:: liquid

   {% assign mobile_view_option = "mobile_view_option" | localize: "Default", "Suggested" %}
   
   {% if mobile_view_option == "Default" %}
     <!-- Standard layout -->
   {% endif %}

**Characteristics:**

- All channels displayed equally
- Native sharing appears at bottom
- Traditional sharing button layout

Suggested Mode
~~~~~~~~~~~~~~

Optimized layout that prioritizes SMS and native sharing:

.. code-block:: liquid

   {% if mobile_view_option == "Suggested" %}
     <!-- SMS appears first if enabled -->
     <!-- Native sharing more prominent -->
   {% endif %}

**Characteristics:**

- SMS sharing appears first (if enabled)
- Native sharing button is more prominent
- Optimized for mobile user experience
- Better conversion rates on mobile devices

Sharing Channel Configuration
------------------------------

Configure which sharing channels are available in your mobile campaign.

Understanding user_agent Helper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Talkable provides a ``user_agent`` helper object that detects device capabilities and platform:

**Device Detection:**

.. code-block:: liquid

   {% if user_agent.mobile %}
     <!-- Mobile device (phone or tablet) -->
   {% endif %}
   
   {% if user_agent.desktop %}
     <!-- Desktop device -->
   {% endif %}
   
   {% if user_agent.tablet %}
     <!-- Tablet device -->
   {% endif %}

**Native Features Supported by SDK:**

The SDK automatically detects and reports the following native features:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Feature
     - Description
   * - ``send_sms``
     - SMS sharing capability (requires SIM card and telephony support)
   * - ``copy_to_clipboard``
     - Copy referral link to device clipboard (always available)
   * - ``share_via_native_mail``
     - Native email app sharing (detects available email clients)
   * - ``share_via_facebook``
     - Facebook sharing (requires Facebook SDK initialization)
   * - ``share_via_facebook_messenger``
     - Facebook Messenger sharing (requires Facebook SDK and Messenger app)
   * - ``share_via_twitter``
     - Twitter/X sharing (currently disabled on mobile SDKs)
   * - ``share_via_whatsapp``
     - WhatsApp sharing (detects WhatsApp installation)

**Feature Detection Examples:**

.. code-block:: liquid

   {% if user_agent.features.send_sms %}
     <!-- Device supports SMS sharing -->
   {% endif %}
   
   {% if user_agent.features.share_via_facebook %}
     <!-- Facebook SDK is initialized -->
   {% endif %}
   
   {% if user_agent.features.share_via_whatsapp %}
     <!-- WhatsApp is installed -->
   {% endif %}
   
   {% if user_agent.features.copy_to_clipboard %}
     <!-- Clipboard access available (always true on mobile) -->
   {% endif %}

.. tip::
   Always use ``user_agent.features`` checks to ensure sharing buttons only appear when the device 
   supports them. This prevents showing non-functional buttons to users.

SMS Sharing
~~~~~~~~~~~

.. code-block:: liquid

   {% assign advocate_share_page_channel_sms = "advocate_share_page_channel_sms" 
      | localize: trait: "boolean", default: "Enabled" %}

**Implementation in template:**

.. code-block:: liquid

   {% if advocate_share_page_channel_sms and user_agent.features.send_sms %}
     <li>
       <a href="#" class="button js-share-offer-via-sms">
         <span class="button-icon is-sms">
           <svg><!-- SMS icon --></svg>
         </span>
         Share by SMS
       </a>
     </li>
   {% endif %}

**Requirements:**

- Only available on mobile devices
- Requires ``user_agent.features.send_sms`` capability check
- Automatically detected by device browser
- Button only renders when both localization is enabled AND device supports SMS

WhatsApp Sharing
~~~~~~~~~~~~~~~~

.. code-block:: liquid

   {% assign advocate_share_page_channel_whatsapp = "advocate_share_page_channel_whatsapp" 
      | localize: "Enable for mobile only", "Enable for desktop only", 
                  "Enable for desktop and mobile", "Disable for desktop and mobile", 
                  default: 'Disable for desktop and mobile' %}

**Implementation in template:**

.. code-block:: text

   {% if advocate_share_page_channel_whatsapp == "Enable for desktop and mobile" %}
     {% assign show_whatsapp = true %}
   {% endif %}
   {% if advocate_share_page_channel_whatsapp == "Enable for mobile only" and user_agent.mobile %}
     {% assign show_whatsapp = true %}
   {% endif %}
   {% if advocate_share_page_channel_whatsapp == "Enable for desktop only" and user_agent.desktop %}
     {% assign show_whatsapp = true %}
   {% endif %}

   {% if show_whatsapp %}
     <li>
       <a href="#" class="button js-share-offer-via-whatsapp" target="_blank">
         Share via WhatsApp
       </a>
     </li>
   {% endif %}

**Options:**

- ``"Enable for mobile only"`` - Recommended for SDK campaigns (checks ``user_agent.mobile``)
- ``"Enable for desktop only"`` - For web-only campaigns (checks ``user_agent.desktop``)
- ``"Enable for desktop and mobile"`` - Both platforms
- ``"Disable for desktop and mobile"`` - Disabled

Email Sharing
~~~~~~~~~~~~~

.. code-block:: liquid

   {% assign advocate_share_page_channel_email = "advocate_share_page_channel_email" | localize: trait: "boolean", default: "Enabled" %}

**Features:**

- Opens email form in popup/modal
- Supports single or multiple recipients
- Can include personalized message
- Works on all platforms

Link Sharing
~~~~~~~~~~~~

.. code-block:: liquid

   {% assign advocate_share_page_channel_link = "advocate_share_page_channel_link" | localize: trait: "boolean", default: "Enabled" %}

**Features:**

- Copy referral link to clipboard
- Share via any channel
- Useful as fallback option

Facebook/Twitter Sharing
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: liquid

   {% assign advocate_share_page_desktop_facebook_sharing = "advocate_share_page_desktop_facebook_sharing" 
      | localize: "Wall Post", "Direct Message", "Both", "Disabled" %}
   
   {% assign advocate_share_page_channel_twitter = "advocate_share_page_channel_twitter" 
      | localize: trait: "boolean", default: "Disabled" %}

**Implementation in template:**

.. code-block:: text

   {% if advocate_share_page_desktop_facebook_sharing != "Disabled" 
         and user_agent.features.share_via_facebook %}
     <li>
       <a href="#" class="button js-share-offer-via-facebook">
         Share on Facebook
       </a>
     </li>
   {% endif %}

   {% if advocate_share_page_channel_twitter and user_agent.features.share_via_twitter %}
     <li>
       <a href="#" class="button js-share-offer-via-twitter">
         Share on X
       </a>
     </li>
   {% endif %}

**Feature Detection:**

- Facebook: Requires ``user_agent.features.share_via_facebook``
- Twitter: Requires ``user_agent.features.share_via_twitter``
- These features are automatically detected based on browser/device capabilities

.. note::
   For iOS SDK, Facebook and Twitter sharing require delegate method implementation. 
   See :ref:`iOS Social Sharing <ios_sdk/social_sharing>` for details.

Best Practices
--------------

Campaign Tag Strategy
~~~~~~~~~~~~~~~~~~~~~

**Single Campaign:**

- Use default tags (``ios-invite``, ``android-invite``)
- Simplest setup, lowest maintenance

**Multiple Campaigns:**

- Use custom tags for segmentation
- Example: ``vip-ios-invite``, ``standard-ios-invite``
- Allows A/B testing different offers

.. important::
   **Campaign Matching Behavior**: When multiple campaigns have matching tags, only **one campaign will be selected** and displayed to the user. The selection is based on campaign priority and other internal factors. Ensure your tag strategy accounts for this behavior to avoid unexpected campaign conflicts.

**Seasonal Campaigns:**

- Include date/season in tag: ``summer-2024-ios``
- Easy to identify and manage
- Clear campaign lifecycle

Sharing Channel Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~

**For Mobile-First Experience:**

1. **Enable Native Sharing**: Set ``mobile_share_page_sharing_channels`` to ``"Native Sharing only"``
   
   - Simplest user experience
   - Access to all device apps
   - Highest conversion rate

2. **Enable SMS**: Most popular mobile sharing method
   
   - Set ``advocate_share_page_channel_sms`` to ``"Enabled"``
   - Works on all mobile devices
   - High open and click rates

3. **Use "Suggested" Mobile View**: For optimized mobile layout
   
   - Set ``mobile_view_option`` to ``"Suggested"``
   - Prioritizes SMS and native sharing
   - Better mobile user experience

**For Hybrid Experience (Mobile + Web):**

1. **Enable "All" Sharing Channels**: Set ``mobile_share_page_sharing_channels`` to ``"All"``
   
   - Shows traditional channels (Email, Facebook, etc.)
   - Plus native sharing as "Share more" option
   - Works across all devices

2. **Configure Platform-Specific Channels**:
   
   - WhatsApp: ``"Enable for mobile only"``
   - Facebook: Configure for desktop
   - SMS: Mobile only

Related Documentation
---------------------

- :ref:`iOS SDK Standalone Campaign <ios_sdk/integration/standalone>`
- :ref:`Android SDK Standalone Campaign <android_sdk/integration/standalone>`
- :ref:`iOS Social Sharing <ios_sdk/social_sharing>`
- :ref:`iOS Advanced Features <ios_sdk/advanced>`
- :ref:`Android Advanced Features <android_sdk/advanced>`
- :ref:`Campaign Localization <campaigns/localization>`
- :ref:`Campaign Views <campaigns/views>`
