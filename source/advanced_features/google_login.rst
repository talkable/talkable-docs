.. _advanced_features/google_login:
.. include:: /partials/common.rst

.. meta::
  :description: Integrate Google Login with your Talkable system for secure and seamless user authentication. Follow our step-by-step guide to enable the app, configure custom Google Client IDs, and enhance your login processes.

Google Login
============

Overview
--------

This documentation provides a comprehensive guide on integrating the Google Sign-In app into your Talkable system. By enabling this app, users can sign in using their Google accounts, enhancing security and reducing login friction.

.. note::

In case you don't have the Talkable Google Sign-In app installed, users can still log in via Google in your Campaign, but Talkable credentials will be used for the OAuth flow.

Prerequisites
-------------

Before you begin, ensure you have the following:

- Access to Google API Console.
- A Google API Client ID (if you want to use a custom Client ID).

Integration Steps
-----------------

1. **Install Google Sign-In App from Talkable Apps Store**
   - Navigate to the Talkable Apps Store.
   - Install the Google Sign-In app.
   - You will see an option to enter your custom Google Client ID. If left blank, Talkable's default Google identifier will be used.

2. **Configure Google Sign-In Settings**
   - Go to the Google Sign-In app settings page.
   - Enter your custom Google Client ID in the provided field.
     - You can find your Client ID in the Google API Console.
     - Ensure the Authorized JavaScript origins of your Client ID include Talkable's domain (`www.talkable.com`) and your custom web domain if set up.
   - Example Client ID format: `123.apps.googleusercontent.com`
   - Save the changes.

3. **Activate the Google Sign-In App**
   - Toggle the activation switch to enable the Google Sign-In app.
   - The app is now active, and users can use their Google accounts to sign in.

Creating a Google API Client ID
-------------------------------

1. **Access Google API Console**
   - Go to the [Google API Console](https://console.developers.google.com/).
   - Create a new project or select an existing project.

2. **Configure OAuth Consent Screen**
   - Navigate to the OAuth consent screen configuration.
   - Fill in the necessary details and save the configuration.

3. **Create OAuth 2.0 Client ID**
   - Go to the Credentials page.
   - Click on "Create Credentials" and select "OAuth 2.0 Client ID".
   - Configure the application type as "Web application".
   - Add Authorized JavaScript origins, including:
     - `https://www.talkable.com`
     - Your custom domain, if applicable.
   - Save and copy the generated Client ID.

Error Handling
--------------

Common errors and how to handle them:

- **Invalid Client ID**: Ensure the Client ID is correctly entered and is active in the Google API Console.
- **Authorization Errors**: Verify that the Authorized JavaScript origins include the necessary domains.
- **Network Issues**: Retry the request or check your network connection.

Testing and Deployment
----------------------

- **Testing**: Use a test account to verify that the Google Sign-In works correctly with your custom Client ID.
- **Deployment**: Once testing is complete, ensure that all configurations are saved and the app is activated.

Additional Resources
--------------------

- Google API Console: https://console.developers.google.com/
- OAuth 2.0 Documentation: https://developers.google.com/identity/protocols/oauth2

.. note::
   For detailed examples and advanced usage, refer to the official Google OAuth 2.0 documentation.

