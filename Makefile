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

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make slink                  make a link to rst or md source         '
	@echo '   make html                   (re)generate the web site               '
	@echo '   make clean                  remove the generated files              '
	@echo '   make push                   push to lixingke3650.github.io          '
	@echo '   make remove                 remove all file lixingke3650.github.io  '
	@echo '                                                                       '

dev:
	$(PELICAN) $(INPUTPATH) -s $(CONFFILE) $(PELICANOPTS)

slink:
	@ln -snf $(SOURCEPATH) $(INPUTPATH)

html:
# 	@cp -rf $(SOURCEPATH)/* $(INPUTPATH)
	$(PELICAN) $(INPUTPATH) -s $(CONFFILE) $(PELICANOPTS)
	@rsync -a $(INPUTPATH)/$(RESOURCE)/ $(OUTPATH)/$(RESOURCE)/

push:
	@cp -r $(OUTPATH)/* $(GITPATH)
	@cd $(GITPATH) && ($(GIT) add .) && ($(GIT) commit -m "memoup") && ($(GIT) push -u origin master)

clean:
	@echo 'revome output html ...'
	@rm -rf $(OUTPATH)
	@echo 'revome link for rst or md source ...'
	@rm -f $(INPUTPATH)
	@echo 'revome some cache ...'
	@rm -rf $(CACHE)

remove:
	@echo '-- Not completed --'

.PHONY: html help clean push remove