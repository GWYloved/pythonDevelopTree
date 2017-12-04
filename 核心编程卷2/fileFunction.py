#!user/bin/env python
# -* - coding: UTF-8 -* - 
filename = raw_input('Enter file name: ')
fobj = open(filename, 'r')
for eachLine in fobj:
	print eachLine
fobj.close()