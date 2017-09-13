# -*- coding: utf-8 -*-

import requests
from lxml import etree
import my_cookies
import re
def getweibo_content(user_id):
    
  try:

      my_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
                    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
      
      email=''
      mobie=''
      result=''
      QQ=''
      wechat=''
      print ('爬虫准备就绪...')
      
      url = 'http://weibo.cn/{}/info'.format(user_id)
      lxml = requests.get(url, cookies = my_cookies.__getCookies(my_cookies._my_weibo),headers=my_headers).content
         #文字爬取
      selector = etree.HTML(lxml)
      content = selector.xpath('//div[@class="c"]')
      write=open("tag2.txt", 'a',encoding='utf-8')
      con="".join(content[2].xpath('string(.)'))

      email = str(re.findall('[a-zA-Z0-9._]{1,}\@[0-9a-zA-Z.]*', con))
      mobie=str(re.findall('1[0-9]{10}|\d{3}-\d{8}|\d{4}-\d{7}',con))
      QQ=str(re.findall('Q.*[1-9][0-9]{4,15}|q.*[1-9][0-9]{4,15}',con))
      wechat=str(re.findall(r'微信.*[0-9a-zA-Z.]*标*|公众号.*[0-9a-zA-Z.]*标*|公号.*[0-9a-zA-Z.]*标*',con))
      
      result=str(user_id)+"~"+con+"~"+email+"~"+mobie+"~"+QQ+"~"+wechat+'\n'
      
      write.write(result)
      print(result)
      
      print (u'用户微博爬取完毕')
      
  except Exception as e:   
      print ("Error: {}".format(e))
  finally:    
      print (u'End GetWeiboContent with user_id {}\n'.format(user_id))
           
#主函数
if __name__ == '__main__':
 
    inforead = open("user2.txt", 'r')
    #user_id = int(inforead.readline())
    user_id="1"
    
    while user_id!="":
        
        user_id = int(inforead.readline().strip())
        getweibo_content(user_id)         
        print(user_id)
    inforead.close()
    #write.closed()