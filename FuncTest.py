#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 14:57:25
# @Author  : tla001 (tla001@foxmail.com)
# @Link    : www.tla001.cn
# @Version : $Id$

import os


def param_check(x):
	if not isinstance(x,(int, float)):
		raise TypeError('bad operand type')


def return_mul():
	a = 5
	b = 6
	return a,b


def add_nums(*numbers):
	sum = 0
	for n in numbers:
		sum +=n
	return sum

def person(name, age, **kw):
	print name, age, kw

def is_odd(n):
	return n%2==1

def reserved_cmp(a, b):
	if a>b:
		return -1
	if a<b:
		return 1
	return 0

def func_sum(*nums):
	def sum():
		ret = 0;
		for num in nums:
			ret +=num
		return ret
	return sum

import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' %func.__name__
		return func(*args, **kw)
	return wrapper

@log
def now1():
	print "2017-11-20"

def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s():' % (text, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorator 

@log('excute')
def now2():
	print "2017-11-20"

import cPickle as pickle

def seri():
	d = dict(name = 'tla001', age = 25)
	f = open('dump.txt','wb')
	pickle.dump(d, f)
	f.close()


def main():
	# param_check('a')
	# a,b=return_mul()
	# print add_nums(1,2,3)
	# nums = [1, 2, 3]
	# print add_nums(*nums)

	# person('tao', 12)
	# person('tao', 13, address='china')

	# print filter(is_odd,[1, 2, 3, 4, 5])
	# print sorted([12, 3, 4, 5, 2, 1, 13], reserved_cmp)
	# f = func_sum(1, 2, 3, 4, 5)
	# print f()

	# print map(lambda x:x*x,[1, 2, 3, 4])
	# f = lambda x:x*x
	# print f(4)

	# now1()
	# now2()

	# int2 = functools.partial(int, base=5)
	# print int2('124')

	seri()

if __name__ == '__main__':
	main()