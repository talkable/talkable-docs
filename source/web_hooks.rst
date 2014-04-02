.. _web_hooks:
.. include:: /partials/common.rst

Web Hooks
#########

Web hooks are "user-defined HTTP callbacks". They are usually triggered by some
event on Curebit's site.

http://en.wikipedia.org/wiki/Webhook

Each web hook in Curebit is defined with an HTTP URL to deliver web hook data
(aka payload). This URL should be defined and implemented on the client's site.

.. raw:: html

   <h2>Setup and Testing</h2>

Testing web hooks can be accomplished with the help of RequestBin, an external
service that tests your post-receive messages.

1. Visit `RequestBin`_ and click **Create a RequestBin**.
2. Copy the URL you are given.
3. Open your site on Web Hooks setup page.
4. Click **New**.
5. Select web hook type.
6. Paste your RequestBin URL and save.
7. Click **Deliver Sample** near the web hook you want to test.
8. After you finish the implementation on your site **change RequestBin URL
   to the live URL** on your site.
9. Click **Deliver Sample** to test web hook with Live URL.

.. raw:: html

   <h2>Data</h2>

All web hooks are delivered as an HTTP Post request with the main parameter
called payload. All data inside this parameter is encoded as JSON. Below is
a PHP parameter decode example:

.. code-block:: php

   json_decode($_POST["payload"])

.. raw:: html

   <h2>Parsing Timestamps</h2>

**Timestamp data type** is not a part of JSON standard. That is why timestamps
are passed as strings in `ISO-8601`_ compatible format. You need to be sure that
your date parser is compatible to this standard. Otherwise issues may appear.
People that use Java need to look through: |br|
http://stackoverflow.com/questions/2201925/converting-iso8601-compliant-string-to-java-util-date

.. raw:: html

   <h2>Response Codes</h2>

Curebit considers a web hook as "delivered successfully" in the case that the site
server returned a **2xx response status**. Otherwise Curebit will continually
retry to deliver a webhook after a set interval of time.

.. raw:: html

   <h2>HTTP Responses and Their Meanings</h2>

* 2xx: Success
* 200: OK
* 201: Created
* 202: Accepted
* 203: Non Authoritative Information
* 204: No Content
* 205: Reset Content
* 206: Partial Content

If you have a problem on your server, you can answer with code 500. If there is
some problem in our request (problem on Curebit's side), you can answer "400 Bad Request".

Any other error code and we will retry later.

.. raw:: html

   <h2>Security Key</h2>

Also there is a key parameter that has a unique value for each site to identify
Curebit as an authorized server to call the web hook (please check it against
a copy on your side). The Security Key for your site can be found in Web Hooks
setup page if you have at least one web hook created.

.. raw:: html

   <h2>Compatibility and Versioning</h2>

Curebit web hooks do not currently have versioning. Current spec will not be
changed for all existing hooks. But Curebit dev team leave a right to add any
additional data to them without removing or changing existing one. Your
implementation should be safe to such changes.

|hr|
See available web hooks on the navigation sidebar.

.. _RequestBin: http://www.w3.org/TR/NOTE-datetime
.. _ISO-8601: http://en.wikipedia.org/wiki/ISO_8601

.. container:: hidden

   .. toctree::

      Create Coupons <web_hooks/create_coupon>
      Referral <web_hooks/referral>
      Post Share <web_hooks/post_share>
      Advocate Signup <web_hooks/offer_signup>
      Friend Email Gating <web_hooks/claim_signup>
