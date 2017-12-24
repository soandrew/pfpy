from pfpy._predicate import Predicate
from pfpy._curry import rcurry
from operator import *
from operator import pow as pow_

__all__ = ["lt", "le", "eq", "ne", "ge", "gt", "is_", "is_not", "contains",
           "add", "sub", "floordiv", "truediv", "mul", "matmul", "mod", "pow_",
           "and_", "or_", "xor", "lshift", "rshift",
           "concat", "countOf", "getitem", "indexOf"]

# Reassign each operator to their reverse curried version
(lt, le, eq, ne, ge, gt, is_, is_not, contains) = (rcurry(2, Predicate)(eval(op)) for op in __all__[0:9])
(add, sub, floordiv, truediv, mul, matmul, mod, pow_,
 and_, or_, xor, lshift, rshift,
 concat, countOf, getitem, indexOf) = (rcurry(2)(eval(op)) for op in __all__[9:])
