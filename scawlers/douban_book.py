# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 19:14:23 2017

@author: joe
"""

import urllib

import urllib.request

import json

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['book']
collection = db.douban_book
book = db.commodity

def getInfoFromDouban(isbn):
    try:
        #将isbn作为变量传递到url中，得到对应的地址
        url = 'https://api.douban.com/v2/book/isbn/'+str(isbn)
        #使用urllib模块打开url
        response = urllib.request.urlopen(url)
        #读取url的网页内容，并用utf8编码
        result = response.read().decode('utf8')
        #将返回的字符串转成json格式
        result_json = json.loads(result,encoding='utf-8')
        #信息获取失败，抛出一个异常
    
    except urllib.error.HTTPError as e:
        raise e
    return result_json
    
if __name__ == '__main__':


   for i in book.find({},{'isbn':1,'_id':0}):
       
      print(i['isbn'])
      
      try:
          
       bookinfo = getInfoFromDouban(i['isbn'])
       
      except Exception:
          
            continue 
        
      print(bookinfo)
      
      print(type(bookinfo))
      
      collection.insert_one(bookinfo)
'''      
 
if __name__ == '__main__':
    
   bn = open('douban.txt','r')

   line = bn.readline()


   while line!="" and len(line)>=2:
       
      print(line)
      
      bookinfo = getInfoFromDouban(line)
      
      print(type(bookinfo))
      
      collection.insert_one(bookinfo)
      
      print(bookinfo)
            
      line = bn.readline()
      
      print(line)
'''  