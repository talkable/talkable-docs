.. _campaigns/editor/extra:
.. include:: /partials/common.rst

Extra
-----

Allows to configure additional options for each view.

.. _editor_delayed_emails:

Delayed email sending
...................

Editor provides an option to delay sending of some emails.

Delay email sending by specifying value of ``Send email in (hours)``.

**Multiple delays**

Email views that support multiple sending delays: :ref:`notifier_offers_claim_view`.

Format of multiple delays: comma separated, e.g. ``0, 24, 72`` — email will be
sent immediately, then in 24 hours, and finally in 72 hours.

See :ref:`editor_variables` page for details how to use delay variables in order to
differentiate email template for specific delay.
