#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-16 22:04:44
# @Author  : tla001 (tla001@foxmail.com)
# @Link    : www.tla001.cn
# @Version : $Id$


import urllib2
import re
import itertools
import time

urlList = ['http://www.cnblogs.com/tla001/p/7490597.html',
			'http://www.cnblogs.com/tla001/p/7061758.html'
			]

agentlist = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
			'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36']

def download(url, user_agent='wswp', num_retries=2):
	print("Downloading:", url)
	headers = {'User-agent': user_agent}
	request = urllib2.Request(url, headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print("Download error:", e.reason)
		html = None
		if num_retries > 0:
			if hasattr(e, 'code') and 500 <+ e.code < 600:
				# recuresively retry 5xx HTTP errors
				return download(url, user_agent, num_retries-1)
	return html



if __name__ == "__main__":
	delay = 1
	sleep = 1
	while(1):

		for i in agentlist:
			for j in urlList:
				download(j, i)
				time.sleep(delay)
			time.sleep(sleep)
