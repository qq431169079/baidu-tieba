#!usr/bin/env python
# -*- coding: utf-8 -*-


import requests
import setting
import time
import rsa
import base64
from .url import URL




class Login(URL):
'''
    该类为百度贴吧的登录类
'''

    
    def __init__(self):
        self._session = requests.Session()
        self._token = None
        self._inittime = ""
        self._gid = self.gid
        self._callback = self.callback
        self.headers = {
                    'User-Agent': setting.agent,
                    "Host": "passport.baidu.com",
                    "Referer": "https://www.baidu.com/"
            }
  
    def get_token(self, flag = True):
        if self._token and flag:
            return self._token
        
        token_callback = self.callback
        self._inittime = str(int(time.time() * 1000))
        token_url = Login.token_url(self._inittime, self._gid, self._callback)
        # token_params = {
        #     "getapi": "",
        #     "tpl": "pp",
        #     "apiver": "v3",
        #     "tt": str(int(time.time() * 1000)),
        #     "class": "login",
        #     "gid": gid,
        #     "logintype": "dialogLogin",
        #     "callback": get_callback()
        # }
        try:
            token_html = session.get(token_url, headers=self.headers)
            token_content_all = token_html.text.replace(token_callback, "")
            token_content_all = eval(token_content_all)
            return token_content_all['data']['token']
        except:
            return None
        
    def get_pubkey(self,token, tt, gid, callback):
        pubkeyurl = Login.pubkey_url(token, tt, gid, callback)
        try:
            self.headers["Referer"] = "https://passport.baidu.com/v2/?login"
            publickey_html = session.get(publickey_url, headers=self.headers)
            publickey_content_all = eval(publickey_html.text.replace(publickey_callback, ""))
            return publickey_content_all['pubkey'], publickey_content_all['key']
        except:
            return None, None
    def get_password(password_input, pubkey):
        pub = rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode("utf-8"))
        password_input = password_input.encode("utf-8")
        psword = rsa.encrypt(password_input, pub)
        psword = base64.b64encode(psword)
        return psword.decode("utf-8")

    def loging(self):
        time.sleep(random.randint(2, 5))
        callback3 = self.callback
        login_url = "https://passport.baidu.com/v2/api/?login"
        login_time = str(int(time.time() * 1000))
        data={
        'apiver':'v3',
        'charset':'utf-8',
        'countrycode':'',
        'crypttype':12,
        'detect':1,
        'foreignusername':'',
        'idc':'',
        'isPhone':'',
        'logLoginType':'pc_loginBasic',
        'loginmerge':True,
        'logintype':'basicLogin',
        'mem_pass':'on',
        'quick_user':0,
        'safeflg':0,
        'staticpage':'http://yun.baidu.com/res/static/thirdparty/pass_v3_jump.html',
        'subpro':'netdisk_web',
        'tpl':'netdisk',
        'u':'http://yun.baidu.com/',
        'username':'xxxxxxxx@qq.com',
        'callback':'parent.'+callback3,
        'gid':gid,
        'password':password,
        'ppui_logintime':71755,
        'rsakey':key,
        'token':token,
        'tt':'%d'%(time.time()*1000),
    }
    @property      
    def gid(self):
        gid = "xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx"
        gid = list(gid)
        for xy in range(len(gid)):
            if gid[xy] in "xy":
                r = int(random.random()*16)
                if gid[xy] == "x":
                    gid[xy] = hex(r).replace("0x", '').upper()
                else:
                    gid[xy] = hex(r & 3 | 8).replace("0x", '').upper()
            else:
                pass
        return ''.join(gid)
    @property 
    def callback(self):
        loopabc = '0123456789abcdefghijklmnopqrstuvwxyz'
        prefix = "bd__cbs__"
        n = math.floor(random.random() * 2147483648)
        a = []
        while n != 0:
            a.append(loopabc[int(n % 36)])
            n = n // 36
        a.reverse()
        return prefix + ''.join(a)
    
