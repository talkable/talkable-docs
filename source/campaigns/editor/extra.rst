.. _campaigns/editor/extra:
.. include:: /partials/common.rst

Extra
-----

Allows to configure additional options for each view.

.. _editor_delayed_emails:

Delayed email sending
.....................

Editor provides an option to delay sending of some emails.

Delay email sending by setting value(s) inside Campaign Editor / Extra fields / Send email in (hours).

**Multiple delays**

Email views that support multiple sending delays: :ref:`notifier_offers_claim_view`.

Format of multiple delays: comma separated, e.g. ``0, 24, 72`` — email will be
sent immediately, then in 24 hours, and finally in 72 hours.

**Variables**

``{{ view_setup.delay }}`` — number, contains exact value of current delay interval.

``{{ view_setup.delay_index }}`` — number, contains index of current delay interval, starting from ``0``.

**Example**

Assuming you configured following delays: ``0, 24, 72``.

- When it is sent immediately both ``{{ view_setup.delay }}`` and ``{{ view_setup.delay_index }}`` will be equal ``0``.

- After 24 hours, when it is send second time, ``{{ view_setup.delay }}`` will be equal ``24`` and ``{{ view_setup.delay_index }}`` will be equal ``1``.

- And finally, after 48 hours more, ``{{ view_setup.delay }}`` will be equal ``72`` and ``{{ view_setup.delay_index }}`` will be equal ``2``.
