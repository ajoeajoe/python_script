# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import jieba
#a=''
jieba.enable_parallel(4)
a = open('zhwiki.sim.utf8','r',encoding='utf8')

output = open('wiki_mul.txt','w+',encoding='utf8')

line = a.readline()

print(line)

while line!="" and len(line)>=5:
  
  stopwords = open('stop_words.txt','r',encoding='utf8').readlines()
  
  stopwords = [w.strip() for w in stopwords]

  #l = list(jieba.cut(line,cut_all=False))
  
  #print(l)

  #result = ''
  #print(type(list(jieba.cut(line))))
  
  #result  =" ".join(w for w in l if w not in stopwords and w!=" ")
  
  result = " ".join(filter(lambda x: x not in stopwords and len(x.strip())>0, list(jieba.cut(line))))
  
  print(result)
  
  line = a.readline()

  output.write(str(result+'\n'))
a.close()
output.close()
print ('处理完成')