.. _advanced_features/facebook_login_share:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate Facebook Login & Share with your Talkable system for enhanced user authentication and social sharing. Follow our step-by-step guide to enable the app, configure Facebook App IDs, and streamline users login and sharing processes.

Facebook Login & Share
======================

Overview
--------

This documentation provides a comprehensive guide on connecting your Facebook App for Login & Share in Talkable.

.. note::
   In case you don't have the Talkable Facebook app installed, users can still log in and share via Facebook, but Talkable's default Facebook app will be used.

Prerequisites
-------------

Before you begin, ensure you have the following:

- Access to the Facebook Developer Console.
- A Facebook App ID.

Integration Steps
-----------------

1. **Install Facebook App from Talkable Apps Store**

   - Navigate to the Talkable Apps Store.
   - Install the Facebook app.
   - Enter your custom Facebook App ID in the provided field. If left blank, Talkable's default Facebook App ID will be used.
   - You can find your App ID in the Facebook Developer Console.
   - Ensure the Valid OAuth Redirect URIs of your App ID include Talkable’s domain (`www.talkable.com`) and your custom web domain if set up.
   - Example App ID format: `1234567890`
   - Save the changes.

2. **Activate the Facebook Login & Share App**

   - Toggle the activation switch to enable the Facebook Login & Share app.
   - The app is now active, allowing users to log in and share content via Facebook using your Facebook App instead of the default Talkable Facebook App.

Creating a Facebook App ID
--------------------------

1. **Access Facebook Developer Console**

   - Go to the `Facebook Developer Console <https://developers.facebook.com/>`_.
   - Create a new project or select an existing project.

2. **Configure OAuth Consent Screen**

   - Navigate to the App settings.
   - Fill in the necessary details and save the configuration.

3. **Create App ID**

   - Go to the App Dashboard.
   - Click on "Create App" and select the appropriate permissions for your app.
   - Add Valid OAuth Redirect URIs, including:

     - `https://www.talkable.com`
     - Your custom domain, if applicable.
   
   - Save and copy the generated App ID.

Error Handling
--------------

Common errors and how to handle them:

- **Invalid App ID**: Ensure the App ID is correctly entered and is active in the Facebook Developer Console.
- **Authorization Errors**: Verify that the Valid OAuth Redirect URIs include the necessary domains.
- **Network Issues**: Retry the request or check your network connection.

Additional Resources
--------------------

- Facebook Developer Console: https://developers.facebook.com/
- Facebook Login Documentation: https://developers.facebook.com/docs/facebook-login

.. note:: For detailed examples and advanced usage, refer to the official Facebook documentation.

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://talkable.com/lets-talk-referral>`_.
