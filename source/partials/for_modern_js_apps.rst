Asynchronous Integration
------------------------

You can trigger Curebit initialization whenever needed. For example, you can fire up Curebit on button click:

.. code-block:: html

  <button onclick="_curebitq.push(['register_purchase', curebit_details]);">Init Curebit</button>

  <script>
    var curebit_details = {
      // ...
      // order_number: '100011',
      // all common Curebit config properties
      // ...
    };
  </script>

  <script src="//cdn.curebit.com/assets/api/all-0.6.js" type="text/javascript"></script>

|br|

Also, you can append Curebit ``iframe`` into your custom container. Add ``iframe`` object like so:

.. code-block:: html

  <div id="curebit-test"></div>

  <script>
    var curebit_details = {
      // ...
      // order_number: '100011',
      // all common Curebit config properties
      // ...
      iframe: {
        container: "curebit-test"
      }
    };
  </script>

  <script src="//cdn.curebit.com/assets/api/all-0.6.js" type="text/javascript"></script>

* You can pass any HTML attributes.
* Pass ``container`` option to set where you want Curebit iframe to be inserted (this is HTML ``id`` attribute value).

`Example integration <http://jsfiddle.net/p32R6/30>`_.

