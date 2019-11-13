.. _campaigns/views/affiliate_members_new:
.. include:: /partials/common.rst

.. meta::
   :description: Advocate referral program sign up page means that advocate signs up by entering their email address.

.. _advocate_signup_page_view:

Advocate Signup Page
--------------------

Advocate referral program sign up page (only for Standalone Campaign). On this page Advocate signs up by entering their email address.
|br|
|br|

.. image:: /_static/img/basics/advocate-signup.png
   :alt: Advocate signup

.. raw:: html

   <h4>Default template markup:</h4>

.. code-block:: html

   <form accept-charset="UTF-8" action="{{ create_affiliate_member_path }}" method="post">
     <input type="email" name="affiliate_member[email]" placeholder="Your Email Address" required />
     <input type="submit" value="Sign up" data-disable-with="Please wait" name="commit" />
   </form>

.. note:: Do not change ``name`` and form ``action`` attributes, otherwise functionality won’t work.
