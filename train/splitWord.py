# 分詞
import codecs
from jseg import Jieba
jieba = Jieba()

infile = 'wiki-zh-article-zht.txt'
outfile = 'wiki-zh-words.txt'

descsFile = codecs.open(infile, 'rb', encoding='utf-8')
i = 0
with open(outfile, 'w', encoding='utf-8') as f:
   for line in descsFile:
       i += 1
       if i % 10000 == 0:
           print(i)
       line = line.strip()
       words = jieba.seg(line)
       for word in words:
           f.write(word + ' ')
       f.write('\n')