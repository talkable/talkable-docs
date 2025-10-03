.. _integration/standard/integration_tag_manager:
.. include:: partials/common.rst

Integrating with a Tag Manager
==============================

-  :underline:`Initialization Script in a Tag Manager:` Place the
   :ref:`Initialization Script <integration/standard/integration_components/initialization_script>`
   in a tag that is
   visible in the head template on all pages.

-  :underline:`Post Purchase Integration in a Tag Manager:` Since the post
   purchase integration on the checkout confirmation page requires the
   Init script to work, you’re welcome to combine the :ref:`Initialization Script <integration/standard/integration_components/initialization_script>`
   + :ref:`Post Purchase Script <integration/standard/integration_components/post_purchase_script>`
   script into a
   single tag for the checkout confirmation page. In fact this is
   recommended for Google Tag Manager, when combining the place the
   Initialization script on top/before the Post purchase script in the
   tag.

-  :underline:`Tag Manager Data Layer to Pass Variables:` You’ll need to
   ensure a data layer object is set up to collect and pass the
   variables to Talkable inside your tag.

-  :underline:`Troubleshooting:` You can use `window._talkableq` for all
   `talkableq` variable instances if you’re having trouble with variable
   interpolation and need to use a global namespace.

Potential Performance Impact
----------------------------

This section addresses two key considerations for integrating Talkable using Google Tag Manager (GTM):

**1. Potential Performance Impact:**

- In some cases, using GTM to load the Talkable integration code can introduce a slight delay in the referral program's functionality. This is because GTM typically waits for all its tags to load before executing them.
- If you've identified performance concerns related to the Talkable integration's load time, consider the alternative approach outlined below.

**2. Safari Private Mode Blocking Third-Party Vendors:**

- A known issue exists where Safari in private mode blocks third-party vendors, including GTM. This can prevent the Talkable integration code from loading entirely, hindering the referral program's operation.

Best Practices for Speed Optimization
-------------------------------------

1. Make sure the campaign uses optimized image/file sizes and upload lower-resolution versions if it is.

2. There should be only one copy of the Initialization script on the page. Delete all duplicates if there are any.

3. Make sure you don't have JS errors from code executed before Talkable. If there is some critical error, the browser may not be able to process Talkable scripts quickly.

4. Implementing a custom domain for your integration won't directly increase its speed, but it will significantly reduce issues related to incognito mode and security policies blocking for third-party content.

.. note:: 
   If you use GTM, you can add `priority <https://support.google.com/tagmanager/answer/2772421>`_ to the tag. The higher the priority, the quicker it gets loaded.

   .. image:: /_static/img/gtm-priority.png

Alternative Approach: Direct Integration
----------------------------------------

To mitigate these potential issues, you can integrate Talkable directly into your web pages without using GTM. Here's a step-by-step guide on :ref:`Custom Integration <integration/standard/integration_components>`.

**Benefits of Direct Integration:**

- **Improved Performance:** Eliminates the delay associated with GTM loading all tags before execution.
- **Enhanced Compatibility:** Ensures the Talkable integration code loads even in Safari private mode, where GTM might be blocked.

**Choosing the Right Approach:**

The optimal approach depends on your specific priorities:

- If performance is a critical concern, direct integration is generally recommended.
- If you prefer a more centralized tag management system for other integrations, GTM might still be suitable, but be aware of the potential performance impact and Safari private mode blocking.

**Additional Considerations:**

- Thoroughly test both approaches (GTM and direct integration) to ensure the Talkable referral program functions as expected in all browsers and scenarios.
- If you encounter further issues, check Talkable's support resources or contact support team for assistance.

Verifying success
-----------------

1. Open Talkable admin, open or create Floating widget campaign. Scroll down to the Placements section and click on the eye button. It will open up your site with the Talkable campaign shown in test mode.
2. Submit purchase through your site.
3. Open Talkable admin, go to Reports → Purchases and find your purchase in the list.
4. Visit the Standalone page you created for the site, it should be showing up within 1-3 seconds.

Removing the Talkable Integration Script from GTM
-------------------------------------------------

If you've decided to remove the Talkable integration script from GTM, follow these steps:

1. Log in to your Google Tag Manager account.
2. Locate the Talkable integration tag (usually named "Talkable Integration" or similar).
3. Click on the tag to open its details.
4. Click the "Delete" button to remove the Talkable integration tag.

**Important Note:** After removing the Talkable integration script from GTM, you'll need to implement the :ref:`direct integration approach <integration/standard/integration_components>` documented earlier to ensure Talkable functionality on your website.

.. note::
   Talkable doesn't recommend adding integration as tags in Google Tag Manager because of slow loading of campaigns for certain user agents as well as GTM being blocked by some Ad blockers

Helpful Links
-------------

- `How to make campaigns load faster? <https://talkable.freshdesk.com/support/solutions/articles/43000682297-how-to-make-campaigns-load-faster->`_
- `How to integrate with a Tag Manager <https://talkable.freshdesk.com/support/solutions/articles/43000628861-how-to-integrate-with-a-tag-manager>`_
- `GTM tag prioritization <https://support.google.com/tagmanager/answer/2772421>`_
