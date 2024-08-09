**HTML:**

.. code-block:: html

  <a class="cs_import" href="#">Import contacts</a>
  <script type="text/javascript" src="//api.cloudsponge.com/address_books.js"></script>
  <script type="text/javascript">
    var csPageOptions = {
      "include": ["email"],
      "locale": "english",
      "domain_key": "PHAUB8N7PNYWP555F7YB",
      "textarea_id": "email_recipients_list"
    };
  </script>

1. ``domain_key`` — CloudSponge account (Talkable by default)
2. ``textarea_id`` — ID attribute to populate data to
