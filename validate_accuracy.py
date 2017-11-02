from tqdm import tqdm
from splitProcess import outputRes
from gensim.models import Word2Vec

model = Word2Vec.load('./wiki-zh_news-model')

# 食物, 交通mode
def validate_test(filePath, mode):
	testDic = {}
	print('Start loading testSet..')
	with open(filePath) as f:
		for line in f:
			try:
				(itemId, category, itemName) = line.split(',')
				itemName = itemName.replace('\n', '')
				testDic[itemName] = category
			except:
				# total += 1
				print('[Debug] line #' + total)
	print('testSet loaded.')

	(total, tp, fp, tn, fn) = (len(testDic.items()), 0, 0, 0, 0)
	for itemName, category in tqdm(testDic.items()):
		predictCategory = outputRes(itemName)['category']
		if(category == predictCategory and category == mode):
			tp += 1
		elif(category == predictCategory and category != mode):
			tn += 1
		elif(category != predictCategory and predictCategory == mode):
		  fp += 1
		elif(category != predictCategory and category == mode):
		# else:
			fn += 1

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

validate_test('testSet.csv', '飲食')
validate_test('testSet.csv', '交通')
