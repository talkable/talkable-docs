Asynchronous Integration
------------------------

You can trigger Talkable initialization whenever needed. For example, you can fire up Talkable on button click:

.. code-block:: html

  <button onclick="_curebitq.push(['register_affiliate', _curebit_affiliate_details]);">Init Talkable</button>

  <script>
    var _curebit_affiliate_details = {
      // all common Talkable config properties
      affiliate_member: {
        email: ''
      }
    };
  </script>

  <script src="//d2jjzw81hqbuqv.cloudfront.net/integration/curebit-1.0.min.js" type="text/javascript"></script>

|br|

Also, you can append Talkable ``iframe`` into your custom container. Add ``iframe`` object like so:

.. code-block:: html

  <div id="curebit-test"></div>

  <script>
    var _curebit_affiliate_details = {
      // ...
      // all common Curebit config properties
      affiliate_member: {
        email: ''
      },
      // ...
      iframe: {
        container: "curebit-test"
      }
    };
  </script>

  <script src="//d2jjzw81hqbuqv.cloudfront.net/integration/curebit-1.0.min.js" type="text/javascript"></script>

* You can pass any HTML attributes.
* Pass ``container`` option to set where you want Talkable iframe to be inserted (this is HTML ``id`` attribute value).

`Example standalone integration <http://jsbin.com/qawicuceqexe/2>`_

`Source for standalone integration <http://jsbin.com/qawicuceqexe/2/edit?html,js,output>`_
