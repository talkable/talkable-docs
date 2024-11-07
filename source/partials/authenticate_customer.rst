 .. code-block:: javascript

       window._talkableq.push(['authenticate_customer', {
         email: '',          // Required - Email of the customer. Example: 'customer@example.com'
         first_name: '',     // First name of the customer. Example: 'John'
         last_name: '',      // Last name of the customer. Example: 'Doe'
         traffic_source: '', // The source of the traffic driven to the campaign. Example: 'facebook'
         segment1: '',       // Segment 1: Represents a custom segment (e.g., location, age group, source channel, platform, gender, interests).
         segment2: '',       // Segment 2: Represents a custom segment (e.g., location, age group, source channel, platform, gender, interests).
         segment3: ''        // Segment 3: Represents a custom segment (e.g., location, age group, source channel, platform, gender, interests).
       }]);
