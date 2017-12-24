from pfpy._function import Function
from pfpy._predicate import Predicate
from functools import update_wrapper, partial

__all__ = ["curry"]

def curry(n, cls=Function):
    """
    Decorator that transforms an n-ary function into a sequence of unary functions.
    Each unary function will be of type Function except for the last one which will
    be of type cls.
    """
    def curry(f):
        def curry(g, n):
            if n == 0:  # No parameters. Pass in dummy argument in order to call function.
                wrapper = cls(lambda x: g())
            elif n == 1:  # 1 parameters left. Pass in argument to call function with.
                wrapper = cls(lambda x: g(x))
            else:  # >1 parameters left. Pass in argument for first unbound parameter in function.
                wrapper = Function(lambda x: curry(partial(g, x), n - 1))
            update_wrapper(wrapper, f)
            return wrapper
        return curry(f, n)
    return curry
