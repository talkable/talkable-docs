# Makefile for Sphinx documentation
#

# Internal variables.
SPHINXBUILD      = sphinx-build
UTF_LOCALE       = LC_ALL=en_US.UTF-8
SOURCEDIR        = source
BUILDDIR         = build
SPHINXOPTS       = -d $(BUILDDIR)/doctrees $(SOURCEDIR)
GH_PAGES_SOURCES = source Makefile

INTEGRATION_VERSION = 1.0.22
INTEGRATION_URL = "//d2jjzw81hqbuqv.cloudfront.net/integration/talkable-$(INTEGRATION_VERSION).min.js"

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you do not have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

.PHONY: help clean html test preview server deploy

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  preview    to make standalone HTML files"
	@echo "  server     to make standalone HTML files and run the server on localhost:5000"
	@echo "  server     run the server on localhost:5000 and open a browser"
	@echo "  test       to run build in test mode"
	@echo "  deploy     to commit and deploy changes to GitHub"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(UTF_LOCALE) $(SPHINXBUILD) -b html $(SPHINXOPTS) $(BUILDDIR)/html
	sed -i '' "s#|integration_version|#$(INTEGRATION_VERSION)#g" `find $(BUILDDIR)/html -name \*.html`
	sed -i '' "s#|integration_url|#$(INTEGRATION_URL)#g" `find $(BUILDDIR)/html -name \*.html`
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

preview:
	make clean html

server:
	make preview
	(sleep 2 && open "http://localhost:5000")&
	$(UTF_LOCALE) bundle exec foreman start

test:
	$(UTF_LOCALE) $(SPHINXBUILD) -nW -b html $(SPHINXOPTS) $(BUILDDIR)/html

deploy:
	git checkout gh-pages
	git pull
	rm -rf $(BUILDDIR) $(SOURCEDIR)
	git checkout master $(GH_PAGES_SOURCES)
	git reset HEAD
	make html
	(cd $(BUILDDIR)/html && tar c ./) | (cd ./ && tar xf -)
	rm -rf $(GH_PAGES_SOURCES) $(BUILDDIR) .buildinfo
	echo '' > .nojekyll
	echo "/build\n/.bundle" > .gitignore
	echo 'docs.talkable.com' > CNAME
	git add -A
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master
	@echo
	@echo "Deployment finished. Check updated docs at http://docs.talkable.com"
