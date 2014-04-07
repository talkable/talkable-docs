.. raw:: html

  <h2>Asynchronous Integration</h2>

You can trigger Curebit initialization whenever needed like so:

.. code-block:: html

  <button onclick="_curebitq.push(['register_purchase', _curebit_order_details]);">Init Curebit</button>

Note ``iframe`` object:

* You can pass any HTML attributes
* Pass ``container`` option to set where you want Curebit iframe to be inserted

`Example integration <http://jsfiddle.net/p32R6/30>`_.

