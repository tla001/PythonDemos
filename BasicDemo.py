#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-09 20:47:56
# @Author  : tla001 (tla001@foxmail.com)
# @Link    : www.tla001.cn
# @Version : $Id$

import os


def basicData():
	#数据输入
	# user = raw_input("Enter your name:")
	# print user

	##字符串处理
	str = "python"
	print str[0]
	print str[2:4]
	print str[3:]
	print str[-1]

	##列表
	aList = [1,2,3,4]
	print aList
	#索引
	print aList[1]
	print aList[2:]
	print aList[:3]
	aList[2] = 5
	print aList
	#列表遍历方法
	for i in aList:
		print i

	for i in range(len(aList)):
		print aList[i],' '

	for i, val in enumerate(aList):
		print "index:%d value:%s" % (i+1,val)

	#改变起始位置
	for i, val in enumerate(aList, 2):
		print "index:%d value:%s" % (i+1,val)

	#列表解析
	bList = [x**2 for x in range(4)]
	print "bList:",bList

	bList = [x**2 for x in range(8) if not x % 2]
	print "bList:",bList


	##元组
	aTuple = ('this', 'is', 98, 23)
	print aTuple
	#索引
	print aTuple[2]


	##字典
	aDict = {"key1":"value1","key2":"value2","key3":"value3"}
	print aDict
	#字典遍历
	for key in aDict.keys():
		print aDict[key]

	for key, value in aDict.items():
		print "key:%s value:%s" % (key, value)


def ioOperaton():
	#写文件
	try:
		handle = open("file_text.txt","w")
		aList = ["This ", "is ","a ","demo "]
		for a in aList:
			handle.write(a+"\n")
	except IOError,e:
		print e
	finally:
		handle.close()

	#读文件
	handle = open("file_text.txt","r")
	for line in handle:
		print line.strip()
	handle.close()


class Student(object):
	#类变量
	index = 0

	def __init__(self, name, age):
		#实例变量
		self.name = name
		#私有变量
		self.__age = age
		print "object is constructed"

	def __del__(self):
		print "object is destroyed"

	def getName(self):
		return self.name

	def setAge(self,age):
		self.__age = age

	def getAge(self):
		return self.__getAge()

	def __getAge(self):
		return self.__age

	#类方法
	@classmethod
	def printClassInfo(cls):
		print cls.__name__
		print dir(cls)

	#静态方法
	@staticmethod
	def printClassAttr():
		Student.index+=1
		print Student.index


def aboutClass():
	s = Student("tao",12)
	print s.name
	print s.getAge()
	print Student.index
	print Student.__name__
	Student.printClassInfo()
	Student.printClassAttr()


def fileDemo():
	f = open("file_text.txt",'r')

	for line in f:
		print line

	allLines = f.readlines()
	for line in allLines:
		print line


def main():
	# basicData()
	# ioOperaton()
	# aboutClass()
	fileDemo()


if __name__ == '__main__':
	main()