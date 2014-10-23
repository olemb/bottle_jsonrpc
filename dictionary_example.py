#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

# Fix paths
# rootdir = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(rootdir)
# os.chdir(rootdir)

import bottle
import bottle_jsonrpc

@bottle.route('/')
def index():
    return bottle.static_file('example.html', os.getcwd())

def add(self, a, b):
    return a + b

def sort(self, lst):
    return sorted(lst)

jsonrpc = bottle_jsonrpc.register('/rpc')
jronrpc.methods = {'add', add,
                   'sort': sort}

bottle.debug(True)

if __name__ == '__main__':
    # Standalone web server
    bottle.run(reloader=True)
else:
    # Running under WSGI (probably apache)
    application = bottle.default_app()
