.. _advanced_features/tango:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate Tango with your Talkable system to generate gift claim links and manage campaign-specific rewards.

Tango Integration
#################

This documentation provides a guide on integrating the Tango rewards with your Talkable system.
By enabling this feature, you can generate gift claim links for users and customize reward amounts based on campaign settings.

Tango integration consists of several parts:

1. A Reward Link reward option in Tango portal.

3. A Tango application installed from Talkable App Store. This application is responsible
   for storing all the necessary data required for Talkable to request gift cards from Tango and insert the generated
   claim links in the referral campaign theme.

2. A referral campaign in Talkable having the following attributes:

   - An Advocate Referral Incentive with "Tango" reward type

   - A :ref:`"tango" Liquid filter <liquid_filter_tango>` used in Reward Paid Email Page.
      
     The filter generates a claim link for the specified reward in Tango.

     .. code-block:: html

        <!-- An example of the claim link leading to Tango -->
        <a href="{{ 'U957978' | tango: amount: 10 }}" target="_blank" title="{{ cta_text }}">
          {{ cta_text }}
        </a>

How to find the reward ID (UTID)
................................

To use the `tango` Liquid filter, you will need to obtain the reward ID (called UTID) in the Tango portal:

1. In the "Send rewards" portal section, select and click the Reward Link you intend to use to reward advocates in Talkable.

2. On the reward details page, click "View all reward details".

   .. image:: /_static/img/advanced_features/tango_open_reward_details.png
      :scale: 50%
      :alt: Open Tango reward details

3. Copy the "UTID" value and use it with the `tango` filter in the Talkable campaign theme.

   .. image:: /_static/img/advanced_features/tango_copy_utid.png
      :scale: 50%
      :alt: Copy Tango UTID

   .. note::
      
      Make sure to only copy the value of UTID, i.e "U957978".

.. include:: /partials/contact_us.rst
