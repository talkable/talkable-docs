Asynchronous Integration
------------------------

You can trigger Talkable initialization whenever needed. For example, you can fire up Talkable on button click:

.. code-block:: html

   <button onclick="_talkableq.push(['register_affiliate', _talkable_affiliate_details]);">Init Talkable</button>

   <script>
     var _talkable_affiliate_details = {
       // all common Talkable config properties
       affiliate_member: {
         email: ''
       }
     };
   </script>

   <script src="|integration_url|" type="text/javascript"></script>

|br|

Also, you can append Talkable ``iframe`` into your custom container. Add ``iframe`` object like so:

.. code-block:: html

   <div id="talkable-test"></div>

   <script>
     var _talkable_affiliate_details = {
       // ...
       // all common Talkable config properties
       affiliate_member: {
         email: ''
       },
       // ...
       iframe: {
         container: "talkable-test"
       }
     };
   </script>

   <script src="|integration_url|" type="text/javascript"></script>

* You can pass any HTML attributes.
* Pass ``container`` option to set where you want Talkable iframe to be inserted (this is HTML ``id`` attribute value).

`Example standalone integration <http://jsbin.com/qawicuceqexe/2>`_

`Source for standalone integration <http://jsbin.com/qawicuceqexe/2/edit?html,js,output>`_
