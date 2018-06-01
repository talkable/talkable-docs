.. _advanced_features/reg_ex:
.. include:: /partials/common.rst

Setting up Campaign Placement criteria
======================================

Talkable allows setting up Campaign Placement “Shown on” / “Hidden on” criteria in two
formats:

1. **Relative match**. If the regex checkbox is turned **off** the relative match mode is
   used. “Relative” means it only matches the `pathname` of a URL and query parameters,
   without the domain part. In this mode site URL is always set and you only need to set a
   relative path. The criteria will only trigger when the relative path is matched (and
   query parameters when provided). Here are some examples:

   * Match only the homepage with optional query parameters:

     .. code-block:: text

       /

     Matched URLs (example):

     * `http://site.com/`
     * `https://new.domain.com/?utm=test`

     |

   * Match “/test/deep” exact path with optional query parameters:

     .. code-block:: text

       /test/deep

     Matched URLs (example):

     * `http://site.com/test/deep`
     * `https://new.domain.com/test/deep?utm=test`

     |

   * Match “/test/deep” exact path containing “utm=true” query parameter:

     .. code-block:: text

       /test/deep?utm=true

     Matched URLs (example):

     * `http://site.com/test/deep?utm=true`
     * `https://new.domain.com/test/deep?other=false&utm=true`

     |

2. **Regular expression** (regex for short). If the regex checkbox is turned **on** the
   regex mode is used. In this mode you are controlling full page URL, including the
   domain part (unlike the relative match mode). If no query parameters were set Talkable
   will ignore query parameters of the original URL in a browser.

   Use https://regex101.com to test placement criteria before applying it. Note: slashes
   are already escaped, no need to backslash them. See examples below:

   * Match URLs containing “/share” path with optional query parameters:

     .. code-block:: text

       /share

     Matched URLs (example):

     * `http://site.com/share`
     * `https://new.domain.com/test/share/deep?utm=test`

     |

   * Match URLs ending with “/share” and containing “utm=true” query parameter:

     .. code-block:: text

       /share/?\?(.+)?utm=true

     Matched URLs (example):

     * `http://site.com/share?other=false&utm=true`
     * `https://new.domain.com/test/share/?utm=true&other=false`

     |

   * Match “site.com/test” exact URL without any query parameters:

     .. code-block:: text

       site.com/test/?$

     Matched URLs (example):

     * `http://site.com/test`
     * `https://site.com/test/`

     |

   * Match URLs starting with “/cart” path with optional query parameters:

     .. code-block:: text

       https?://([\w\-\d]+\.)+[\w\-\d]+/cart

     Matched URLs (example):

     * `http://site.com/cart`
     * `http://new.domain.com/cart/deep?utm=test`

     |

   * Match URLs containing either “/products/one” or “/products/two” path with optional
     query parameters:

     .. code-block:: text

       /products/one|/products/two

     Matched URLs (example):

     * `http://site.com/test/products/one`
     * `http://stage.com/products/two`
     * `http://test.com/test/products/one/deep?utm=test`

.. container:: hidden

   .. toctree::
