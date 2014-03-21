.. code-block:: html

  <!-- right_navigation //-->
  <?php require(DIR_WS_INCLUDES . 'column_right.php'); ?>
  <!-- right_navigation_eof //-->
      </table></td>
    </tr>
  </table>
  <!-- Begin Curebit integration code -->
  <?php
    include(DIR_WS_MODULES . 'order_total/curebit_checkout.php');
    if (class_exists('curebit_checkout')) {
      $curebit = new curebit_checkout();
      echo $curebit->getOutput((int)$customer_id);
    }
  ?>
  <!-- End Curebit integration code -->
  <!-- body_eof //-->

  <!-- footer //-->
  <?php require(DIR_WS_INCLUDES . 'footer.php'); ?>
  <!-- footer_eof //-->
