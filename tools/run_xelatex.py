#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os
import base64
import subprocess

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
	main()