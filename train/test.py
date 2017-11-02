# 看看效果
from gensim.models import Word2Vec

model = Word2Vec.load('../wiki-zh-model')
model_new = Word2Vec.load('../wiki-zh_news-model')
#model = Word2Vec.load_word2vec_format('./wiki-zh-vector', binary = False) # 如果之前用文本保存話， 用這個方法加載
print(model.most_similar('食物'))
print(model_new.most_similar('食物'))

