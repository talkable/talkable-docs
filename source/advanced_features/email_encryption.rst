.. _advanced_features/email_encryption:
.. include:: /partials/common.rst

Email Encryption
================

For additional security, it is possible to encrypt Advocate and Friend e-mails on back-end.
This can be done by using 2048-bit key `Talkable Public Key`_.
So, instead of sending email addresses in plain text, you can send them encrypted.

Passing email as a GET parameter to Standalone Campaign
-------------------------------------------------------

Also it's possible to pass encrypted email as a GET parameter (e.g. for CTA links that
point to standalone invite page). But to do that encrypted email should be **URL-encoded**.

Ruby Example
------------

.. code-block:: ruby

    require 'openssl'
    require 'base64'

    def key
      @key ||= begin
        key_content = File.read('talkable_public_key.pem')
        OpenSSL::PKey::RSA.new(key_content)
      end
    end

    def encode_email_for_talkable(email)
      encrypted_email = key.public_encrypt(email)
      Base64.strict_encode64(encrypted_email)
    end

    puts encode_email_for_talkable("email_to_encrypt@example.com")


Java Example
------------

This example uses `Bouncy Castle library`_ and has been tested on:

* bcprov-jdk15on-156.jar (Provider)
* bcpkix-jdk15on-156.jar (PKIX/CMS/EAC/PKCS/OCSP/TSP/OPENSSL)

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
        static class EmailEncryptor {
            private Cipher cipher;
            private Key publicKey;

            private void initPublicKey() throws IOException {
                PEMParser pemParser = new PEMParser(new FileReader("talkable_public_key.pem"));
                JcaPEMKeyConverter converter = new JcaPEMKeyConverter().setProvider("BC");
                SubjectPublicKeyInfo publicKeyInfo = (SubjectPublicKeyInfo) pemParser.readObject();
                publicKey = converter.getPublicKey(publicKeyInfo);
            }

            private void initCipher() throws GeneralSecurityException {
                cipher = Cipher.getInstance("RSA/ECB/PKCS1Padding", "BC");
                cipher.init(Cipher.ENCRYPT_MODE, publicKey);
            }

            public EmailEncryptor() throws IOException, GeneralSecurityException {
                initPublicKey();
                initCipher();
            }

            public String encryptEmail(String email) throws BadPaddingException, IllegalBlockSizeException {
                byte[] input = email.getBytes();
                byte[] cipherText = cipher.doFinal(input);
                byte[] encodedBytes = Base64.getEncoder().encode(cipherText);
                return new String(encodedBytes);
            }
        }

        static EmailEncryptor emailEncryptor;

        static {
            Security.addProvider(new BouncyCastleProvider());
            try {
                emailEncryptor = new EmailEncryptor();
            } catch (IOException | GeneralSecurityException e) {
                e.printStackTrace();
            }
        }

        public static String encryptEmail(String email) throws BadPaddingException, IllegalBlockSizeException {
            return emailEncryptor.encryptEmail(email);
        }

        public static void main(String[] args) throws Exception {
            String email = "encrypted_email@example.com";
            System.out.println(encryptEmail(email));
        }
    }

Front-end Part
--------------

Please modify the front-end using this pseudo code example:

.. code-block:: html

    <script>
     _talkableq.push(['authenticate_customer', {
       email: '<%= to_json(TalkableEmail.encrypt(current_user.email)) %>',
       first_name: '<%= to_json(current_user.first_name) %>',
       last_name: '<%= to_json(current_user.last_name) %>'
     }]);
    </script>

.. _Talkable Public Key: https://d2jjzw81hqbuqv.cloudfront.net/integration/talkable_public_key.pem
.. _Bouncy Castle Library: https://www.bouncycastle.org
.. _Bouncy Castle Latest Releases: https://www.bouncycastle.org/latest_releases.html
