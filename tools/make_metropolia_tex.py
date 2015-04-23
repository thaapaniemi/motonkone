#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import site

import time
import os
import base64
import subprocess
import metadata

def load_file(filename):
	c = None
	with open(filename,"rb") as fh:
		c = fh.read()

	return c

def save_file(filename,content):
	with open(filename,"wb") as fh:
		fh.write(content)

def add_metadata_to_tex(filenames,layout_name=None):
	if layout_name is None:
		layout_name = os.path.dirname(os.path.realpath(sys.argv[0])) +"/template/metropolia_layout.tex"

	md = metadata.harvest_yaml(filenames[0])
	layout = load_file( layout_name)

	for key in md:
		layout = layout.replace("__"+key.upper()+"__",md[key])

	for filename1 in filenames:
		fileName, fileExtension = os.path.splitext(filename1)
		if fileExtension == ".bib":
			continue

		#content = load_file(filename1)

		#for key in md:
		#	content = content.replace("__"+key.upper()+"__",md[key])

		#layout += "\n"+content
		layout += "\n\\input{"+ ".".join(filename1.split(".")[:-1]) +"}"

	layout +="\n"
	
	return layout

if __name__ == '__main__':
	save_file( "test_out.tex", add_metadata_to_tex(sys.argv[1:]) )

