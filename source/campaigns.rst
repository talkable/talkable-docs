.. _campaigns:
.. include:: /partials/common.rst

Talkable Campaigns
##################

Talkable Campaign is based on interaction between ``Advocate`` and ``Friend``:

- Advocate: person, who shares an offer with his Friend(s)
- Friend: person, who is invited to participate in Campaign by Advocate

.. image:: /_static/img/basics/sharing-process.png
  :alt: Sharing process

Each step of this interaction has its own ``View`` so developer can easily
change every singe step and customize its appearance and functionality based on
campaign requirements.

We use |liquid| as a View template engine to provide a simple and quick way
to change campaign functionality and appearance.
|br| This choice was made mainly because of developers who are already
familiar with Liquid templating in Shopify.

To start editing Views simple visit ``Editor`` page from the Campaign dashboard.

Contents:

.. toctree::

   campaigns/views
   campaigns/tutorials
   campaigns/editor
   campaigns/designer
   campaigns/offers_expiration
