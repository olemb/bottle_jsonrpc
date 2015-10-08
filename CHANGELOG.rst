0.2.1 - 2015-10-08
------------------

* Params are now optional as required by the JSONRPC
specification. (Patch by Kirill Grushetsky.)

* now takes into account bottle's app.catchall setting while handling
  exceptions. (Patch by Kirill Grushetsky.)


0.2.0 - 2014-10-23
------------------

* rewrote entire library.

* added decorators.

* methods are now stored in a dictionary instead of being looked
  up directly on the object. This allows for a lot more flexibility.


0.1.0
-----

Initial version.
