#!/usr/bin/env python

import os, sys, re

itemfile = open(sys.argv[1])

lines = itemfile.readlines()

# parse input
items = []
for line in lines:
	str = re.compile("([0-9]+)@@@@[\-@0-9]+@(.*)@@@@[\-@0-9]+@(.*) // (.*)@@")
	match = re.match(str,line)
	if match:
		items.append([line,match.group(1),match.group(2),match.group(3),match.group(4)])
	else:
		items.append([line])

# insert dashes into output
for item in items:
	if len(item)==1:
		print("SKIPPED: %s\n" % item[0])
	else:
		orig = item[0]
		num = item[1]
		mcb = item[2]
		igt = item[3]
		eng = item[4]
		
		mcbsplit = mcb.replace('-',' -').replace('=',' =').split()
		igtsplit = igt.split()

		if len(mcbsplit) != len(igtsplit):
			print("DIFFERENT COUNT: %s\n" % item)
		else:
			for i in range(len(mcbsplit)):
				if mcbsplit[i].startswith('-'):
					igtsplit[i] = '-'+igtsplit[i]
			igtnew = ' '.join(igtsplit).replace(' -','-').replace(' =','=')
			print("%s \n%s \n%s \n%s \n" % (num, mcb, igtnew, eng))

