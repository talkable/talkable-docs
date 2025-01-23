.. _advanced_features/white_labeling/shopify:

.. meta::
  :description: Learn how to add DNS records in Shopify to enable white-labeling.

Adding DNS records in Shopify
=============================

.. note::
  The instructions below use `subdomain.example.com` as an example of a custom domain where `example.com` is your domain.

.. note::
  This instruction applies to domains that are transferred to Shopify
  or registered there in the first place.
  Third-party domains connected to Shopify should be managed in respective domain registries.

For delegated setup,

#. In your Shopify admin, go to your primary domain settings
   (Settings → `Domains <https://shopify.com/admin/settings/domains>`_)

#. Add NS records listed in Talkable custom domain settings.

For self-managed setup of a custom web domain,

#. `Add a subdomain <https://help.shopify.com/en/manual/domains/add-a-domain/add-subdomains>`_ in Shopify.

#. `Edit <https://help.shopify.com/en/manual/domains/managing-domains/edit-dns-settings#edit-dns-record>`_
   the automatically created CNAME record for the subdomain to point to Talkable.
   See the value of the CNAME record in Talkable custom domain settings.
   Example: your-talkable-site-id.elb.talkable.com

#. Add another CNAME record to verify the SSL certificate created by Talkable.

For self-managed setup of a custom email domain,

#. `Add a subdomain <https://help.shopify.com/en/manual/domains/add-a-domain/add-subdomains>`_ in Shopify.

#. Add the CNAME, MX, and other records listed on Talkable custom domain settings to enable the email sending.
