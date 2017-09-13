# coding:utf-8
import logging
from gensim.models import Word2Vec
import time
from gensim.models.word2vec import LineSentence
start = time.time()
#提前加载
logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s", level=logging.INFO)

model = Word2Vec.load('O:/test/wiki/word2vector2.model')
#新的语料库
new_corpus = LineSentence('all.copy')
print(new_corpus)
#训练新的语料
#model.build_vocab(new_corpus)

model.train(new_corpus)
#将其进行保存
model.save('word2vector3.model')
#model.save_word2vec_format('word2vector4.bin', binary = False)
#model = Word2Vec.load_word2vec_format('word2vector4.bin', binary = False)
model = Word2Vec.load('word2vector3.model')
print(time.time()-start)
print(model['中国'])
#==============================================================================
# print(model.most_similar('沐浴', topn=10))
# w = 'T恤'
# if w in model:
#     print (w)
# else:
#     print('None')
#==============================================================================
