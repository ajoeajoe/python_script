# -*- coding: utf-8 -*-
import json
import base64
import requests
import random

class WeiboAccount:
    def __init__(self, no, psw):
        self.no = no
        self.psw = psw

_my_weibo = [
    WeiboAccount('13902879682', '184275875Ye'),
    WeiboAccount('13726224248', 'a12345'),
    WeiboAccount('13712549603', 'a123456'),
    WeiboAccount('13417321673', 'a123456'),
    WeiboAccount('13486433816', 'a123456')
]

def __getCookies(weibo):
    """ 获取Cookies """
    cookies = []
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    for elem in weibo:
        account = elem.no
        password = elem.psw
        username = base64.b64encode(account.encode('utf-8')).decode('utf-8')
        postData = {
            "entry": "sso",
            "gateway": "1",
            "from": "null",
            "savestate": "30",
            "useticket": "0",
            "pagerefer": "",
            "vsnf": "1",
            "su": username,
            "service": "sso",
            "sp": password,
            "sr": "1440*900",
            "encoding": "UTF-8",
            "cdult": "3",
            "domain": "sina.com.cn",
            "prelt": "0",
            "returntype": "TEXT",
        }
        session = requests.Session()
        r = session.post(loginURL, data=postData)
        jsonStr = r.content.decode('utf-8')
        info = json.loads(jsonStr)
        if info["retcode"] == "0":
            #print("Get Cookie Success!( Account:%s )" % account)
            cookie = session.cookies.get_dict()
            cookies.append(cookie)
        else:
            print("Failed!( Reason:%s )" % info['reason'])
    return random.choice(cookies)
    
#cookies = __getCookies(_my_weibo)
#print(cookies)
