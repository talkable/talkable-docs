Asynchronous Integration
------------------------

You can trigger Talkable initialization whenever needed. For example, you can fire up Talkable on button click:

.. code-block:: html

   <button onclick="_talkableq.push(['register_purchase', curebit_details]);">Init Talkable</button>

   <script>
     var curebit_details = {
       // ...
       // order_number: '100011',
       // all common Talkable config properties
       // ...
     };
   </script>

   <script src="//d2jjzw81hqbuqv.cloudfront.net/integration/talkable-1.0.min.js" type="text/javascript"></script>

|br|

Also, you can append Talkable ``iframe`` into your custom container. Add ``iframe`` object like so:

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

   <script src="//d2jjzw81hqbuqv.cloudfront.net/integration/talkable-1.0.min.js" type="text/javascript"></script>

* You can pass any HTML attributes.
* Pass ``container`` option to set where you want Talkable iframe to be inserted (this is HTML ``id`` attribute value).

`Example post-purchase integration <http://jsbin.com/doqihasivuce/4>`_

`Source for post-purchase integration <http://jsbin.com/doqihasivuce/4/edit?html,js,output>`_
