.. _advanced_features/passing_custom_data:
.. include:: /partials/common.rst

Pass Custom User Data
=====================

``custom_properties`` is a variable that allows you to pass custom data
to Talkable in the form of Key-Value pairs via integration.

``custom_properties`` has robust uses as you are able to define and pass
any key value pairs you wish.

The values you define for some key should be JSON Key-Value pairs themselves,
this means complex data structures can be passed through.

Any ``custom_properties`` data passed through is tied to the |advocate| or the |friend|,
that means there is only one instance of each field in
existence at any time: the most recently passed data.

All data associated with ``custom_properties`` is available for use
across all Campaign Views. Accessing this data beings by creating a variable
to store your custom_properties:

.. code-block:: liquid

   {% assign data = advocate_custom_properties %}

or

.. code-block:: liquid

   {% assign data = friend_custom_properties %}

Key Value pairs can be referenced through your newly created object by referencing
the value name such as:

.. code-block:: liquid

   {{ data.favorite_color }}

Defining ``custom_properties`` in your integration might look something like this:

.. code-block:: javascript

   var _talkable_data = {
     ...
     custom_properties: {
       person_occupation: 'marketing',
       height: '72 inches',
       eye_color: 'brown',
       birthday: '07/03/1983'
     }
     ...
   }

.. container:: hidden

   .. toctree::

