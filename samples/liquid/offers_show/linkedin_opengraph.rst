Enable separate Linkedin share wording (Open Graph title and message).

.. code-block:: liquid

  {% if user_agent contains "LinkedInBot" %}
  Special offer title for Linkedin friends
  {% else %}
  Special offer title for Facebook friends
  {% endif %}
