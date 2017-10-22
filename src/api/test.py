# -*- coding: utf-8 -*-
import urllib2
import time
import requests

url = "https://passport.baidu.com/v2/api/"
data = {"getapi":"",
"tpl":"mn",
"apiver":"v3",
"tt":str(time.time()*1000),
"class":"login",
"gid":"4A2DE52-6106-43FA-9FC9-437EEC5B3927",
"logintype":"dialogLogin",
"callback":"bd__cbs__rj3r0i",
}



#req = urllib2.Request(url, data = data, headers = headers)
#esponse = urllib2.urlopen(req)
#print response.read()
def get_token():
        session = requests.Session()
        a = session.get("http://www.baidu.com")
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
"Host": "passport.baidu.com",
"Referer": "https://www.baidu.com/"}
        token_callback = "bd__cbs__rj3r0i"
        gid = "4A2DE52-6106-43FA-9FC9-437EEC5B3927"
        _inittime = str(int(time.time() * 1000))
        token_url = "https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&tt="
        token_url = token_url + _inittime + "&class=login&gid="
        token_url = token_url + gid + "&logintype=basicLogin&callback="
        token_url = token_url + token_callback
        a = session.get("http://www.baidu.com", headers=headers)
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
        #print dir(a.cookies)
       
            
        #b =  "".join(["=".join(item) for item in a.cookies])
        token_html = session.get(token_url, headers=headers)
        #print token_html.text.encode("utf-8")
        token_content_all = token_html.text.replace(token_callback, "")
        token_content_all = eval(token_content_all)
        return token_content_all['data']['token']

        
print get_token()
