.. _advanced_features/sheerid:
.. include:: /partials/common.rst

.. meta::
  :description: Learn how to seamlessly integrate the SheerID app into your Talkable system. Follow our step-by-step guide for installation, API integration, and error handling to enhance your verification processes and improve campaign management.

SheerID Integration
=======================

Overview
--------

This documentation provides a comprehensive guide on integrating the SheerID app into your Talkable system.

Prerequisites
-------------

Before you begin, ensure you have the following:

- Access to SheerID Developer Portal.
- SheerID Access Token provided by SheerID team or customer’s team.
- Basic knowledge of RESTful APIs and JSON.

Integration Steps
-----------------

1. **Install SheerID App from Talkable Apps Store**
   - Navigate to the Talkable Apps Store.
   - Install the SheerID app.
   - During installation, you will be prompted to enter a SheerID Access Token.
     - The Access Token should be provided by the SheerID team or your customer’s team.
   - The app works as a SheerID features enabler and opens app SheerID fields in Campaign Rules.

2. **Connect Talkable Campaign to SheerID Program**
   - Go to the Talkable Campaign settings.
   - Locate the SheerID integration section.
   - Fill in the `SheerID Program ID` with the appropriate value provided by SheerID.
   - Save the settings.

API Integration (Optional)
--------------------------

For additional custom integrations using SheerID API:

1. **Get API Keys**
   - Log in to the SheerID Developer Portal.
   - Navigate to the API keys section.
   - Copy the sandbox and production API keys.

2. **Set Up API Requests**
   - Base URL: `https://services.sheerid.com/rest/v2/`
   - Authentication: Use your API key as a Bearer token in the Authorization header.

3. **Create a Verification Request**
   - Endpoint: `/verification`
   - Method: `POST`
   - Headers:
     - `Content-Type: application/json`
     - `Authorization: Bearer <YOUR_API_KEY>`
   - Request Body Example:
     ```json
     {
       "countryCode": "US",
       "programId": "<YOUR_PROGRAM_ID>",
       "email": "user@example.com",
       "firstName": "John",
       "lastName": "Doe"
     }
     ```

4. **Handle Verification Responses**
   - On a successful request, you will receive a response with a `requestId` that you can use to check the status of the verification.
   - Example Response:
     ```json
     {
       "requestId": "1234567890abcdef",
       "status": "PENDING",
       "message": "Verification in progress"
     }
     ```

5. **Check Verification Status**
   - Endpoint: `/verification/{requestId}`
   - Method: `GET`
   - Headers:
     - `Authorization: Bearer <YOUR_API_KEY>`
   - Example Response:
     ```json
     {
       "requestId": "1234567890abcdef",
       "status": "APPROVED",
       "message": "Verification successful"
     }
     ```

Error Handling
--------------

Common errors and how to handle them:

- **Invalid API Key**: Ensure your API key is correct and active.
- **Request Validation Errors**: Check the request body for missing or invalid fields.
- **Network Issues**: Retry the request or check your network connection.

Testing and Deployment
----------------------

- **Sandbox Environment**: Use the sandbox API key for testing. The base URL for sandbox is `https://sandbox.sheerid.com/rest/v2/`.
- **Production Environment**: Once testing is complete, switch to the production API key and base URL.

Additional Resources
--------------------

- SheerID Developer Portal: https://developer.sheerid.com/
- API Documentation: https://developer.sheerid.com/docs/

.. note::
   For detailed examples and advanced usage, refer to the official SheerID API documentation.
