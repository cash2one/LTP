#coding=utf8
"""
# Author: jackson
# Created Time : Mon 15 Jun 2015 02:05:11 PM CST

# File Name: ltp_test.py
# Description:

"""
import urllib2
import multiprocessing

def myprocess(filename):
	fin = open(filename,'r')
	fout = open(filename + '.out','w')
	url_get_base = "http://ltpapi.voicecloud.cn/analysis/?"
	# 这里替换成自己的用户id
	api_key = 'abcdefghijklmnopq'
	# 定义返回格式
	fmt = 'plain'
	# 识别命名实体
	pattern = 'ner'
	# 只返回命名实体
	only_ner = 'true'
	cnt = 0
	for k in fin:
		cnt += 1
		try:
			line = k.strip().split('\t')
			text = line[0]
			result = urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s&only_ner=%s" % (url_get_base,api_key,text,fmt,pattern,only_ner))
			content = result.read().strip()
			if len(content) == 0:
				continue
			name = content.split(' ')[0]
			if (content.split(' ')[1] == 'Ni'):
				print >> fout,name
			if cnt % 100 == 0:
				print filename + ' ' + str(cnt)
		except:
			continue
	fout.close()
	fin.close()
	

def ltp_muti():
	# 经过测试，更多的进程也不能提高速度，所以只开两个进程
	pool = multiprocessing.Pool(processes = 2)
	pool.apply_async(myprocess, ('xaa',))
	pool.apply_async(myprocess, ('xab',))
	'''
	pool.apply_async(myprocess, ('xac',))
	pool.apply_async(myprocess, ('xad',))
	pool.apply_async(myprocess, ('xae',))
	pool.apply_async(myprocess, ('xaf',))
	pool.apply_async(myprocess, ('xag',))
	pool.apply_async(myprocess, ('xah',))
	pool.apply_async(myprocess, ('xai',))
	pool.apply_async(myprocess, ('xaj',))
	pool.apply_async(myprocess, ('xak',))
	pool.apply_async(myprocess, ('xal',))
	pool.apply_async(myprocess, ('xam',))
	pool.apply_async(myprocess, ('xan',))
	pool.apply_async(myprocess, ('xao',))
	pool.apply_async(myprocess, ('xap',))
	'''
	pool.close()
	pool.join()	

if __name__ == '__main__':
	ltp_muti()
