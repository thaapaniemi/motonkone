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

def add_metadata_to_tex(filename):
	md = metadata.harvest_yaml(filename)
	layout = load_file("th_layout.tex")
	
	filenames = sys.argv[1:]

	for key in md:
		layout = layout.replace("__"+key.upper()+"__",md[key])

	for filename in filenames:
		content = load_file(filename)

		for key in md:
			content = content.replace("__"+key.upper()+"__",md[key])

		layout += "\n"+content
		#layout += "\n\\input{"+ ".".join(filename.split(".")[:-1]) +"}"

	layout +="\n"
	
	return layout

if __name__ == '__main__':
	save_file( "test_out.tex", add_metadata_to_tex(sys.argv[1]) )

