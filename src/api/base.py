#!usr/bin/env python
# -*- coding: utf-8 -*-



class TiebaApiBase(object):
'''
        ����Ϊ��api�Ļ���
'''
    def _post(self, url, **opts):
        return self._session.post(url, **opts)
        
        
        
    def _get(self, url, **opts):
        return self._session.get(url, **opts)
        