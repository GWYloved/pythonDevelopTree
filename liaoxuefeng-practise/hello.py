#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import sys

def test():
	args = sys.argv
	if len(args) == 1 :
		print 'hello world!'
	elif len(args) == 2 :
		print 'hello, %s !' % args[1]
	else:
		print 'too many arguments!'

if __name__ == '__main__':
	test()
