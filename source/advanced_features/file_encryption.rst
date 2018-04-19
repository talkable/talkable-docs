.. _advanced_features/file_encryption:
.. include:: /partials/common.rst

File Encryption
===============

For encrypting sensitive data when sending it through the Internet, you can use
PGP encryption. It is a public key encryption program that has become the most
popular standard for email encryption. PGP uses a private key that must be kept
secret and a public key that sender and receiver must share.

In the example below, we will use GPG (GNU Privacy Guard), which is a complete
and free implementation of the OpenPGP standard. If you do not have GPG setup
yet, here is a nice tutorial how to do it ("Set Up GPG Keys" section):
`How To Use GPG to Encrypt and Sign Messages`_.
Also, you can find a brief list of software that has PGP capability
`here <https://www.openpgp.org/software/>`_.

How To Import the Talkable Public Key
-------------------------------------

Before encrypting or decrypting you should import the Talkable public key.
Here is a command to do it:

.. code-block:: shell

   curl https://d2jjzw81hqbuqv.cloudfront.net/integration/talkable_public_key.asc | gpg --import

To check that the Talkable public key importing was done right, make sure that
next command is successful:

.. code-block:: shell

   gpg --list-keys dev@talkable.com

Encrypting
----------

To encrypt data, you can use the following syntax:

.. code-block:: shell

   gpg --encrypt --sign --armor -r dev@talkable.com name_of_file

This encrypts data using the Talkable public key and signs it with your own
private key to guarantee that it is coming from you. Encrypted file will have the
same name as the input one, but with an ``.asc`` extension. After this, you can
safely send the encrypted file to Talkable. Make sure to send us the public key
as well.

.. note::

   You should include a second ``"-r"`` recipient with your own email address if
   you want to be able to read the encrypted message.

Decrypting
----------

To decrypt a file simply call GPG on it:

.. code-block:: shell

   gpg file_name.asc

.. _How To Use GPG to Encrypt and Sign Messages: https://www.digitalocean.com/community/tutorials/how-to-use-gpg-to-encrypt-and-sign-messages#set-up-gpg-keys

.. container:: hidden

   .. toctree::
