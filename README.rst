A simple JSON-RPC implementation for Bottle
===========================================

``bottle_jsonrpc.py`` implements `JSON-RPC <http://json-rpc.org/>`_
for `Bottle <http://bottlepy.org/>`_ in a pretty straight forward way.

You can attach any object to a path. POST requests to that path will
then be treated as JSON-RPC calls. Each public callable method or
attribute of the object will be exposed as a method.


Usage
-----

.. code-block:: python

    import bottle_jsonrpc

    class Methods(object):
        def add(self, a, b):
            return a + b

    bottle_jsonrpc.register('/math', Methods())

``register()`` takes an optional ``app`` argument:

.. code-block:: python

    app = bottle.Bottle()

    bottle_jsonrpc.register('/math', Methods(), app=app)


License
--------

Released under the terms of the `MIT license
<http://en.wikipedia.org/wiki/MIT_License>`_.


Contact
--------

Ole Martin Bjorndalen - ombdalen@gmail.com
