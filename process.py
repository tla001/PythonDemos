#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 22:12:50
# @Author  : tla001 (tla001@foxmail.com)
# @Link    : www.tla001.cn
# @Version : $Id$

import multiprocessing
import time

def worker(interval):
	n = 5
	while n > 0:
		print 'The time is {0}'.format(time.ctime())
		n -= 1

def singleProcess():
	p = multiprocessing.Process(target = worker, args=(3,))
	p.start()
	print 'p.pid:',p.pid
	print 'p.name:',p.name
	print 'p.is_alive:',p.is_alive()

def mworker(interval,name):
	print 'This is process:%s' %name
	time.sleep(interval)
	print name,' end'

def multiProcess():
	p1 = multiprocessing.Process(target = mworker,args=(2,'process-1'))
	p2 = multiprocessing.Process(target = mworker,args=(3,'process-2'))
	p3 = multiprocessing.Process(target = mworker,args=(4,'process-3')) 

	p1.start()
	p2.start()
	p3.start()

	print 'The number of CPU is:'+str(multiprocessing.cpu_count())
	for p in multiprocessing.active_children():
		print 'child p.name:'+p.name +'\tp.id:'+str(p.pid)
	print "End"

class ClockProcess(multiprocessing.Process):
	def __init__(self, interval):
		multiprocessing.Process.__init__(self)
		self.interval = interval

	def run(self):
		n=5
		while n>0:
			print "the time is {0}".format(time.ctime())
			time.sleep(self.interval)
			n-=1


def worker_with(lock, f):
	with lock:
		fs = open(f,'a+')
		n=10
		while n>1:
			fs.write("Lock acquired via with\n")
			n-=1
		fs.close()

def worker_no_with(lock, f):
	lock.acquire()
	try:
		fs = open(f,'a+')
		n=10
		while n>1:
			fs.write("Lock acquired directly\n")
			n-=1
		fs.close()
	finally:
		lock.release()

def lock_test():
	lock = multiprocessing.Lock()
	f = "file.txt"
	w = multiprocessing.Process(target = worker_with,args=(lock,f))
	nw = multiprocessing.Process(target=worker_no_with,args=(lock,f))
	w.start()
	nw.start()

def sem_worker(s, i):
	s.acquire()
	print multiprocessing.current_process().name+" acquire\n"
	time.sleep(i)
	print multiprocessing.current_process().name+" release\n"
	s.release()

def sem_test():
	s=multiprocessing.Semaphore(1)
	for i in range(5):
		p = multiprocessing.Process(target=sem_worker,args=(s,i*2))
		p.start()


def wait_for_event(e):
	print "wait for event:starting"
	e.wait()
	print "wait for event: e.is_set()->"+str(e.is_set())

def wait_for_event_timeout(e,t):
	print "wait for event timeout:starting"
	e.wait(t)
	print "wait for event timeout:e.is_set->"+str(e.is_set())

def event_test():
	e= multiprocessing.Event()
	w1= multiprocessing.Process(name="block",target=wait_for_event,args=(e,))
	w2= multiprocessing.Process(name="no-block",target=wait_for_event_timeout,args=(e,2))

	w1.start()
	w2.start()

	time.sleep(3)
	e.set()
	print "event is set"


def writer_proc(q):
	try:
		q.put(1, block = False)
	except:
		pass

def reader_proc(q):
	try:
		print q.get(block = False)
	except:
		pass

def queue_test():
	q = multiprocessing.Queue()
	writer = multiprocessing.Process(target=writer_proc, args=(q,))
	writer.start()

	reader = multiprocessing.Process(target=reader_proc,args=(q,))
	reader.start()

	reader.join()
	writer.join()

def pipe_proc1(pipe):
	for i in xrange(5):
		print "send: %s" %(i)
		pipe.send(i)
		time.sleep(1)

def pipe_proc2(pipe):
		time.sleep(2)
		print "rec :",pipe.recv()

def pipe_test():
	pipe = multiprocessing.Pipe()
	p1 = multiprocessing.Process(target = pipe_proc1, args=(pipe[0],))
	p2 = multiprocessing.Process(target = pipe_proc2, args=(pipe[1],))

	p1.start()
	p2.start()

	p1.join()
	p2.join()


def pool_cb(msg):
	print "msg:",msg
	time.sleep(2)
	print "end"

def pool_test1():
	pool = multiprocessing.Pool(processes = 3)
	for i in xrange(4):
		msg = "hello %s"%(i)
		pool.apply_async(pool_cb,(msg,))

	pool.close()
	pool.join()
	print "processes done"

def pool_cb2(msg):
	print "msg:",msg
	time.sleep(2)
	print "end"
	return msg

def pool_test2():
	pool = multiprocessing.Pool(processes = 3)
	result = []
	for i in xrange(4):
		msg = "msg-%s" % i
		result.append(pool.apply_async(pool_cb2,(msg,)))
	pool.close()
	pool.join()

	for res in result:
		print res.get()

def main():
	# singleProcess()
	# multiProcess()
	# p = ClockProcess(3)
	# p.start()

	pool_test2()



if __name__ == '__main__':
	main()
