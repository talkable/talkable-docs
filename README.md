The Curebit documentation uses [reStructuredText](http://docutils.sourceforge.net/rst.html) as its markup language and is built using [Sphinx](http://sphinx-doc.org/).

## Sphinx

For more details see [The Sphinx Documentation](http://sphinx-doc.org/contents.html)

## reStructuredText

For more details see [The reST Quickref](http://docutils.sourceforge.net/docs/user/rst/quickref.html)

### Sections

Section headings are very flexible in reST. We use the following convention in the Curebit documentation:

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
.. _curebit-module:
 
Curebit Module
##############
 
This is the module documentation.
 
.. _curebit-section:
 
Curebit Section
===============
 
Curebit Subsection
------------------

Curebit Subsubsection
.....................
 
Here is a reference to "curebit section": :ref:`curebit-section` which will have the
name "Curebit Section".
```

## Build the documentation

First install [Sphinx](http://sphinx-doc.org/). See below.

### Installing Sphinx on OS X

Install [Homebrew](http://brew.sh/)

Install Python and pip:

    brew install python
    /usr/local/share/python/easy_install pip

More information in case of trouble: https://github.com/Homebrew/homebrew/wiki/Homebrew-and-Python

Install Sphinx:

    pip install sphinx
    
If you get the error "unknown locale: UTF-8" when generating the documentation the solution is to define the following environment variables:

    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8

### Building

If you did everything right, deploying is as easy as `make deploy` from "master" branch.

You can preview your changes with `make preview`.

---

See "master" branch: https://github.com/curebit/docs

See "gh-pages" branch: https://github.com/curebit/docs/tree/gh-pages

See GitHub Page (auto generated): http://curebit.github.io/docs/ (alias: http://docs.curebit.com)
