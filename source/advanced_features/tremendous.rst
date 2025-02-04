.. _advanced_features/tremendous:
.. include:: /partials/common.rst

.. meta::
   :description: Reward advocates with gift cards provided by Tremendous.

Tremendous Integration
######################

Reward advocates with gift cards from various retailers provided by Tremendous.

Tremendous integration consists of several parts:

1. A campaign in Tremendous with the selected rewards for customers.

3. A "Tremendous" application installed from Talkable App Store. This application is responsible
   for storing API tokens, enabling Talkable to request gift cards from Tremendous and insert the generated
   claim links in the referral campaign theme.

2. A referral campaign in Talkable having the following attributes:

   - An Advocate Referral Incentive with "Tremendous" reward type

     .. image:: /_static/img/advanced_features/tremendous_incentive.png
        :width: 400
        :alt: Creating a Tremendous Advocate Referral incentive

   - A :ref:`"tremendous" Liquid filter<tremendous_filter>` used in Reward Paid Email Page.
      
     The filter generates a claim link within the specified Tremendous campaign.

     .. code-block:: html

       <!-- An example of the claim link leading to Tremendous -->
       <a href="{{ 'KBBYF5Q64BL4' | tremendous }}" target="_blank" title="{{ cta_text }}">
       {{ cta_text }}
       </a>

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.
