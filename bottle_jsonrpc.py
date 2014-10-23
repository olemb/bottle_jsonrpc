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
__version__ = '0.1.0'

def register(path, obj, app=None):
    """Register object (any namespace will do) for JSON-RPC."""

    app = app or bottle.default_app()

    @app.post(path)
    def rpc():
        req = bottle.request.json

        try:
            name = req['method']

            # Ignore private methods
            if name.startswith('_'):
                raise AttributeError(name)

            # Get function
            f = getattr(obj, name)

            if not callable(f):
                raise AttributeError(name)

            # Call method
            if 'params' in req:
                result = f(*req['params'])
            else:
                result = f()

            return {
                'id': req['id'],
                'result': result,
                'error': None,
                }
        except:
            traceback.print_exc(file=sys.stderr)
            return { 
                'id': req['id'],
                'result': None,
                'error': traceback.format_exc(),
                }

