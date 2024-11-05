.. _advanced_features/facebook_login_share:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate Facebook Login & Share with your Talkable system for enhanced user authentication and social sharing. Follow our step-by-step guide to enable the app, configure Facebook App IDs, and streamline your login and sharing processes.

Facebook Login & Share
======================

Overview
--------

This documentation provides a comprehensive guide on integrating Facebook Login & Share into your Talkable system. By enabling this feature, users can sign in and share content directly via Facebook, enhancing engagement and simplifying the login process.

.. note::
   In case you don't have the Talkable Facebook Login & Share app installed, users can still log in and share via Facebook, but Talkable credentials will be used for authorization.

Prerequisites
-------------

Before you begin, ensure you have the following:

- Access to the Facebook Developer Console.
- A Facebook App ID (if you want to use a custom App ID).

Integration Steps
-----------------

1. **Install Facebook Login & Share App from Talkable Apps Store**
   - Navigate to the Talkable Apps Store.
   - Install the Facebook Login & Share app.
   - You will see an option to enter your custom Facebook App ID. If left blank, Talkable's default Facebook App ID will be used.

2. **Configure Facebook Login & Share Settings**
   - Go to the Facebook Login & Share app settings page.
   - Enter your custom Facebook App ID in the provided field.
   - You can find your App ID in the Facebook Developer Console.
   - Ensure the Valid OAuth Redirect URIs of your App ID include Talkable’s domain (`www.talkable.com`) and your custom web domain if set up.
   - Example App ID format: `1234567890`
   - Save the changes.

3. **Activate the Facebook Login & Share App**
   - Toggle the activation switch to enable the Facebook Login & Share app.
   - The app is now active, allowing users to log in and share content via Facebook.

Creating a Facebook App ID
--------------------------

1. **Access Facebook Developer Console**
   - Go to the [Facebook Developer Console](https://developers.facebook.com/).
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

Testing and Deployment
----------------------

- **Testing**: Use a test account to verify that Facebook Login & Share works correctly with your custom App ID.
- **Deployment**: Once testing is complete, ensure that all configurations are saved and the app is activated.

Additional Resources
--------------------

- Facebook Developer Console: https://developers.facebook.com/
- Facebook Login Documentation: https://developers.facebook.com/docs/facebook-login

.. note::
   For detailed examples and advanced usage, refer to the official Facebook Login documentation.