# Talkable Documentation

## What is Talkable Documentation?

The set of articles describing Talkable's capabilities, publicly available at [docs.talkable.com](https://docs.talkable.com).

It uses [reStructuredText](https://docutils.sourceforge.io/rst.html) as its markup language, an easy-to-read, what-you-see-is-what-you-get plaintext markup syntax. All reStructuredText formatting capabilities can be found in [The reST Quickref](https://docutils.sourceforge.io/docs/user/rst/quickref.html).

It is built using [Sphinx](https://www.sphinx-doc.org) with the `sphinx_book_theme`, an open-source documentation generation tool that transforms plain text files into beautifully formatted documentation. For more details, see [The Sphinx Documentation](https://www.sphinx-doc.org).

## Where is it stored?

It's stored in a dedicated GitHub repository ([talkable-docs](https://github.com/talkable/talkable-docs)).

The repository consists of the following branches:

- [master](https://github.com/talkable/talkable-docs/tree/master): The main branch used to keep the most recent stable version available at [docs.talkable.com](https://docs.talkable.com).
- [staging](https://github.com/talkable/talkable-docs/tree/staging): A staging branch used for testing by QA. It is available at [docs.bastion.talkable.com](https://docs.bastion.talkable.com).
- Feature branches created from `master` by individual contributors/developers.

## What is the documentation update workflow?

1. Pull changes from `master`.
2. Checkout a new branch from `master`.
3. Deploy the local/development environment.
4. Make changes and test them locally.
5. Commit the changes to the `staging` branch.
6. Get the documentation tested by QA.
7. Create a pull request to the `master` branch, providing the staging URL of the changed page in the pull request description.
8. Merge the pull request once it passes the review.

## How to deploy the local environment?

0. **Install Docker**

   Follow the [official Docker documentation](https://docs.docker.com/compose/install/).

   Note: Both Docker and Docker Compose are required for local development.

1. **Navigate to the repository root directory.**

   Ensure the `docker-compose.yml` file is located there.

2. **Create an `.env` file by copying `.env.template`.**

   Review and update the variable values if needed.

   For a **development/local environment**, all default settings should work out of the box. The only value you may need to change is `LOCAL_PORT` if `8080` is already in use on your local machine. The `BASE_URL` is automatically determined based on the `ENVIRONMENT` setting.

3. **Run the local environment deployment.**

   Run the command:

   ```bash
   docker compose --profile local up -d --build
   ```

   > [!NOTE]
   > Docker Compose uses profiles to manage different environments. If no profile is specified, `docker compose` does nothing. Always include `--profile local` for local development.

   If everything is set up correctly, the documentation will be available at [http://localhost:8080](http://localhost:8080). Make sure you use the port number defined in the `.env` file.

   If the documentation does not load, check the **Troubleshooting** section.

## How to remove the local environment

1. Stop the containers and remove the volumes

   ```bash
   docker compose down -v
   ```

2. Remove the built and downloaded images

   ```bash
   docker system prune -af
   ```

## How to deploy changes to production and staging?

You should not deploy it manually!

The deployment is handled by [Jenkins job](http://jenkins.production/view/Talkable-docs/).

All you need to do is commit your changes to the corresponding branch to deploy them to the appropriate server:

- Commit to the [staging](https://github.com/talkable/talkable-docs/tree/staging) branch => [docs.bastion.talkable.com](https://docs.bastion.talkable.com/).
- Commit to the [master](https://github.com/talkable/talkable-docs/tree/master) branch => [docs.talkable.com](https://docs.talkable.com/).

## How do I make the actual changes?

Navigate to the [source](./source/) directory and update the files using `reStructuredText` syntax. Refer to [The reST Quickref](https://docutils.sourceforge.io/docs/user/rst/quickref.html) for syntax details.

The documentation uses the following Sphinx extensions:

- `sphinx_sitemap` for generating sitemaps
- `sphinx_copybutton` for copy buttons on code blocks
- `sphinx_design` for advanced layout components

Here are some formatting examples:

### Sections

Section headings are very flexible in reST. We use the following convention in the Talkable documentation:

- `#` for module headings
- `=` for sections
- `-` for subsections
- `.` for subsubsections

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

## Redirects

> [!IMPORTANT]
> Please update the redirect rules if you change the file name, file path, or delete a file.

Redirects are implemented using the Nginx `rewrite` rules stored in [./nginx/redirects.conf](./nginx/redirects.conf) file.

After changing that file restart the local container to get the rules applied.

```bash
docker compose restart docs-local 
```

> [!TIP]
>
> - Use ChatGPT to adjust existing or add new rules. Ask for `nginx redirection rules`.
>
> - Avoid creating the rules by operating on something except paths (like protocols and hostnames). The best way is to manipulate paths only.

## Troubleshooting

### Can't view the documentation locally in the browser?

1. Ensure you are using the correct port number and protocol.
   The port number should match the value provided in `.env` as `LOCAL_PORT`.

2. Check logs:

   ```bash
   docker compose logs -f docs-local
   ```

## Links

- GitHub "staging" branch: [staging](https://github.com/talkable/talkable-docs/tree/staging)
- Staging web server: [docs.bastion.talkable.com](https://docs.bastion.talkable.com/)
- GitHub "production" branch: [master](https://github.com/talkable/talkable-docs/tree/master)
- Production web server: [docs.talkable.com](https://docs.talkable.com/)

## Additional Information

### Environment Configuration

The documentation automatically configures its base URL based on the `ENVIRONMENT` variable:

- `production`: `https://docs.talkable.com/`
- `staging`: `https://docs.bastion.talkable.com/`
- `local`: `http://localhost:{LOCAL_PORT}/`

### Theme and Styling

The documentation uses the `sphinx_book_theme` with custom styling defined in `source/_static/talkable.css`. The Talkable logo and favicon are located in `source/_static/img/`.
