import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

inp = 'wiki-zh-words.txt'
outp1 = 'wiki-zh-model'
outp2 = 'wiki-zh-vector'

print('Start training word2vec...')
model = Word2Vec(LineSentence(inp), size = 400, window = 5, min_count = 5, workers = multiprocessing.cpu_count())

model.save(outp1) ## 以二進制格式存儲
#model.save_word2vec_format(outp2, binary = False) ## 以文本格式存儲， 一行是一個詞的vector