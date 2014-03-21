.. code-block:: php

  <?php
    class ControllerCheckoutSuccess extends Controller {
      public function index() {
        if (isset($this->session->data['order_id')) {
          // Begin Curebit social referral tracking
          $this->session->data['curebit_order_id'] = $this->session->data['order_id'];
          // End Curebit social referral tracking

          $this->cart->clear();

  ...
