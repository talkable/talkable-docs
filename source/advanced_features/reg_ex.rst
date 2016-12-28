.. _advanced_features/reg_ex:
.. include:: /partials/common.rst

Using Regular Expressions
=========================

Talkable allows you to use regular expressions (regex for short) inside Campaign Placement options so that you can span
multiple URLs instead of an exact one.
Only Talkable admins are able to use this as an option.
In order to switch "Shown on" or "Hidden on" field into Regex mode turn on the appropriate checkbox.
Keep in mind that you don't need to escape **/** with backslash, those are already escaped for you.
The rest of the queries need to be backslashed.
It is recommended to run some checks when coding up Regex criteria: https://regex101.com.
Here is an example of a URL: `http://www.google.com/test`, you can replace it with your site URL and add your own path(s).

It is not recommended to hardcode your site URL like `http://site.com` because you might also support `https` protocol as
well as `www` as a part of your domain, all combinations should work.

Examples
--------

1. Show/suppress Campaigns on URLs that start with **/cart**, i.e.: `http://site.com/cart`, |br| `http://site.com/cart/checkout`,
   but not `http://site.com/test/cart`.

   Here is the Regex criteria:

   .. code-block:: text

     https?://([\w\-\d]+\.)+[\w\-\d]+/cart

2. Show/suppress Campaigns on URLs that contains **/share**, i.e.: `http://site.com/pages/share`, `http://site.com/share`,
   `http://site.com/pages/share/product`, any URL that contains `/share`.

   Here is the Regex criteria:

   .. code-block:: text

     /share

3. Show/suppress Campaigns on multiple specific URLs, i.e.: `https://site.com/products/product-1`
   and `https://site.com/products/product-5`.

   Here is the Regex criteria:

   .. code-block:: text

     /products/product-1|/products/product-5

   |

.. container:: hidden

   .. toctree::
