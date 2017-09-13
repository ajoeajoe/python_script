# coding:utf-8
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time
start = time.time()
'''
class TextLoader(object):

    def __init__(self):
        pass

    def __iter__(self):
        input = open('all.txt','r',encoding ='utf-8')
        line = input.readline()
        counter = 0
        while line!=None and len(line)>=4:
            #print line
            segments = line.split(' ')
            yield  segments
            counter=counter+1
            if (counter==14):
                break
            else:
                pass
            print(counter)
            #print(line)
            line = input.readline()
'''            
s = open('all.txt','r',encoding ='utf-8')
sentences = LineSentence(s)
#sentences = TextLoader()
#print(sentences)
# 0=CBOW , 1= SkipGrams
size = 100
window = 5
min_count = 5
model = Word2Vec(sentences, sg = 0,window=window, min_count=min_count,size=size,workers=multiprocessing.cpu_count())
model.save('word2vector11.model')
#model.save_word2vec_format('word2vector11.model', binary=False)
print ('ok')
print(time.time()-start)

model = Word2Vec.load('word2vector11.model')

print(model.most_similar('T恤', topn=10))