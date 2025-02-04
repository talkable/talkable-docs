.. _integration/custom_integration:
.. include:: /partials/common.rst

.. meta::
   :description: Learn all the ins and outs of integration. It’s easier than it seems.

Standard Integration
####################

.. raw:: html

   <h2 class="mts">Integration High Level Overview</h2>

1. Add the :ref:`Talkable Initialization Script <integration/custom/integration_components/initialization_script>`
   to your header or any template spanning every page.
   Surface variables for email and name if user is logged in.

2. Add the :ref:`Talkable Post Purchase Script <integration/custom/integration_components/post_purchase_script>`
   to your checkout confirmation page to pass purchase details
   to Talkable for all purchases.
   Surface purchase detail variables as described in more detail in :ref:`Integration Components <integration/custom/integration_components>`.

3. Create a new HTML page with standard header/footer to host the Talkable Standalone campaign
   which will be your Advocate Landing page where you can drive traffic from email and other onsite
   and offsite locations to refer friends. Copy & paste the Talkable container DIV element into the
   body as seen in :ref:`Integration Components <integration/custom/integration_components>`.

4. Create an additional new HTML page attached to your user accounts section (if you have one) behind
   login which is where referring Advocates can go to view referral details of all of the friends
   they’ve shared with. Copy & paste the Talkable container DIV element into the body as seen in
   :ref:`Integration Components <integration/custom/integration_components>`.

.. container:: hidden

  .. toctree::

     custom/overview


.. raw:: html

   <h2 class="mts">Contents:</h2>

.. grid:: 1 2 2 2

   .. grid-item::

      .. toctree::
         :maxdepth: 2 
      
         custom/integration_components
         verify
    
   .. grid-item::

      .. toctree::
         :maxdepth: 2 
        
         custom/validating_integration
         custom/cookies
         custom/questions   
   
   
