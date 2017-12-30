from pfpy._predicate import Predicate
from pfpy._curry import curry, rcurry
from operator import *
from functools import reduce
from itertools import groupby

predicate_operators = ["lt", "le", "eq", "ne", "ge", "gt", "is_", "is_not", "contains"]
regular_operators =  ["add", "sub", "floordiv", "truediv", "mul", "matmul", "mod", "pow",
                       "and_", "or_", "xor", "lshift", "rshift",
                       "concat", "countOf", "getitem", "indexOf"]
builtins = ["map", "filter", "reduce"]
reverse_builtins = ["getattr", "groupby"]
keyword_builtins = ["sorted", "max", "min"]

__all__ = predicate_operators + regular_operators + builtins + reverse_builtins + keyword_builtins + ["apply"]

# Reassign each operator to their appropriately curried version
(lt, le, eq, ne, ge, gt, is_, is_not, contains) = (rcurry(2, Predicate)(eval(op)) for op in predicate_operators)
(add, sub, floordiv, truediv, mul, matmul, mod, pow,
 and_, or_, xor, lshift, rshift,
 concat, countOf, getitem, indexOf) = (rcurry(2)(eval(op)) for op in regular_operators)

# Reassign each built-in to their appropriately curried version
(map, filter, reduce) = (curry(2)(eval(f)) for f in builtins)
(getattr, groupby) = (rcurry(2)(eval(f)) for f in reverse_builtins)
(sorted, max, min) = (curry(3)(lambda f, key, iterable: f(iterable, key=key))(eval(f)) for f in keyword_builtins)

# Manually curry apply
@curry(2)
def apply(f, args):
    return f(*args)
