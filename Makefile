# Makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
PAPER         =
SOURCEDIR     = source
BUILDDIR      = build

# Internal variables.
ALLSPHINXOPTS    = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) $(SOURCEDIR)
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
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

preview:
	make clean && make html
	open $(BUILDDIR)/html/index.html

deploy:
	git checkout gh-pages
	rm -rf $(BUILDDIR) $(SOURCEDIR)
	git checkout master $(GH_PAGES_SOURCES)
	git reset HEAD
	make html
	(cd build/html && tar c .) | (cd ./ && tar xf -)
	rm -rf $(GH_PAGES_SOURCES) $(BUILDDIR)
	echo '' > .nojekyll
	echo 'docs.curebit.com' > CNAME
	git add -A
	git ci -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages ; git checkout master
