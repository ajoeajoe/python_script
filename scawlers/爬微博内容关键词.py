# -*- coding: utf-8 -*-
from jieba import analyse
from xlutils.copy import copy
import xlrd
import requests
from lxml import etree
import time
import my_cookies

def getweibo_content(user_id):
    
  try:
      my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
      url = 'http://weibo.cn/u/{0}?filter=0&page=1'.format(user_id)
      html = requests.get(url, cookies = my_cookies.__getCookies(my_cookies._my_weibo),headers=my_headers).content
      selector = etree.HTML(html)
      pageNum = selector.xpath('//input[@name="mp"]')[0].attrib['value']
      print(pageNum)
      if(int(pageNum)>10): 
         pageNum=10
      else :
         pageNum=pageNum  
      result = "" #微博内容字段
      rz= "" #认证字段
      print ('爬虫准备就绪...')
      for page in range(1,pageNum+1):
        url = 'http://weibo.cn/u/{0}?filter=0&page={1}'.format(user_id,page) 
        lxml = requests.get(url, cookies = my_cookies.__getCookies(my_cookies._my_weibo),headers=my_headers).content
         #文字爬取
        selector = etree.HTML(lxml)
        content = selector.xpath('//span[@class="ctt"]')
        
        if (page==1):
         print (content[1].xpath('string(.)'))
         rz=content[1].xpath('string(.)')
        else:
            pass
        
        for each in content:
          
          text =each.xpath('string(.)')
          result = result + text
        '''
        for each in content:
          
          text = each.xpath('string(.)')
          result = result + text
          if word_count>= 4:
            text = "%d :"%(word_count-3) +text+"\n\n"
          else :
            text = text+"\n\n"
          result = result + text
          word_count += 1
        '''
      #把微博内容写入文件
      #print(len(user_id))
      #tostr=(str(user_id)).strip()#去掉左右空格
      #fo = open("{}.txt".format(tostr), "w",encoding='utf-8')
      #fo.write(result)
      #把所爬内容写入Exel
      book= xlrd.open_workbook("we.xls", formatting_info=True)
      sheet=book.sheet_by_index(0)
      
      newWb = copy(book)
      newWs = newWb.get_sheet(0)
      newWs.write(sheet.nrows,0,user_id)
    
      newWs.write(sheet.nrows,1,rz)   
      #停用词
      analyse.set_stop_words('stop_words.txt')
      #只输出Top20关键词
      my_string=''    
      for x in analyse.textrank(result, topK=20):#用Textrank算法进行分词
        my_string = my_string +str(x)+" "
      newWs.write(sheet.nrows,2,my_string)
      #输出Top20关键词及其权重
      my_str=''
      for x in analyse.textrank(result, topK=20,withWeight = True):
        my_str = my_str +str(x)+" "
      newWs.write(sheet.nrows,3,my_str)
      print(str(user_id).strip()+''+my_str)
      newWb.save("we.xls")
    
  except Exception as e:   
      print ("Error: {}".format(e))
  finally:    
      print (u'End GetWeiboContent with user_id {}\n'.format(user_id))
           
#主函数
if __name__ == '__main__':
 
    inforead = open("user.txt", 'r',encoding='utf-8')#读书微博账户id
    user_id = int(inforead.readline().strip())
    
    while user_id!="":
        time.sleep(1)
        getweibo_content(user_id)         
        user_id = inforead.readline()
    inforead.close()
    