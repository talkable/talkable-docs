.. _advanced_features/white_labeling/cloudflare:

.. meta::
   :description: Learn how to add DNS records in Cloudflare to enable white-labeling.

Adding DNS records in Cloudflare
================================

`Cloudflare docs <https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/#create-dns-records>`_

#. In your Cloudflare dashboard, select the site you want to manage (e.g. `example.com`).

#. Go to **DNS** → **Records** and click "Add record".

#. Select appropriate record type (might be NS, CNAME, MX, etc.).

#. In the "Name" field, enter only the **subdomain** part
   (e.g. `subdomain` if you want to add a record for `subdomain.example.com`).

#. Copy the DNS record value (or values) from the Talkable custom domain settings into the "Value" field.

#. Save the changes.
