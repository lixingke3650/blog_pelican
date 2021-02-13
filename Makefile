#SHELL = /bin/bash

PY=python3
GIT=git
PELICAN=pelican
PELICANOPTS=

SOURCEPATH=/home/hanbin/Dropbox/CodeCentre/blog/rst
INPUTPATH=./rst
RESOURCE=resource
OUTPATH=./html
GITPATH=https://github.com/lixingke3650
CACHE=__pycache__

CONFFILE=./pelicanconf.py

# preview
PREVIEWCONFFILE=./pelicanconf_preview.py
PREVIEWDIR=preview
PREVIEWINPUTPATH=./$(PREVIEWDIR)
PREVIEWOUTPUTPATH=$(PREVIEWINPUTPATH)/html
PREVIEWHTMLPATH=$(OUTPATH)/$(PREVIEWDIR)

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make slink                  make a link to rst or md source         '
	@echo '   make html                   (re)generate the web site               '
	@echo '   make preview                pre-build the web site for a new page   '
	@echo '   make clean                  remove the generated files              '
	@echo '   make push                   push to lixingke3650.github.io          '
	@echo '   make remove                 remove all file lixingke3650.github.io  '
	@echo '                                                                       '

dev:
	$(PELICAN) $(INPUTPATH) -s $(CONFFILE) $(PELICANOPTS)

slink:
	@ln -snf $(SOURCEPATH) $(INPUTPATH)

html:
	$(PELICAN) $(INPUTPATH) -s $(CONFFILE) $(PELICANOPTS)
	@rsync -a $(INPUTPATH)/$(RESOURCE)/ $(OUTPATH)/$(RESOURCE)/

# make a html for preview folder ad link it to html path
preview:
	@rm -f $(PREVIEWHTMLPATH)
	@rm -rf $(PREVIEWOUTPUTPATH)
	$(PELICAN) $(PREVIEWINPUTPATH) -s $(PREVIEWCONFFILE) $(PELICANOPTS)
	ln -snf .$(PREVIEWOUTPUTPATH) $(PREVIEWHTMLPATH)

push:
	@cp -r $(OUTPATH)/* $(GITPATH)
	@cd $(GITPATH) && ($(GIT) add .) && ($(GIT) commit -m "memoup") && ($(GIT) push -u origin master)

# clean output html/rst link/pycache/preview catch
clean:
	@echo 'revome output html ...'
	@rm -rf $(OUTPATH)
	@echo 'revome link for rst or md source ...'
	@rm -f $(INPUTPATH)
	@echo 'revome py cache ...'
	@rm -rf $(CACHE)
	@echo 'remove preview cache ...'
	@rm -rf $(PREVIEWOUTPUTPATH)
	@rm -rf $(PREVIEWINPUTPATH)
	@rm -f $(PREVIEWOUTPUTPATH)

remove:
	@echo '-- Not completed --'

.PHONY: html preview help clean push remove