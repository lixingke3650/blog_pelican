# python3
# -*-coding: utf8 -*-
# Filename: makeup.py

import os

# make
os.system( 'make html' )

os.chdir('/home/hanbin/web/blog/lixingke3650.github.io')

# commit
os.system( 'git add *' )
os.system( 'git commit -m "memoup" ' )
os.system( 'git push -u origin master' )
