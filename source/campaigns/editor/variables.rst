.. _campaigns/editor/variables:
.. include:: /partials/common.rst

.. _editor_variables:

Variables
---------

Each Curebit view has its own set of Variables which can be used in template.

Interpolations
..............

List of available interpolations is displayed in ``Variables`` editor menu.

View Setup Variables
....................

This is available for emails with multiple sending delays, see :ref:`editor_delayed_emails`.

``{{ view_setup.delay }}`` — number, contains exact value of current delay interval.

``{{ view_setup.delay_index }}`` — number, contains index of current delay interval, starting from ``0``.

.. note::

  You have email which has following delays: ``0, 24, 72``.

  When it is sent immediately both ``{{ view_setup.delay }}`` and ``{{ view_setup.delay_index }}`` will be equal ``0``.

  After 24 hours, when it is send second time, ``{{ view_setup.delay }}`` will be equal ``24`` and ``{{ view_setup.delay_index }}`` will be equal ``1``.

  And finally, after 48 hours more, ``{{ view_setup.delay }}`` will be equal ``72`` and ``{{ view_setup.delay_index }}`` will be equal ``2``.
