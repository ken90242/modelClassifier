from gensim.models import Word2Vec
model = Word2Vec.load('train/wiki-zh-model')

sample_path = 'sampling/'
# sample_path = 'train/generate_category_keyWord/'
def readClasses():
	food_ref = []
	with open(sample_path + 'food_class.txt', 'r') as f:
		for line in f:
			(name, num) = line.split(',')
			food_ref.append(name)

	clothes_ref = []
	with open(sample_path + 'clothes_class.txt', 'r') as f:
		for line in f:
			(name, num) = line.split(',')
			clothes_ref.append(name)

	live_ref = []
	with open(sample_path + 'live_class.txt', 'r') as f:
		for line in f:
			(name, num) = line.split(',')
			live_ref.append(name)

	go_ref = []
	with open(sample_path + 'go_class.txt', 'r') as f:
		for line in f:
			(name, num) = line.split(',')
			go_ref.append(name)

	education_ref = []
	with open(sample_path + 'education_class.txt', 'r') as f:
		for line in f:
			(name, num) = line.split(',')
			education_ref.append(name)
	play_ref = []
	with open(sample_path + 'play_class.txt', 'r') as f:
		for line in f:
			(name, num) = line.split(',')
			play_ref.append(name)
	return (food_ref, clothes_ref, live_ref, go_ref, education_ref, play_ref)

def getSim(ref, query):
	res = 0.0
	count = 0
	for item in ref:
		try:
			res += model.similarity(item, query)
			count += 1
		except Exception as ex:
			continue
	if(count == 0):
		return 0.0
	else:
		return res/count

def outPutCate(query):
	(food_ref, clothes_ref, live_ref, go_ref, education_ref, play_ref) = readClasses()
	try:
		cate = {}
		threshold = 0.0
		a = getSim(food_ref, query)
		b = getSim(clothes_ref, query)
		c = getSim(live_ref, query)
		d = getSim(go_ref, query)
		e = getSim(education_ref, query)
		f = getSim(play_ref, query)
		g = 0.0000000001

		cate[a] = '飲食'
		cate[b] = '衣飾'
		cate[c] = '居住'
		cate[d] = '交通'
		cate[e] = '教育'
		cate[f] = '娛樂'
		cate[g] = '其他'

		estimate = max([a, b, c, d, e, f, g])

		res = '其他'
		if(estimate > threshold):
			res = cate[estimate]
		else:
			print(query,' / ',cate)
		return (res, cate)
	except Exception as ex:
		print(ex)
		return ('找不到', cate)
