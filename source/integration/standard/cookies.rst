.. _integration/standard/cookies:
.. include:: partials/common.rst

.. meta::
   :description: This is all about how we use cookies.

Cookies
#######

At Talkable, we prioritize enhancing your digital experience.
Our use of cookies is instrumental in this endeavor, as they play a critical role in tracking referrals and conversions, personalizing content, and maintaining the overall performance and reliability of our services.

Understanding the Cookies We Use
--------------------------------

We broadly categorize our cookies and similar technologies as follows:

**Strictly Necessary**

These cookies and other technologies are essential to enabling your use of our Site  and Services and its features.
Without these cookies, key functionalities (like sign-up processes) would be unfeasible.
These cookies may be associated with personal data.

**Functionality**

These cookies and other technologies improve your experience by enabling personalization (like remembering language and region).
They can help you fill out forms on our campaigns more easily.
These cookies may be associated with personal data.

**Analytics and Performance**

These cookies and other technologies help us learn how well our Campaigns and Services are performing.
We use these cookies to understand, improve, and research our Site and Services.

.. list-table::
   :widths: 30 30 30 10
   :header-rows: 1

   * - Cookie name
     - Purpose
     - Domain(s)
     - Retention period(Days)
   * - ``tkbl_session_id``
     - Strictly Necessary
     - | talkable.com
       | shop domain
     - 0
   * - ``tkbl_session``
     - Functionality
     - | talkable.com
       | shop domain
     - 400
   * - ``tkbl_cvuuid``
     - Functionality
     - | talkable.com
       | shop domain
     - 400
   * - `multiple <https://newrelic.com/termsandconditions/cookie-policy/cookie-table>`_
     - Analytics and Performance
     - \*.newrelic.com
     - 0-400
   * - ``bugsnag*``
     - Analytics and Performance
     - \*.bugsnag.com
     - 0-400
   * - ``_ga``
     - Analytics and Performance
     - talkable.com
     - 400

.. _integration/standard/cookies/gdpr_and_ccpa_compliance:

GDPR and CCPA compliance
------------------------
Talkable ensures compliance with GDPR and CCPA regulations.
In compliant mode, we only set a session cookie during the first user interaction.
These session cookies, being temporary, disappear once the browser is closed.
Under GDPR and CCPA, setting such cookies does not require user consent.
Post-consent (e.g., during signup), Talkable activates standard cookies to monitor user activities, aligning with regulatory guidelines.

.. note::
   Limitations of compliance mode seriously hinders Talkable ability to track referrals and conversions.
   It is advised to use compliant mode only if you are legally obligated to do so.

To enable GDPR and CCPA compliant mode, please contact your Customer Success Manager.

