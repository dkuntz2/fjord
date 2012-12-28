# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class FjordException(Exception):
    code = 1
    
    
    def __init__(self, message, *args):
        self.message = message
        self.debug = args
    
    
    def __str__(self):
        return unicode(self).encode('utf-8')
    
    def __unicode__(self):
        message = '!! {0}'.format(self.message)
        
        for d in self.debug:
            message += '\n..  {0}'.format(d)
        
        return message


class OptionException(FjordException):
    code = 2

class ConfigException(FjordException):
    pass

class ParserException(FjordException):
    pass

class PostException(FjordException):
    pass

class RendererException(FjordException):
    pass
