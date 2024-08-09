**HTML:**

.. code-block:: html

  <script src="//platform.linkedin.com/in.js" type="text/javascript"></script>
  <script type="IN/Share" data-url="{{ 'linkedin' | claim_url }}" data-onsuccess="fireOnLinkedInShare"></script>

**JS:**

.. code-block:: javascript

  function fireOnLinkedInShare() {
    Talkable.share_succeeded('linkedin');
  }
