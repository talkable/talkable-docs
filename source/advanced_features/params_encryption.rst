.. _advanced_features/params_encryption:
.. include:: /partials/common.rst

.. meta::
   :description: It is possible to encrypt Advocate, Friend, and Loyalty member emails on back-end if you want to provide additional security.

Params Encryption
=================

For additional security, it is possible to encrypt |advocate|, |friend|, and |loyalty_member| email,
as well as :ref:`Custom User Data <advanced_features/passing_custom_data>` on back-end.
This can be done by using 2048-bit key generated by Talkable for your site.
So, instead of sending params in plain text, you can send them encrypted.

Site public encryption key
--------------------------

To get your unique site public encryption key, go to **All Site Settings → Integrations → JS integration → Public encryption key**.

Passing email as a GET parameter to Standalone Campaign
-------------------------------------------------------

Also it’s possible to pass encrypted email as a GET parameter (e.g. for CTA links that
point to standalone invite page). But to do that encrypted email should be **URL-encoded**.

.. note::

   It’s recommended to use `Optimal Asymmetric Encryption Padding (OAEP)`_ padding scheme together with RSA encryption.

Ruby Example
------------

.. code-block:: ruby

   require 'openssl'
   require 'base64'

   def key
     @key ||= begin
       key_content = File.read('talkable_your_site_slug_public_key.pem')
       OpenSSL::PKey::RSA.new(key_content)
     end
   end

   def encode_param_for_talkable(param)
     encrypted_param = key.public_encrypt(param, OpenSSL::PKey::RSA::PKCS1_OAEP_PADDING)
     Base64.strict_encode64(encrypted_param)
   end

   puts encode_param_for_talkable("email_to_encrypt@example.com")

Java Example
------------

This example uses `Bouncy Castle library`_ and has been tested on:

* bcprov-jdk18on-1.78.1.jar (Provider)
* bcpkix-jdk18on-1.78.1.jar (PKIX/CMS/EAC/PKCS/OCSP/TSP/OPENSSL)

that can be downloaded from `Bouncy Castle Latest Releases`_.

.. note::

   Please note that loading a Security Provider and a key into memory takes more time than encrypting.
   So it is recommended to store the key in memory instead of loading it each time to avoid performance overhead.

.. code-block:: java

   import javax.crypto.BadPaddingException;
   import javax.crypto.Cipher;
   import javax.crypto.IllegalBlockSizeException;
   import java.io.FileReader;
   import java.io.IOException;
   import java.security.*;
   import java.util.Base64;

   import org.bouncycastle.asn1.x509.SubjectPublicKeyInfo;
   import org.bouncycastle.jce.provider.BouncyCastleProvider;
   import org.bouncycastle.openssl.PEMParser;
   import org.bouncycastle.openssl.jcajce.JcaPEMKeyConverter;

   public class EncryptionDemo {
       static class ParamEncryptor {
           private Cipher cipher;
           private Key publicKey;

           private void initPublicKey() throws IOException {
               PEMParser pemParser = new PEMParser(new FileReader("talkable_your_site_slug_public_key.pem"));
               JcaPEMKeyConverter converter = new JcaPEMKeyConverter().setProvider("BC");
               SubjectPublicKeyInfo publicKeyInfo = (SubjectPublicKeyInfo) pemParser.readObject();
               publicKey = converter.getPublicKey(publicKeyInfo);
           }

           private void initCipher() throws GeneralSecurityException {
               cipher = Cipher.getInstance("RSA/ECB/OAEPPadding", "BC");
               cipher.init(Cipher.ENCRYPT_MODE, publicKey);
           }

           public ParamEncryptor() throws IOException, GeneralSecurityException {
               initPublicKey();
               initCipher();
           }

           public String encryptParam(String param) throws BadPaddingException, IllegalBlockSizeException {
               byte[] input = param.getBytes();
               byte[] cipherText = cipher.doFinal(input);
               byte[] encodedBytes = Base64.getEncoder().encode(cipherText);
               return new String(encodedBytes);
           }
       }

       static ParamEncryptor paramEncryptor;

       static {
           Security.addProvider(new BouncyCastleProvider());
           try {
               paramEncryptor = new ParamEncryptor();
           } catch (IOException | GeneralSecurityException e) {
               e.printStackTrace();
           }
       }

       public static String encryptParam(String param) throws BadPaddingException, IllegalBlockSizeException {
           return paramEncryptor.encryptParam(param);
       }

       public static void main(String[] args) throws Exception {
           String email = "email_to_encrypt@example.com";
           System.out.println(encryptParam(email));
       }
   }

Node.js Example
---------------

.. code-block:: js

   const fs = require('fs');
   const crypto = require('crypto');

   // Read the public key from file
   const publicKey = fs.readFileSync('talkable_your_site_slug_public_key.pem', 'utf8');

   const encryptData = (data) => {
     const encryptedData = crypto.publicEncrypt(
       {
         key: publicKey,
         padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
         oaepHash: 'sha1',
       },
       Buffer.from(data)
     );
     return encryptedData.toString('base64');
   };

   // Example usage
   const encryptedEmail = encryptData('email_to_encrypt@example.com');
   console.log('Encrypted email:', encryptedEmail);

Front-end Part
--------------

.. important::
   Do not use params encryption for :ref:`Talkable backend API <api_v2/origins>`.

   Params encryption is only for JS integration.

Please modify the front-end using this pseudo code example:

.. code-block:: html

   <script>
     _talkableq.push(['authenticate_customer', {
       email: '<%= to_json(TalkableEncryptionService.encrypt(current_user.email)) %>',
       phone_number: '<%= to_json(TalkableEncryptionService.encrypt(current_user.phone_number)) %>',
       first_name: '<%= to_json(current_user.first_name) %>',
       last_name: '<%= to_json(current_user.last_name) %>',
       person_custom_properties: {
         secret: '<%= to_json(TalkableEncryptionService.encrypt(current_user.secret)) %>'
       }
     }]);
   </script>

.. _Talkable Public Key: https://d2jjzw81hqbuqv.cloudfront.net/integration/talkable_public_key.pem
.. _Bouncy Castle Library: https://www.bouncycastle.org
.. _Bouncy Castle Latest Releases: https://www.bouncycastle.org/download/bouncy-castle-java/#latest
.. _Optimal Asymmetric Encryption Padding (OAEP): https://en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding
