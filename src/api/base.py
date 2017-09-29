#!usr/bin/env python
# -*- coding: utf-8 -*-



class TiebaApiBase(object):
'''
        该类为各api的基类
'''
    def _post(self, url, **opts):
        return self._session.post(url, **opts)
        
        
        
    def _get(self, url, **opts):
        return self._session.get(url, **opts)
        