.. _campaigns/editor/variables:
.. include:: /partials/common.rst

.. _editor_variables:

Variables
=========

Variables are used to show dynamic data like Campaign tag, Advocate info, etc.
|br|
All Variables are enclosed into ``{{ }}`` which means
`Liquid Output <http://docs.shopify.com/themes/liquid-basics/output>`_.

Each Campaign View has its own set of Variables located inside Editor
navigation:

.. image:: /_static/img/editor/vars-menu-item.png
  :alt: Variables: menu item

|br|

Each Variable is represented with Name, Liquid notation, Value:

.. image:: /_static/img/editor/vars-variable.png
  :alt: Variables: variable

* Name describes meaning of the Variable
* Notation explains how to write Variable inside Template/Styles editor area
* Value shows what this particular Variable results with (Value may be
  different between preview and production scenarious)

{{ advocate_info }}
-------------------

Personal data for Advocate. |br|
Available in: all Views. |br|
Type: ``Object``

.. container:: ptable

  ==================== ========================= =======================================
  Property             Value                     Description
  ==================== ========================= =======================================
  email                "affiliate@example.com"   Advocate email he is registered with
  first_name           "John"                    Advocate first name provided on Signup
  last_name            "Smith"                   Advocate last name provided on Signup
  gender               null | "male" | "female"  Advocate gender provided on Signup
  external_customer_id "1jsh17136"               Advocate unique ID passed by Merchnat
                                                 to :ref:`Curebit Integration
                                                 <ecommerce/custom>` as ``customer_id``
  sub_choice           "0" | "on"                Advocate custom parameter which can be
                                                 used to pass additional data to
                                                 Advocate Share Page
  purchases_count      0                         Advocate number of tracked store
                                                 purchases
  ==================== ========================= =======================================

