# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 15:06:09 2017

@author: joe
"""
from gensim.models import Word2Vec  
from gensim.models.word2vec import LineSentence  
import multiprocessing  
import time
_author__ = 'joe'  
# read the txt  
# word2vec it  
# save it as model and vector 
  
def my_function():  
    a = open('wiki_mul.txt', 'r',encoding='utf-8')  
    #f_1 = open('zhiwiki_news.model', 'w')  
    #f_2 = open('zhiwiki_news.vector', 'w')  
    model = Word2Vec(LineSentence(a), size=400, window=5, min_count=5, workers=multiprocessing.cpu_count()-4)  
    model.save('word2vector_with_LineSentence.model')  
    #model.save_word2vec_format('word2vector_with_LineSentence.vector', binary=False)
if __name__ == '__main__':
    start = time.time()
    my_function()
    print(time.time()-start)
