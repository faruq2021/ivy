"""
Collection of Jax general functions, wrapped to fit Ivy syntax and signature.
"""

# global
import jax as _jax
import math as _math
import numpy as _onp
import jax.numpy as _jnp
import jaxlib as _jaxlib
from numbers import Number
from operator import mul as _mul
from functools import reduce as _reduce
from jaxlib.xla_extension import Buffer
import multiprocessing as _multiprocessing
from haiku._src.data_structures import FlatMapping

# local
import ivy
from ivy.functional.ivy.device import default_device
from ivy.functional.ivy.old import default_dtype
from ivy.functional.backends.jax.device import to_dev, dev as callable_dev

# noinspection PyUnresolvedReferences,PyProtectedMember
def is_array(x, exclusive=False):
    if exclusive:
        return isinstance(x, (_jax.interpreters.xla._DeviceArray,
                              _jaxlib.xla_extension.DeviceArray, Buffer))
    return isinstance(x, (_jax.interpreters.xla._DeviceArray,
                          _jaxlib.xla_extension.DeviceArray, Buffer,
                          _jax.interpreters.ad.JVPTracer,
                          _jax.core.ShapedArray,
                          _jax.interpreters.partial_eval.DynamicJaxprTracer))

copy_array = _jnp.array