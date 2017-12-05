#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-28 21:04:52
# @Author  : tla001 (tla001@foxmail.com)
# @Link    : www.tla001.cn
# @Version : $Id$

import threading
import time

count = 0
class Counter(threading.Thread):
	def __init__(self,lock,threadName):
		super(Counter, self).__init__(name = threadName)
		self.lock = lock

	def run(self):
		global count
		self.lock.acquire()
		for i in xrange(10000):
			count += 1
		self.lock.release()

def thread_test1():
	lock = threading.Lock()
	for i in xrange(5):
		Counter(lock, "thread-"+str(i)).start()
	time.sleep(2)
	print count

def addFunc(lock):
	global count
	lock.acquire()
	for i in xrange(100):
		count +=1
	lock.release()

def thread_test2():
	lock = threading.Lock()
	for i in xrange(5):
		threading.Thread(target = addFunc, args=(lock,),name="thread-"+str(i)).start()

	time.sleep(2)
	print count




if __name__ == '__main__':
	thread_test2()
