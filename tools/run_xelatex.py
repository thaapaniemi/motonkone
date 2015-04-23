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
original_cwd = os.getcwd()

tempdir = tempfile.mkdtemp()

def preprocess(filenames):
	pass
	texfile = add_metadata_to_tex(filenames)
	texfile = texfile.replace("\graphicspath{{illustration/}}","\graphicspath{{"+ original_cwd +"/illustration/}}")

	shutil.rmtree(tempdir)
	shutil.copytree(execdir+"/template",tempdir)
	shutil.copy(execdir+"/template/vancouver_fi.bst",tempdir)

	bibpieces = []
	i = 0
	for bibpiece in texfile.split("\\bibliography{"):
		if i== 0:
			i += 1
			continue
		bibpiece = bibpiece.split("}")[0]
		bibpieces.append(bibpiece + ".bib")
		i +=1

	bibpieces_normalized = []
	for f in bibpieces:
		print f
		if os.path.isfile(f):
			shutil.copy(f,tempdir)
			bibpieces_normalized.append( tempdir + "/" + os.path.basename(f+".bib") )

	temp = tempfile.mkstemp(dir=tempdir,suffix=".tex")
	
	with os.fdopen(temp[0],"wb") as fh:
		fh.write(texfile)

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
	pf = preprocess(sys.argv[1:])

	os.chdir(tempdir)

	originalFileName, originalFileExtension = os.path.splitext(sys.argv[1])

	fileName, fileExtension = os.path.splitext(pf["texfilename"])
	fileName = os.path.basename(fileName)

	print run_ext(["xelatex", fileName+fileExtension ])[0]

	#for b in pf["bibpieces"]:
	#	print run_ext(["bibtex", b])[0]
	print run_ext(["bibtex", fileName+".aux"])[0]
	
	print run_ext(["xelatex", fileName+fileExtension ])[0]
	print run_ext(["xelatex", fileName+fileExtension ])[0]	

	print "ok"

	shutil.copy(fileName+".pdf",original_cwd+"/"+originalFileName+".pdf")

	os.chdir(original_cwd)

	shutil.rmtree(tempdir)
	#print tempdir

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