# 德士、的士、巨業、經營業者
import pickle
from tqdm import tqdm
from gensim.models import Word2Vec

model = Word2Vec.load('./wiki-zh-model')

def genByOneKeyWord(keyword):
	a = model.most_similar(keyword, topn=40)

	filtered_a = []
	item = ''
	for x,c in a:
		item = input("[ " + "{0:<3s}".format(x) + " ] : ")
		if(item == '' or item == 'y'):
			filtered_a.append(x)

	fst_round = []
	for s in filtered_a:
		fst_round.append(s)

	snd_round = []
	for i in fst_round:
		k = model.most_similar(i, topn=10)
		for j,b in k:
			snd_round.append(j)


	result = {}
	for i in fst_round:
		if(i in result):
			result[i] = result[i] + 1
		else:
			result[i] = 0

	for j in snd_round:
		if(j in result):
			result[j] = result[j] + 1
		else:
			result[j] = 0
	return result


# transportation_class = ['車','轎車','火車','捷運','公車','計程車','通勤','交通']
# food_class = ['飯','麵','水果','蔬菜','飲料','肉','食物','食','素食','速食','甜點']
play_class = ['電影','音樂會','旅遊','舞劇','球賽','遊戲','娛樂','小說','漫畫']
train_class = play_class

res = {}

# for x in tqdm(transportation_class):
# 	res.update(genByOneKeyWord(x))
for x in tqdm(train_class):
	res.update(genByOneKeyWord(x))

# output_pkl = open('transportation_class.pkl', 'wb')
output_pkl = open('play_class.pkl', 'wb')
pickle.dump(res, output_pkl)
output_pkl.close()

# output_txt = open('transportation_class.txt', 'w')
output_txt = open('play_class.txt', 'w')
for key, item in res.items():
	output_txt.write(key + ',' + str(item) + '\n')
output_txt.close()

