**HTML:**

.. code-block:: html

  <span class="js-linkedin-button-holder" style="display: none;">
    <script src="//platform.linkedin.com/in.js" type="text/javascript"></script>
    <script type="IN/Share" data-url="{{ 'linkedin' | claim_url }}" data-onsuccess="fireOnLinkedInShare"></script>
  </span>

Remember to wrap LI scripts into an ``js-linkedin-button-holder``
container which is hidden by default not to show LinkedIn custom button
until it is loaded.

**JS:**

.. code-block:: javascript

  function fireOnLinkedInShare() {
    Talkable.share_succeeded('linkedin');
  }

  function configureShareOnLinkedIn(params) {
    $('.IN-widget').attr('style', '').find('a').addClass(params.className);
    $('.IN-widget').find('span').each(function(i, element) {
      $(element).attr({style: '', id: ''});
      if ($(element).text() === 'in') {
        $(element).remove();
      } else if ($(element).text() === 'Share') {
        $(element).text(params.text);
      }
    });
  }

  var initLinkedInShareButton = setInterval(function() {
    if ($('span').hasClass('IN-widget')) {
      clearInterval(initLinkedInShareButton);
      $('.js-linkedin-button-holder').fadeIn(300);
      configureShareOnLinkedIn({
        className: 'btn btn-linkedin', // Button class
        text: 'LinkedIn' // Button text
      });
    }
  }, 500);

1. ``fireOnLinkedInShare`` — triggering this method is required to make
   Talkable visits tracking work.
2. ``initLinkedInShareButton`` — checks for LI button to load and then
   show its container ``js-linkedin-button-holder`` and trigger
   ``configureShareOnLinkedIn``.
3. ``configureShareOnLinkedIn`` — strips all unnecessary styles and
   ``id`` attributes from all LI button children nodes and allows to
   change ``class`` attribute and button text by passing an object.
