import string
import jieba.posseg as pseg
from classProcess import outPutCate

stopWords = []
with open('stopwords_zhTw.txt') as f:
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
	it = pseg.cut(query)
	itemName = ''
	for i in it:
		word = i.word
		flag = i.flag

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
			# if(category == '其他'):
				# print(word,'  |  ' ,weightsObj)

	candidates = {}
	for (cate, flag) in cates:
		if(cate in candidates):
			flag_arr = candidates[cate]
			flag_arr.append(flag)
		else:
			flag_arr = [flag]
		candidates[cate] = flag_arr

	res['category'] = vote(candidates)
	res['item'] = itemName.strip()
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