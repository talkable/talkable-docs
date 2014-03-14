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
 
Here is a reference to "curebit section": :ref:`curebit-section` which will have the
name "Curebit Section".
```
