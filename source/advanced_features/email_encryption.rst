.. _advanced_features/email_encryption:
.. include:: /partials/common.rst

Email Encryption
================

For additional security, it is possible to encrypt Advocate and Friend e-mails on back-end.
This can be done by using `Talkable Public Key`_.
So, instead of sending email addresses in plain text, you can send them encrypted.

Ruby Example
------------

.. code-block:: ruby

    require 'openssl'
    require 'base64'

    key_content = File.read('talkable_public_key.pem')
    key = OpenSSL::PKey::RSA.new(key_content)
    encrypted_email = key.public_encrypt("email_to_encrypt@example.com")
    puts Base64.strict_encode64(encrypted_email)


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

        public static void main(String[] args) throws Exception {
            Security.addProvider(new BouncyCastleProvider());
            EmailEncryptor emailEncryptor = new EmailEncryptor();
            String email = "email_to_encrypt@example.com";
            String encryptedEmail = emailEncryptor.encryptEmail(email);
            System.out.println(encryptedEmail);
        }
    }

.. _Talkable Public Key: https://d2jjzw81hqbuqv.cloudfront.net/integration/talkable_public_key.pem
.. _Bouncy Castle Library: https://www.bouncycastle.org
.. _Bouncy Castle Latest Releases: https://www.bouncycastle.org/latest_releases.html
