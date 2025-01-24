Talkable Documentation
======================

Overview
--------

This GitHub repository represents Talkable’s documentation site, located at [docs.talkable.com](https://docs.talkable.com).

The Talkable documentation uses [reStructuredText](https://docutils.sourceforge.io/rst.html) as its markup language and is built using [Sphinx](https://www.sphinx-doc.org).

For more details see [The Sphinx Documentation](https://www.sphinx-doc.org).

Concepts
--------

#### reStructuredText

An easy-to-read, what-you-see-is-what-you-get plaintext markup syntax.
All reStructuredText formatting capabilities can be found at [The reST Quickref](https://docutils.sourceforge.io/docs/user/rst/quickref.html).

#### Documentation Builder

Dockerized set of Sphinx and Nginx containers. Used to build the static pages from .rst and other format files into html static pages (Sphinx) and populate tyem in form of the documentation pages (Nginx) available to the user.

#### Documentation Building Process

The .rst files need to be buit to static html files. That doesn't require any involvement from developers since is handled by the [sphinx-autobuild](https://github.com/sphinx-doc/sphinx-autobuild) package included in to the Documentation Builder set mentoned above.

#### Changes Deployment

The local deployment doesn't require any efforts since available instantly after the files are changed on the local machine storage. The Builder buils teh changes just after indicated the change.
The staging and producxtion deployment are handled by the corresponding Jenkins jobs just after the changes are pushed to the proper branch (staging or master) 

Environments
------------

### Local

Used to make teh local changes on developer's machine before pushing them to staging environment for testing by QA.
Deployed in form of docker container on the developer's machine.
Code managed in the dedicated github branch created from `master` branch.

### Staging

Used by QA team to test the documentation before pushing it to master branch/production environment.
Deployed in dockerised AWS infrastructure.
Code managed in `staging-bastion` branch.
Available under the following url `url to be provided` 

### Production

The public version of the documentation available to the users.
Deployed in dockerised AWS infrastructure.
Code managed in `master` branch.
Available under the following url `url to be provided` 

Workflows
---------

### General Flow:

1. Pull changes from master
2. Checkout your new branch from master
3. Deploy local Sphinx container
4. Make changes, test your changes locally
5. Commit the changes to staging branch
6. Get the documentation tested by QA
7. Create a Pull Request to "main" branch, providing the staging URL to the changed page in Pull Request’s description.
8. Merge pull request once it passes the review

### Builder Container Deployment

0. Install Docker

   Follow the [official Docker documentation](https://docs.docker.com/compose/install/)
  

1. Navigate to the repo root directory. 
   
   Make sure `docker-compose.yaml` file is located there.

2. Create `.env` file and set the value of the port you want the documentation to be available on your local machine. Use `.env.example` file as a template.
   
    ```
    NGINX_PORT=8080
    ENVIRONMENT=local
    ```

    Set the port number to the value you want to use as a port number while browsing the documentation locally.
    For teh example above you would use `http://localhost:8080`. Chose whichever free port.

    Possible values for `ENVIRONMENT` variable:
      - `local` for local development environment deployment
      - `staging` for staging
      - `production` for production 

3. Run the local environment deployment

    Run the command to deploy the Builder

    ```
    docker-compose up -d
    ```

4. Check the successfull deployment

    Try follow the link [http://localhost:8080](http://localhost:8080)
    Make sure you use the port number define din `.env` file
    If you've done everything right the documentation will open.
    If it doesn't check teh Troubleshooting section

Troubleshooting
---------------

#### Can't view the documentation locally in browser

1. Make sure you use correct post number and protocol.
    The port number should equal the number you've provided in `.env` as `NGINX_PORT` value

2. Check `nginx` logs:
    ```shell
    docker logs -f nginx
    ```

3. Check `Sphinx` logs
    ```shell
    dcoker logs -f sphinx
    ```

Formatting examples
-------------------

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


Deployment
----------

#### Local Enviro


1. Switch to local branch "void" and pull the latest changes from the remote:
  `git checkout void; git pull`
2. Merge your branch into local branch "void":
  `git merge YOUR_BRANCH_NAME`
3. Push the changes to the remote branch "void":
  ```git push origin void```

---

See "master" branch: https://github.com/talkable/talkable-docs

See "gh-pages" branch: https://github.com/talkable/talkable-docs/tree/gh-pages

See GitHub Page (auto generated): https://docs.talkable.com
