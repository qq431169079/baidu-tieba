#!usr/bin/env python
# -*- coding: utf-8 -*-


import requests

class Loging(object):
'''
    ����Ϊ�ٶ����ɵĵ�¼��
'''
    def __init__(self, username, pwd):
        self._username = username
        self._pwd = pwd
        self._session = requests.session()
    def get_token(self):
        pass
    def get_pubkey(self):
        pass
        
    def get_password(self):
        pass
    def loging(self):
        pass