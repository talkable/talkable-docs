.. _advanced_features/passing_custom_data:
.. include:: /partials/common.rst

.. meta::
   :description: The custom properties variable allows you to transfer any custom data to Talkable as a collection of key-value pairs.

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

Add the ``custom_properties`` collection in the ``authenticate_customer`` call of the Initialization script.

.. code-block:: javascript

  _talkableq.push(['authenticate_customer', {
    email: '',
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

**Loyalty script**

Add the ``custom_properties`` collection to the data passed in one of the following calls:

- ``show_loyalty``
- ``show_loyalty_redeem_widget``
- ``join_loyalty``
- ``register_loyalty_action``

If no ``custom_properties`` are passed explicitly, they will be taken from ``authenticate_customer`` params.

.. code-block:: javascript

  var _talkable_data = {
    email: '',
    custom_properties: {
      person_occupation: 'marketing',
      eye_color: 'brown'
    }
  };
  _talkableq.push(['show_loyalty', _talkable_data]);

.. note::

    The values you pass in the ``custom_properties`` have to be JSON Key-Value pairs themselves,
    meaning that complex nested data structures cannot be passed through.
    Property names (e.g. ``eye_color``) can contain lowercase letters, numbers and ``_`` only and cannot begin with a number.

.. raw:: html

   <h2>How to use</h2>

To access ``custom_properties`` in Talkable, use:

.. code-block:: liquid

   {{ advocate_custom_properties }}
   {{ friend_custom_properties }}
   {{ member_info.custom_properties }}

Key-Value pairs can be referenced calling the desired data key, such as:

.. code-block:: liquid

   {{ advocate_custom_properties.eye_color }}

.. note::

    Any ``custom_properties`` data passed through is tied to the |advocate|, |friend|, or |loyalty_member|.
    If Talkable receives a custom property that was previously defined for the user, the property gets overwritten with a new value.

.. container:: hidden

   .. toctree::
