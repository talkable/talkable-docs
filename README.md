Talkable Documentation
======================

[![Build Status](https://circleci.com/gh/talkable/talkable-docs.svg?style=svg&circle-token=cc33458158e7b0c1f6f8cbf1bcbf74f00ee28a8e)](https://circleci.com/gh/talkable/workflows/talkable-docs)

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

* Install Python (>= 3.5) and pip:

  ```
  brew install python
  ```

  More information in case of trouble: https://docs.brew.sh/Homebrew-and-Python

* Install dependencies:

  ```
  pip3 install -r requirements.txt
  ```

  If you have problems, try adding `-I` flag (`--ignore-installed`) to the `pip install` command.

If you get the error "unknown locale: UTF-8" when generating the documentation,
the solution is to define the following environment variables:

    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8

### Building

Run `rake preview` from "master" branch.

#### Setting up LiveReload

Run `rake server` from "master" branch and open `http://localhost:5000` in browser.

### Deploying

If you’re deploying for the first time make sure you have `gh-pages` branch locally. Otherwise run the following command to create it: `git checkout -b gh-pages origin/gh-pages`.

General flow:
1. Pull changes from master
2. Checkout your new branch from master
3. Make changes
4. Deploy your changes to staging (see the instruction below)
4. Create a Pull Request to "master" branch, providing the demo URL to the changed page in Pull Request’s description.
5. Merge pull request once it passes the review
6. Deploy

If you did everything right, deploying is as easy as `rake deploy` from "master" branch.

#### Deploying to Staging

If it’s your first time deploying to staging, run `rake setup` to setup git remote.

1. Switch to local branch "void" and pull the latest changes from the remote:
  `git checkout void; git pull`
2. Merge your branch into local branch "void":
  `git merge YOUR_BRANCH_NAME`
3. Push the changes to the remote branch "void":
  ```git push origin void```
4. Deploy:
  ```rake deploy:staging```

---

See "master" branch: https://github.com/talkable/talkable-docs

See "gh-pages" branch: https://github.com/talkable/talkable-docs/tree/gh-pages

See GitHub Page (auto generated): http://docs.talkable.com
