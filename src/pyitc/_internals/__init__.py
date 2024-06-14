try:
    from .._pyitc import ffi as _ffi
    from .._pyitc import lib as _lib
except ImportError: # pragma: no cover
    raise ImportError("pyitc C extension import failed, cannot use C-API")
