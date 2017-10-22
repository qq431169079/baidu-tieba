#!usr/bin/env python
# -*- coding: utf-8 -*-


class URL(object):
    @classmethod
    def loging_url():
        return "https://passport.baidu.com/v2/api/?login"
    @classmethod
    def token_url(tt, gid, callback):
        tokenurl = '''https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3\
&tt=%s&class=login&gid=%s&logintype=basicLogin&callback=%s'''%(tt, gid, callback)
        return tokenurl
    @classmethod
    def pubkey_url(token, tt, gid, callback):
        pubkeyurl = '''https://passport.baidu.com/v2/getpublickey?token=%s&class\
%s&tpl=pp&apiver=v3&tt=%s&gid=%s&callback=%s'''%(token,tt,gid,callback)
        return pubkey_url