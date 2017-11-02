# 看看效果
from gensim.models import Word2Vec

model = Word2Vec.load('./wiki-zh-model')
#model = Word2Vec.load_word2vec_format('./wiki-zh-vector', binary = False) # 如果之前用文本保存話， 用這個方法加載
res = model.most_similar('車')
print(res)
#item = ''
#while(item != 'exit'):
#    item = input('Enter item name (input \'exit\' to exit): ')
#    try:
#        print('Food probability:', model.similarity(item, 'food'))
#        print('食物 probability:', model.similarity(item, '食物'))
#        print('Entertainment probability:', model.similarity(item, 'entertainment'))
#        print('娛樂 probability:', model.similarity(item, '娛樂'))
#        print('日常用品 probability:', model.similarity(item, '日常用品'))
#        print('Education probability:', model.similarity(item, 'education'))
#        print('教育 probability:', model.similarity(item, '教育'))
#    except:
#        print('找不到QQ')
