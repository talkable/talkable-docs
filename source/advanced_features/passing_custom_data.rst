.. _advanced_features/passing_custom_data:
.. include:: /partials/common.rst

Pass Custom User Data
=====================

The ``custom_properties`` variable allows you to pass any custom data
to Talkable as a collection of Key-Value pairs.
Those can be used for various segmentation purposes, since join criteria and incentive criteria are capable of using the ones in conditions.

All data associated with ``custom_properties`` is available for use
across all Campaign Views.

.. raw:: html

   <h2>How to set</h2>

**Initialization script**

Add the ``custom_properties`` collection in the ``register_affiliate`` call of the Initialization script.

.. code-block:: javascript

  _talkableq.push(['register_affiliate', {
    custom_properties: {
      person_occupation: 'marketing',
      eye_color: 'brown'
    }
  }]);

**Post-purchase script**

Add the ``custom_properties`` collection to the data passed in the ``register_purchase`` call. It should be nested the same as ``purchase`` collection.

.. code-block:: javascript

  var _talkable_data = {
    purchase: {
      order_number: '',
      subtotal: '',
    },
    custom_properties: {
      person_occupation: 'marketing',
      eye_color: 'brown'
    }
  };
  _talkableq.push(['register_purchase', _talkable_data]);


.. note::

    The values you pass in the ``custom_properties`` have to be JSON Key-Value pairs themselves,
    meaning that complex nested data structures can not be passed through.

.. raw:: html

   <h2>How to use</h2>

To access ``custom_properties`` in Talkable, use:

.. code-block:: liquid

   {{ advocate_custom_properties }}
   {{ friend_custom_properties }}

Key-Value pairs can be referenced calling the desired data key, such as:

.. code-block:: liquid

   {{ advocate_custom_properties.eye_color }}

.. note::

    Any ``custom_properties`` data passed through is tied to the |advocate| or the |friend|.
    If Talkable receives a custom property that was previously defined for the user, the property gets overwritten with a new value.

.. container:: hidden

   .. toctree::
