A simple JSON-RPC implementation for Bottle
===========================================

Usage
-----

.. code-block:: python

    import bottle_jsonrpc

    class Methods(object):
        def add(self, a, b):
             return a + b

    bottle_jsonrpc.register('/math', Methods())

``register()`` takes an optional ``app`` argument::

.. code-block:: python

    app = bottle.Bottle()

    bottle_jsonrpc.register('/math', Methods(), app=app)


References
----------

http://json-rpc.org/

http://bottlepy.org/
