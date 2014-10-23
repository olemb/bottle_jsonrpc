# -*- coding: utf-8 -*-
"""
Very minimal implementation of JSON-RPC for Bottle.
"""
from __future__ import unicode_literals, print_function

import os
import sys
import traceback
import bottle

__author__ = 'Ole Martin Bjorndalen'
__email__ = 'ombdalen@gmail.com'
__url__ = 'http://github.com/olemb/bottle_jsonrpc/'
__license__ = 'MIT'
__version__ = '0.2.0'

class NameSpace:
    def __init__(self, path, obj=None, app=None):
        self.path = path
        self.app = app or bottle.default_app()
        self.methods = {}

        if obj is not None:
            self.add_object(obj)

        self._make_handler()

    def add_object(self, obj):
        """Adds all public methods of the object."""
        for name in dir(obj):
            if name.startswith('_'):
                continue

            func = getattr(obj, name)
            if not callable(func):
                continue

            self.methods[name] = func

    def _make_handler(self):
        """Sets up bottle request handler."""
        @self.app.post(self.path)
        def rpc():
            request = bottle.request.json
            
            try:
                name = request['method']
                func = self.methods[name]
                if 'params' in request:
                    result = func(*request['params'])

                return {
                    'id': request['id'],
                    'result': result,
                    'error': None,
                }                
            except:
                traceback.print_exc(file=sys.stderr)
                return { 
                    'id': request['id'],
                    'result': None,
                    'error': traceback.format_exc(),
                    }

    def __call__(self, func):
        """This is called when the mapper is used as a decorator."""
        self.methods[func.__name__] = func
        return func

register = NameSpace
