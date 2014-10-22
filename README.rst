A simple JSON-RPC implementation for Bottle
===========================================

``bottle_jsonrpc.py`` implements `JSON-RPC <http://json-rpc.org/>`_
for `Bottle <http://bottlepy.org/>`_ in a pretty straight forward way.

You can attach any object to a path. POST requests to that path will
then be treated as JSON-RPC calls. Each public callable method or
attribute of the object will be exposed as a method.


Usage
-----

Methods can be added in one of two ways. You can use decorators:

.. code-block:: python

    from bottle_jsonrpc import NameSpace

    jsonrpc = NameSpace('/rpc')

    @jsonrpc
    def add(a, b):
        return a + b

    @jsonrpc
    def sub(a, b):
        return a - b

or you can add an object to the namespace:
    
.. code-block:: python

    import bottle_jsonrpc

    bottle_jsonrpc.register()

.. code-block:: python

    class Methods(object):
        def add(self, a, b):
            return a + b

    bottle_jsonrpc.register('/math', Methods())

``register()`` takes an optional ``app`` argument:

.. code-block:: python

    app = bottle.Bottle()

    bottle_jsonrpc.register('/math', Methods(), app=app)


Status
------

Should be considered experimental.

Error reporting (back to the JavaScript client) is not very good.


License
--------

Released under the terms of the `MIT license
<http://en.wikipedia.org/wiki/MIT_License>`_.


Contact
--------

Ole Martin Bjorndalen - ombdalen@gmail.com
