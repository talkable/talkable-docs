.. code-block:: html

    <div class="buttonSet">
      <span class="buttonAction"><?php echo tep_draw_button(IMAGE_BUTTON_CONTINUE, 'triangle-1-e', null, 'primary'); ?></span>
    </div>
  </div>

  </form>

  <!-- Begin Curebit integration code -->
  <?php
    include(DIR_WS_MODULES . 'order_total/curebit_checkout.php');
    if (class_exists('curebit_checkout')) {
      $curebit = new curebit_checkout();
      echo $curebit->getOutput((int)$customer_id);
    }
  ?>
  <!-- End Curebit integration code -->

  <?php
    require(DIR_WS_INCLUDES . 'template_bottom.php');
    require(DIR_WS_INCLUDES . 'application_bottom.php');
  ?>
