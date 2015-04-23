#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os
import base64
import subprocess

import shutil
import tempfile

from make_metropolia_tex import add_metadata_to_tex

execdir = os.path.dirname(os.path.realpath(sys.argv[0]))
curdir = os.getcwd()

tempdir = tempfile.mkdtemp()

def preprocess(filenames):
	pass
	texfile = add_metadata_to_tex(filenames)
	texfile = texfile.replace("\graphicspath{{illustration/}}","\graphicspath{{"+ curdir +"/illustration/}}")

	bibpieces = []
	for bibpiece in texfile.split("\\bibliography{"):
		bibpiece = bibpiece.split("}")[0]
		bibpieces.append(bibpiece)

	bibpieces_normalized = []
	for f in bibpieces:
		if os.path.isfile(f):
			shutil.copy(f,tempdir)
			bibpieces_normalized.append( tempdir + "/" + os.path.basename(f) )

	temp = tempfile.mkstemp()
	temp[0].write(texfile)
	close(temp[0])

	return {"texfilename":temp[1],"bibpieces":bibpieces_normalized}


def run_ext(array,stdin=None):
	try:
		ssh = subprocess.Popen(array, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

		if stdin is not None:
			ssh.stdin.write( stdin )
		
		out, err = ssh.communicate()

		#print out
		#print err

		return (out,err)
	except OSError as e:
		print str("ERROR:")
		print "call: " + str(array)
		print "stdin:" + str(stdin)
		print "-----"
		raise e

def main2():
	pf = preprocess(sys.arv[1:])

	print run_ext(["xelatex", pf["texfilename"] ])[0]

	for b in pf["bibpieces"]:
		print run_ext(["bibtex", b])[0]
	
	print run_ext(["xelatex", pf["texfilename"] ])[0]
	print run_ext(["xelatex", pf["texfilename"] ])[0]	

	print "ok"

	shutil.rmtree(tempdir)

def main():
	filename_original = sys.argv[1]

	fileName, fileExtension = os.path.splitext(filename_original)

	if fileExtension != ".tex":
		print "ERR! unknown extension " + str(fileExtension)
		sys.exit(1)
	else:

		for ext in (".aux",".log",".bbl",".pdf",".blg",".out",".toc"):
			if os.path.isfile(fileName+ext):
				os.remove(fileName+ext)

		print run_ext(["xelatex",filename_original])[0]
		print run_ext(["bibtex",fileName + ".aux"])[0]
		print run_ext(["xelatex",filename_original])[0]
		print run_ext(["xelatex",filename_original])[0]

		print "ok"

	pass

if __name__ == '__main__':
	main2()