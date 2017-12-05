#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-28 22:21:18
# @Author  : tla001 (tla001@foxmail.com)
# @Link    : www.tla001.cn
# @Version : $Id$

from collections import namedtuple
from collections import deque

def namedtuple_test():
	Point = namedtuple('Point', ['x','y'])
	p = Point(1,2)
	print p.x,p.y
	assert isinstance(p,tuple)

def deque_test():
	q = deque(['a','b','c'])
	q.append('d')
	q.appendleft('r')
	print q
	q.popleft()
	print q

from collections import defaultdict
def defaultdict_test():
	dd = defaultdict(lambda:'N/A')
	dd['key1']="aaa"
	print dd['key1']
	print dd['key2']

from collections import OrderedDict
def orderedDict_test():
	d = OrderedDict([('a',1),('c',2),('b',3)])
	print d

from collections import Counter
def counter_test():
	c = Counter()
	for ch in 'programer':
		c[ch] = c[ch] + 1
	print c 

import hashlib
def hashlib_test():
	md5 = hashlib.md5()
	md5.update("tla001")
	print md5.hexdigest() 


import socket
import threading
import time

def tcpLink(sock, addr):
	print 'accept new connection from %s:%s...' %addr
	sock.send('Welcome')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello, %s' %data)
	sock.close()
	print 'connection from %s:%s closed' %addr


def server():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('127.0.0.1',9999))
	s.listen(5)
	print 'Waiting for clients...'
	
	while True:
		sock, addr = s.accept()
		t = threading.Thread(target=tcpLink,args=(sock, addr))
		t.start()

def client():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('127.0.0.1',9999))
	print s.recv(1024)
	for data in ['tla001', 'xiaoheizi']:
		s.send(data)
		print s.recv(1024)
	s.send('exit')
	s.close()

def udp_server():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind(('127.0.0.1',9999))
	print 'Bind UDP on 9999...'
	while True:
		data, addr = s.recvfrom(1024)
		print 'Received from %s:%s' %addr
		s.sendto('Hello,%s' %data,addr)

def udp_client():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	for data in ['tla001', 'xiaoheizi']:
		s.sendto(data,('127.0.0.1',9999))
		print s.recv(1024)
	s.close()

if __name__ == '__main__':
	udp_client()
