.. _custom_integration/chatgpt_text_generation:
.. include:: /partials/common.rst

.. meta::
   :description: Integrate ChatGPT with your Talkable system to generate AI-driven text for various use cases like AD notes.

ChatGPT AI Text Generation
==========================

With this integration, Talkable utilizes OpenAI's ChatGPT API to generate custom AI-driven text for AD notes or other campaign-specific purposes.

**Endpoint for ChatGPT AI Text Generation:**
|br|
`<https://esp.talkable.com/chat-gpt/generate>`_

**Params configuration for ChatGPT AI Text Generation**

Documentation: [OpenAI API Reference](https://platform.openai.com/docs/api-reference/chat/create)

.. code-block:: javascript

   const params = {
     site: "*********",            // required
     email: "{{ person.email }}",  // required
     api_key: "************",      // required
     event_number: "{{ origin.event_number }}-complete", // optional, default `generate_text_complete`
     openai: {
       messages: [{
         role: "user",
         content: "There once was a user named {{ person.first_name }}, who bought a {{ origin.custom_field }}, now create a humorous verse with this information."
       }], // required
       api_key: "************",    // required
       model: "gpt-3.5-turbo",    // optional
       max_tokens: 150             // optional
     },
     usage_limit: {                // optional, if added - all params required
       amount: "3",                // requests amount
       duration_in_seconds: "3600",// during this time we count amount or requests
       // service variables, don't change it
       start_time: "{% assign ct = 'now' | date: '%s' %}{{ person.custom_properties.__start_time | default: ct }}",
       current_time: "{{ 'now' | date: '%s' }}",
       current_usage_amount: "{{ person.custom_properties.__current_usage_amount | default: 0 }}"
     },
     trigger_criteria: "{% if origin.event_category == 'generate_text' %}true{% endif %}"
   };

Support
-------
- All webhooks
- Custom App

**Contact us**

Interested in setting this up? Contact your CSM or get in touch `here <https://lp.talkable.com/lets-talk-referral>`_.