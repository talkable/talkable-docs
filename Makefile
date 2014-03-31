# Makefile for Sphinx documentation
#

# Internal variables.
SPHINXBUILD      = sphinx-build
SOURCEDIR        = source
BUILDDIR         = build
SPHINXOPTS       = -d $(BUILDDIR)/doctrees $(SOURCEDIR)
GH_PAGES_SOURCES = source Makefile

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

.PHONY: help clean html preview deploy

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  preview    to make standalone HTML files and open index.html in the default browser"
	@echo "  deploy     to commit and deploy changes to GitHub"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

up:
	make clean && make html

preview:
	make up
	open $(BUILDDIR)/html/index.html

deploy:
	git checkout gh-pages
	git pull
	rm -rf $(BUILDDIR) $(SOURCEDIR)
	git checkout master $(GH_PAGES_SOURCES)
	git reset HEAD
	make html
	(cd $(BUILDDIR)/html && tar c .) | (cd ./ && tar xf -)
	rm -rf $(GH_PAGES_SOURCES) $(BUILDDIR)
	echo '' > .nojekyll
	echo 'docs.curebit.com' > CNAME
	git add -A
	git commit -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master
	@echo
	@echo "Deployment finished. Check updated docs at http://docs.curebit.com"
