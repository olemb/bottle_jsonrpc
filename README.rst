A simple JSON-RPC implementation for Bottle
===========================================

``bottle_jsonrpc.py`` implements `JSON-RPC <http://json-rpc.org/>`_
for `Bottle <http://bottlepy.org/>`_ in a pretty straight forward way.

You can attach any object to a path. POST requests to that path will
then be treated as JSON-RPC calls. Each public callable method or
attribute of the object will be exposed as a method.


Example
-------

.. code-block:: python

    import bottle_jsonrpc

    jsonrpc = bottle_jsonrpc.register('/rpc')

    @jsonrpc
    def add(a, b):
        return a + b

Alternatively you can pass an object to ``register()``:

.. code-block:: python

    class Methods(object):
        def add(a, b):
            return a + b

    bottle_jsonrpc.register('/rpc', Methods())

All public methods (callable attributes that don't start with ``_``)
will be exported as JSON-RPC methods.

You can also manipulate the method dictionary directly:

.. code-block:: python

    def add(a, b):
        return a + b

    jsonrpc = bottle_jsonrpc.register('/rpc')
    jsonrpc.methods['add'] = add


Arguments to register()
-----------------------

Returns a ``NameSpace`` object that can also be used as a decorator.

path
  Path that the client will send requests to. This will
  be mounted in bottle with ``@post(path)``.

obj=None
  All public methods (callable attributes) of the object will
  be exported as JSON-RPC methods.

app=None
  App to use. Defaults to ``bottle.default_app()``.



NameSpace Attibutes
-------------------

path, app
  The values passed as arguments.

methods
  A dictionary of methods for lookup where name is the JSON-RPC methods name
  and value is a callable object (typically a function or method).


NameSpace Methods
-----------------

add_object(obj)
  Exports all public methods (callable attributes) of the object as JSON-RPC
  methods.


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
