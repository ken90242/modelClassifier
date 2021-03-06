#!/usr/bin/env python
#-*- coding: utf-8 -*-
from tqdm import tqdm
from ..src import outputRes
from gensim.models import Word2Vec
from collections import OrderedDict
import codecs

#交通食物mode
def validate_test(filePath, mode):
	testDic = OrderedDict()
	print('Start loading testSet..')
	
	descsFile = codecs.open(filePath, 'rb', encoding='utf8')
	
	#with open(filePath,'r',encoding='utf-8') as f:
	for line in descsFile:
		try:
			(itemId, category, itemName) = line.split(',')
			itemName = itemName.replace('\n', '').strip()
			#category = category.replace('\n', '')
			#if category=='交通':
			testDic[itemName] = category
			#print ("dict ",category," ",itemName)
		except:
			# total += 1
			#print('[Debug] line #' + total)
			print ("csv error")
	print('testSet loaded.')
	nof = 0
	f = 0
	(total, tp, fp, tn, fn) = (len(testDic.items()), 0, 0, 0, 0)
	for itemName, category in testDic.items():
		#print ("dict: ", itemName,category)
		#print ("result: ",outputRes(itemName))
		predictCategory = outputRes(itemName)['category']
		if(category == predictCategory and category == mode):
			tp += 1
		elif(category == predictCategory and category != mode):
			tn += 1
		elif(category != predictCategory and predictCategory == mode):
			fp += 1
		elif(category != predictCategory and category == mode):
		# else:
			# print(itemName)
			fn += 1
		# else:
			# print(itemName)
	printTestRes(total, tp, fp, fn, tn, mode)

def printTestRes(total, tp, fp, fn, tn, mode):
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	accuracy = (tp + tn) / total
	f1 = (2 * precision * recall) / (precision + recall)

	print('Mode:', mode)
	print('Total:', str(total))
	print('True Positive:', str(tp))
	print('False Positive:', str(fp))
	print('True Negative:', str(tn))
	print('False Negative:', str(fn))
	print('Precision:',str(precision))
	print('Recall:',str(recall))
	print('Accuracy:' + str(accuracy))
	print('F1:' + str(f1))
	print('-----------------------------------------------------------------------------------')

# validate_test('testSet.txt', '飲食')
# validate_test('testSet.txt', '交通')

# from tqdm import tqdm
# from splitProcess import outputRes
# from gensim.models import Word2Vec

# model = Word2Vec.load('./wiki-zh_news-model')

# # 食物, 交通mode
# def validate_test(filePath, modesArr):
# 	testDic = {}
# 	print('Start loading testSet..')
# 	count = 0
# 	with open(filePath) as f:
# 		for line in f:
# 			count += 1
# 			try:
# 				if(count > 10):
# 					break
# 				(itemId, category, itemName) = line.split(',')
# 				itemName = itemName.replace('\n', '')
# 				testDic[itemName] = category
# 			except:
# 				# total += 1
# 				print('[Debug] line #' + total)
# 	print('testSet loaded.')

# 	modelObj = { mode: {'total': len(testDic.items()),'tp': 0, 'tn': 0, 'fp': 0, 'fn': 0} for mode in modesArr }
# 	print(modelObj)
# 	for itemName, category in tqdm(testDic.items()):
# 		predictCategory = outputRes(itemName)['category']
# 		for mode in modesArr:
# 			print(mode)
# 			if(category == predictCategory and category == mode):
# 				modelObj[mode]['tp'] += 1
# 			elif(category == predictCategory and category != mode):
# 				modelObj[mode]['tn'] += 1
# 			elif(category != predictCategory and predictCategory == mode):
# 			  modelObj[mode]['fp'] += 1
# 			elif(category != predictCategory and category == mode):
# 				modelObj[mode]['fn'] += 1
# 	print(modelObj)
# 	printTestRes(modelObj)

# def printTestRes(modelObj):
# 	for mode in modelObj.keys():
# 		obj = modelObj[mode]
# 		(total, tp, fp, fn, tn) = (obj['total'], obj['tp'], obj['fp'], obj['fn'], obj['tn'])

# 		precision = tp / (tp + fp)
# 		recall = tp / (tp + fn)
# 		accuracy = (tp + tn) / total
# 		f1 = (2 * precision * recall) / (precision + recall)

# 		print('Mode:', mode)
# 		print('Total:', str(total))
# 		print('True Positive:', str(tp))
# 		print('False Positive:', str(fp))
# 		print('True Negative:', str(tn))
# 		print('False Negative:', str(fn))
# 		print('Precision:',str(precision))
# 		print('Recall:',str(recall))
# 		print('Accuracy:' + str(accuracy))
# 		print('F1:' + str(f1))
# 		print('-----------------------------------------------------------------------------------')

# validate_test('testSet.csv', modesArr = ['飲食', '交通', '娛樂'])

