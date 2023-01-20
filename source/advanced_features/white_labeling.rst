.. _advanced_features/white_labeling:
.. include:: /partials/common.rst

.. meta::
   :description: Talkable can be white-labeled so that links and URLs will point to your domain. Nobody will know how you created your referral program.

White-labeling
==============

By default, Talkable runs campaigns on talkable.com domain and sends emails
from @p2p.talkable.com or @offers.talkable.com. That can be changed by configuring
a custom web and/or email domain so that links and emails
appear to be pointing to the store itself (e.g @share.puravida.com).

.. note::
   This is currently an Enterprise plan-only feature.
   Please |contact_us| for more information.

How to set up a custom domain
-----------------------------

Custom Email and Web domains can be configured in **Site Settings** → **Custom domains**.

#. Decide if you want custom **web domain**, **email domain**, or **both**.
   The domain names can match or be different. By default, if you select "Set up web domain",
   both web and email domains will be configured and will share the same domain name.
   This can be changed in the following step.

   .. image:: /_static/img/advanced_features/custom_domain_settings.png

#. Choose a **domain name** you want to use for white-labeling.

#. Choose if you want to **delegate** the custom domain to Talkable or want to keep control over its DNS settings.
   Read more about this in the section below.

#. If you clicked "Set up web domain" and you only want the web domain
   or you want different names for the web and email domains,
   change **"Domain consistency"** to "Web only".
   Otherwise, you will proceed to set up both web and email domains with the same name (which is recommended).
   If you clicked "Set up email domain", you can only configure email domain.

#. Once the domain configuration is confirmed, it is time to add **DNS records** to your parent domain accordingly.
   Read detailed instructions on how to add records for the most common DNS providers below.
   Please note that any DNS changes might take a while (sometimes more than a day) to become active.

#. After adding all the required DNS records, wait for a while for the records to become active.
   Click "Check DNS status" on Talkable custom domain settings to see the updated status of your domain.

.. image:: /_static/img/advanced_features/custom_domain_missing_records.png

Delegated VS Self-managed setup
...............................

Talkable offers two options for custom domain management:

* **Delegated** (recommended)
   This option allows adding fewer DNS records on your main domain.
   Once you set up the correct NS records, the rest of the configuration will be done by Talkable.
   However, it might not be available in every DNS provider.

   Required DNS records:

   * NS records (to delegate custom domain management to Talkable).

   Example:

   .. image:: /_static/img/advanced_features/custom_domain_ns.png

* **Self-managed**
   This option provides more granular control over DNS settings of the custom domain.
   It requires adding multiple DNS records to support the white-labeling and thus is more prone to errors
   if the records are omitted or misconfigured.

   Required DNS records for a web domain:

   * CNAME record (to point custom domain to Talkable)
   * CNAME record (to verify SSL certificate)

   Required DNS records for an email domain (see the picture below for reference):

   * CNAME record (to verify SSL certificate, number 3 on the picture)
   * CNAME record (to enable click tracking, 2)
   * MX records (direct mail to a mail server, 4 and 5)
   * TXT record (allows sending mail from Talkable on behalf of your domain, 1)

   Example of DNS records required for a self-managed custom email domain:

   .. image:: /_static/img/advanced_features/custom_email_domain_records.png

.. _adding-dns-records:

Adding DNS records
------------------

See detailed instructions on adding or modifying DNS records in the most common DNS management services below.

* :ref:`Add DNS records in AWS Route53 <advanced_features/white_labeling/aws_route53>`

* :ref:`Add DNS records in Shopify <advanced_features/white_labeling/shopify>`

* :ref:`Add DNS records in GoDaddy <advanced_features/white_labeling/godaddy>`

* :ref:`Add DNS records in Cloudflare <advanced_features/white_labeling/cloudflare>`

Email sending issues
....................

If the emails sent by Talkable go to spam, it is likely that there are issues with the DNS records setup,
namely `DMARC policies <https://www.mailgun.com/blog/deliverability/domain-reputation-and-dmarc/>`_.

Custom email domains in Talkable use a special DNS record called SPF record (Sender Policy Framework)
to mark Talkable as a valid sender of emails on behalf of your site.
So if your site uses a strict DMARC policy, emails sent from unverified domains will likely go to spam.

To avoid that, you either need to:

* ensure that the emails sent by Talkable are from a properly set up custom domain.

  Check that **"Customer service email"** in **All site settings** → **General** → **Notifications** has the same
  custom domain. For instance, if your custom domain is `subdomain.example.com`, and your customer service email is
  `cm@another_subdomain.example.com` or `cm@sub.subdomain.example.com`, there might be problems with sending.

* add Mailgun (a service that Talkable uses for sending emails) to a whitelist in your SPF record.

  This requires :ref:`adding-dns-records`. To look up your current SPF record, enter the domain of a "From" value
  of an email that went to spam in a `lookup service <https://dnslookup.online/spf.html>`_.

  Example of a TXT record value that allows Mailgun to send emails:

  .. code-block::

     v=spf1 include:mailgun.org include:_spf.google.com include:mail.zendesk.com include:_spf.salesforce.com ~all

.. container:: hidden

   .. toctree::

      white_labeling/aws_route53
      white_labeling/shopify
      white_labeling/godaddy
      white_labeling/cloudflare
