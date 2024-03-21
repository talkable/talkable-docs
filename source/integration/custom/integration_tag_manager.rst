.. _integration/custom/integration_tag_manager:
.. include:: /partials/common.rst

Integrating with a Tag Manager
==============================

-  :underline:`Initialization Script in a Tag Manager:` Place the
   :ref:`Initialization Script <integration/custom/integration_components/initialization_script>`
   in a tag that is
   visible in the head template on all pages.

-  :underline:`Post Purchase Integration in a Tag Manager:` Since the post
   purchase integration on the checkout confirmation page requires the
   Init script to work, you’re welcome to combine the :ref:`Initialization Script <integration/custom/integration_components/initialization_script>`
   + :ref:`Post Purchase Script <integration/custom/integration_components/post_purchase_script>`
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

Alternative Approach: Direct Integration
----------------------------------------

To mitigate these potential issues, you can integrate Talkable directly into your web pages without using GTM. Here's a step-by-step guide on :ref:`custom integration <integration/custom/integration_components/initialization_script>`

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

**Conclusion:**

By understanding the potential performance impact and alternative approach, you can make an informed decision on the best method to integrate Talkable with your website using Google Tag Manager.
