from gensim.models import Word2Vec
model = Word2Vec.load('./wiki-zh-model')

def getSim(ref, query):
	res = 0.0
	count = 0
	for item in ref:
		res += model.similarity(item, query)
		count += 1
	return res/count

def outPutCate(query):
	try:
		cate = {}
		threshold = 0.05
		a = getSim(food_ref, query)
		b = getSim(transportation_ref, query)
		c = getSim(play_ref, query)

		cate[a] = '飲食'
		cate[b] = '交通'
		cate[c] = '娛樂'

		estimate = max([a, b, c])

		res = '其他'
		if(estimate > threshold):
			res = cate[estimate]
		return (res, cate)
	except:
		return ('其他', cate)


food_ref = []
with open('train/generate_category_keyWord/food_class.txt', 'r') as f:
	for line in f:
		(name, num) = line.split(',')
		food_ref.append(name)

transportation_ref = []
with open('train/generate_category_keyWord/transportation_class.txt', 'r') as f:
	for line in f:
		(name, num) = line.split(',')
		transportation_ref.append(name)

play_ref = []
with open('train/generate_category_keyWord/play_class.txt', 'r') as f:
	for line in f:
		(name, num) = line.split(',')
		play_ref.append(name)
