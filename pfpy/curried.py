from pfpy._predicate import Predicate
from pfpy._curry import rcurry
from operator import *

predicate_operators = ["lt", "le", "eq", "ne", "ge", "gt", "is_", "is_not", "contains"]
regular_operators =  ["add", "sub", "floordiv", "truediv", "mul", "matmul", "mod", "pow",
                       "and_", "or_", "xor", "lshift", "rshift",
                       "concat", "countOf", "getitem", "indexOf"]

__all__ = predicate_operators + regular_operators

# Reassign each operator to their reverse curried version
(lt, le, eq, ne, ge, gt, is_, is_not, contains) = (rcurry(2, Predicate)(eval(op)) for op in predicate_operators)
(add, sub, floordiv, truediv, mul, matmul, mod, pow,
 and_, or_, xor, lshift, rshift,
 concat, countOf, getitem, indexOf) = (rcurry(2)(eval(op)) for op in regular_operators)
