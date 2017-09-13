# -*- coding: utf-8 -*-
import jieba
import os
basedir = "/home/joe/share/text_classifier/THUCNews/"
dir_list = ['affairs','constellation','economic','edu','ent','fashion','game','home','house','lottery','science','sports','stock']
##生成fastext的训练和测试数据集

ftrain = open("news_fasttext_train1.txt","w")
ftest = open("news_fasttext_test1.txt","w")
stopwords = open('stop_words.txt','r',encoding='utf8').readlines()
stopwords = [w.strip() for w in stopwords]
jieba.enable_parallel(2)
num = -1
for e in dir_list:
    num += 1
    indir = basedir + e + '/'
    print(indir)
    files = os.listdir(indir)
    count = 0
    for file in files:
        count += 1            
        filepath = indir + file
        with open(filepath,'r',encoding='utf-8') as fr:
            text = fr.read()
        seg_text = jieba.cut(text.replace("\t"," ").replace("\n"," "))
        outline = " ".join(filter(lambda x: x not in stopwords and len(x)>1, list(seg_text)))
        outline = str(outline) + ("\t__label__") + (e) + ("\n")
        if count < 10000:
            ftrain.write(outline)
            ftrain.flush()
            continue
        elif count  < 20000:
            ftest.write(outline)
            ftest.flush()
            continue
        else:
            break

ftrain.close()
ftest.close()