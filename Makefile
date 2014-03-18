# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
BUILDDIR      = _build

GHPAGES       = $(realpath $(dir $(lastword $(MAKEFILE_LIST)))/..)/gh-pages

# User-friendly check for sphinx-build
ifeq ($(shell which $(SPHINXBUILD) >/dev/null 2>&1; echo $$?), 1)
$(error The '$(SPHINXBUILD)' command was not found. Make sure you have Sphinx installed, then set the SPHINXBUILD environment variable to point to the full path of the '$(SPHINXBUILD)' executable. Alternatively you can add the directory with the executable to your PATH. If you don't have Sphinx installed, grab it from http://sphinx-doc.org/)
endif

# Internal variables.
PAPEROPT_a4     = -D latex_paper_size=a4
PAPEROPT_letter = -D latex_paper_size=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
# the i18n builder cannot share the environment and doctrees with the others
I18NSPHINXOPTS  = $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

.PHONY: help clean html preview deploy

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html       to make standalone HTML files"
	@echo "  preview    to make standalone HTML files and open index.html in the default browser"
	@echo "  deploy     to commit and deploy changes to GitHub"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

preview:
	make clean && make html
	open $(BUILDDIR)/html/index.html

deploy:
	cd $(GHPAGES) && git reset --hard origin/gh-pages
	mkdir $(BUILDDIR)/temp
	mv $(GHPAGES)/.git $(BUILDDIR)/temp/
	rm -rf $(BUILDDIR)/html $(GHPAGES)/*
	make html
	rm $(BUILDDIR)/html/.buildinfo
	cp -a $(BUILDDIR)/html/. $(GHPAGES)/
	mv $(BUILDDIR)/temp/.git $(GHPAGES)/
	rm -rf $(BUILDDIR)/temp
	touch $(GHPAGES)/.nojekyll
	echo 'docs.curebit.com' > $(GHPAGES)/CNAME
	cd $(GHPAGES) && git add -A && git ci -m "Generated gh-pages" && git pull && git push origin gh-pages
