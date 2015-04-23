#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import os
import base64
import yaml
from pprint import pprint

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def harvest_yaml(filename):
	lines = []
	with open(filename) as fh:
		yaml_found = None

		for line in fh.readlines():
			line = line.strip()
			if line.find("---") > 0 and yaml_found is None:
				yaml_found = True
			elif line.find("---") > 0 and yaml_found is True:
				yaml_found = False
			
			if yaml_found:
				start_loc = line.find("%") +1
				if start_loc > 5:
					start_loc = 0

				lines.append(line[start_loc:].strip())

			elif yaml_found is False:
				break

	#lines.append("---")
	return yaml.safe_load("\n".join(lines))

def main():
	data = harvest_yaml(sys.argv[1])
	print data

	a = yaml.safe_load(data)

	pprint(a)

	#print yaml.dump(a, Dumper=Dumper, allow_unicode=True, default_flow_style=False)

if __name__ == '__main__':
	main()