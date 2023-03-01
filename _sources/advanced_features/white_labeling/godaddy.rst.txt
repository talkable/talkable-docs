.. _advanced_features/white_labeling/godaddy:

.. meta::
   :description: Learn how to add DNS records in GoDaddy to enable white-labeling.

Adding DNS records in GoDaddy
=============================

.. note::

   The instructions below use `subdomain.example.com` as an example of a custom domain where `example.com` is your domain.

`GoDaddy docs <https://www.godaddy.com/help/manage-dns-records-680>`_

.. note::
   This instruction applies to domains that have GoDaddy name servers.
   If you purchased a GoDaddy domain, but use other service's name servers,
   you should add DNS records in the name server account.

#. Click **My Account** → **Domains**.

#. Pick a domain that you want to manage, click three dots and click "Manage DNS".

#. Click "Add" to add a new DNS record, or "Edit" to update an already existing one.
   Pay attention to the "Name" column. You want to make sure that you edit the correct
   record. The "Name" should only include a subdomain part, so if you want to edit
   `subdomain.example.com`, look for `subdomain` in the "Name".

#. In the editing window, select appropriate record type (might be NS, CNAME, MX, etc.).

#. In the "Name" field, enter only the **subdomain** part
   (e.g. `subdomain` if you want to add a record for `subdomain.example.com`).

#. Copy the DNS record value (or values) from the Talkable custom domain settings into the "Value" field.
