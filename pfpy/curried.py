from pfpy._predicate import Predicate
from pfpy._curry import curry, rcurry
from operator import *
from functools import reduce

predicate_operators = ["lt", "le", "eq", "ne", "ge", "gt", "is_", "is_not", "contains"]
regular_operators =  ["add", "sub", "floordiv", "truediv", "mul", "matmul", "mod", "pow",
                       "and_", "or_", "xor", "lshift", "rshift",
                       "concat", "countOf", "getitem", "indexOf"]
builtins = ["map", "filter", "reduce", "getattr"]

__all__ = predicate_operators + regular_operators + builtins

# Reassign each operator to their appropriately curried version
(lt, le, eq, ne, ge, gt, is_, is_not, contains) = (rcurry(2, Predicate)(eval(op)) for op in predicate_operators)
(add, sub, floordiv, truediv, mul, matmul, mod, pow,
 and_, or_, xor, lshift, rshift,
 concat, countOf, getitem, indexOf) = (rcurry(2)(eval(op)) for op in regular_operators)

# Reassign each builtin to their appropriately curried version
(map, filter, reduce) = (curry(2)(eval(f)) for f in builtins[:3])
getattr = rcurry(2)(eval("getattr"))
