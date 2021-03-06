#!/usr/bin/python 
# -*- coding: utf-8 -*-
import io
import string
from jseg import Jieba
from .classProcess import outPutCate

jieba = Jieba()

stopWords = []
with io.open('src/stopwords_zhTw.txt','r',encoding='utf-8') as f:
	for line in f:
		stopword = line.replace('\n', '')
		stopWords.append(stopword)


# State of word: n, zg, etc.
def getWeights(posArr):
	return len(posArr)

def vote(candidates):
	def distance(weightA, weightB):
		return abs(weightA - weightB)

	# sub is for confliction purpose(classify to 'other')
	max_weight = 0.0
	sub_weight = 0.0
	max_cate = ''
	sub_cate = ''

	diff_threshold = 1

	for cate in candidates:
		cur_cate = cate
		cur_weight = getWeights(candidates[cate])
		if(cur_weight > max_weight):
			if(max_weight > sub_weight):
				sub_weight = max_weight
				sub_cate = max_cate
			max_weight = cur_weight
			max_cate = cur_cate
		elif(cur_weight > sub_weight):
			sub_weight = cur_weight
			sub_cate = cur_cate

	result = '其他'
	if(distance(max_weight, sub_weight) >= diff_threshold):
		result = max_cate
	return result

def outputRes(query):
	res = {}
	cates = []
	try:
		it = jieba.seg(query, pos=True)
		itemName = ''
		for i in it:
			(word, flag) = i

			if(word.isdigit()):
				res['dollar'] = int(word)
			elif(needFiltered(word)):
				itemName += word
				continue
			else:
				itemName += word
				(category, weightsObj) = outPutCate(word)
				category_flag_pair = (category, flag)
				cates.append(category_flag_pair)
				if(category == '找不到'):
					print(word)

		candidates = {}
		for (cate, flag) in cates:
			if(cate in candidates):
				flag_arr = candidates[cate]
				flag_arr.append(flag)
			else:
				flag_arr = [flag]
			candidates[cate] = flag_arr

		res['category'] = vote(candidates)
		res['item'] = itemName.replace('元', '').replace('塊', '').replace('錢', '').strip()
	except Exception as a:
		print(a)
	return res

def needFiltered(s):
	s = s.strip()
	flag = False
	if(isDummy(s)):
		flag = True
	elif(s in string.punctuation):
		flag = True
	elif(s in stopWords):
		flag = True
	return flag

def isDummy(s):
	if(s == '' or s.isspace()):
		return True
	else:
		return False

def isDummy(s):
	if(s == '' or s.isspace()):
		return True
	else:
		return False
