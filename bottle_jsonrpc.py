# -*- coding: utf-8 -*-
"""
Very minimal implementation of JSON-RPC for Bottle.
"""

from __future__ import unicode_literals, print_function

import os
import sys
import traceback
import bottle

def register(path, obj):
    """
    Register object (any namespace will do) for JSON-RPC.
    """

    @bottle.post(path)
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
                'id' : req['id'],
                'result' : result,
                'error' : None,
                }
        except:
            traceback.print_exc(file=sys.stderr)
            return { 
                'id' : req['id'],
                'result' : None,
                'error' : traceback.format_exc(),
                }
