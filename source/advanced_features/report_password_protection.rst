.. _advanced_features/report_password_protection:
.. include:: partials/common.rst

.. meta::
   :description: To protect sensitive information, all exported reports are password protected by default.

Report Password Protection
==========================

To protect sensitive information, all exported reports are password protected by default,
but you can disable this in your site settings.

How It Works
------------

After the report generation, the user will receive an email with a link to download encrypted
ZIP file and a password to unzip it.

.. image:: _static/img/password_protected_report_email.png
   :alt: Password Protected Report

To disable password protection in reports, you can turn off this option in the site settings:

.. image:: _static/img/password_protected_toggle.png
   :alt: Password Protected Toggle

.. note::

   Do not turn off password protection unnecessarily because this setting
   exists for protection reports data from hacker attacks.
