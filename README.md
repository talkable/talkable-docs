Talkable Documentation
======================

[![Build Status](https://travis-ci.org/talkable/talkable-docs.svg)](https://travis-ci.org/talkable/talkable-docs)

This GitHub repository represents Talkable’s documentation site, located at [docs.talkable.com](http://docs.talkable.com).

The Talkable documentation uses [reStructuredText](http://docutils.sourceforge.net/rst.html) as its markup language and is built using [Sphinx](http://sphinx-doc.org/).

Sphinx
------

For more details see [The Sphinx Documentation](http://sphinx-doc.org/contents.html).

reStructuredText
----------------

For more details see [The reST Quickref](http://docutils.sourceforge.net/docs/user/rst/quickref.html).

### Sections

Section headings are very flexible in reST. We use the following convention in the Talkable documentation:

* `#` for module headings
* `=` for sections
* `-` for subsections
* `.` for subsubsections

### Cross-referencing

Sections that may be cross-referenced across the documentation should be marked with a reference.
To mark a section use `.. _ref-name:` before the section heading.
The section can then be linked with `` :ref:`ref-name` ``. These are unique references across the entire documentation.

For example:

```rst
.. _talkable-module:

Talkable Module
###############

This is the module documentation.

.. _talkable-section:

Talkable Section
================

Talkable Subsection
-------------------

Talkable Subsubsection
......................

Here is a reference to "talkable section": :ref:`talkable-section` which will have the
name "Talkable Section".
```

Build the documentation
-----------------------

First install [Sphinx](http://sphinx-doc.org/). See below.

### Installing Sphinx on OS X

* Install [Homebrew](http://brew.sh/).

* Install Ruby and [Bundler](http://bundler.io/), and run `bundle install` to install dependencies.

* Install Python and pip:

  ```
  brew install python
  easy_install pip
  ```

  More information in case of trouble: https://github.com/Homebrew/homebrew/wiki/Homebrew-and-Python

* Install dependencies:

  ```
  pip install -r requirements.txt
  ```

If you get the error "unknown locale: UTF-8" when generating the documentation
the solution is to define the following environment variables:

    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8

### Building

Run `rake preview` from "master" branch.

#### Setting up LiveReload

Run `rake server` from "master" branch and open `http://localhost:5000` in browser.

### Deploying

If you’re deploying for the first time make sure you have `gh-pages` branch locally. Otherwise run the following command to create it: `git checkout -b gh-pages origin/gh-pages`.
If you did everything right, deploying is as easy as `rake deploy` from "master" branch.

#### Deploying to Staging

If it’s your first time deploying to staging, run `rake setup` to setup git remote.

Merge your changes into "void" branch and deploy with `rake deploy:staging`.

---

See "master" branch: https://github.com/talkable/talkable-docs

See "gh-pages" branch: https://github.com/talkable/talkable-docs/tree/gh-pages

See GitHub Page (auto generated): http://docs.talkable.com
