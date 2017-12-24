from pfpy._function import Function
from pfpy._predicate import Predicate
from functools import update_wrapper, partial

__all__ = ["rpartial", "curry", "rcurry"]

def rpartial(f, *args):
    """
    Return f with arguments bound from the right.
    Similar to functools.partial but in reverse.
    """
    return lambda *a: f(*(a + args))

def curry(n, cls=Function):
    """
    Decorator that transforms an n-ary function into a sequence of n unary functions
    that partially applies the arguments of the original function from left to right.
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

def rcurry(n, cls=Function):
    """
    Decorator that transforms an n-ary function into a sequence of n unary functions
    that partially applies the arguments of the original function from right to left.
    Each unary function will be of type Function except for the last one which will
    be of type cls.
    """
    def rcurry(f):
        def rcurry(g, n):
            if n == 0:  # No parameters. Pass in dummy argument in order to call function.
                wrapper = cls(lambda x: g())
            elif n == 1:  # 1 parameters left. Pass in argument to call function with.
                wrapper = cls(lambda x: g(x))
            else:  # >1 parameters left. Pass in argument for first unbound parameter in function.
                wrapper = Function(lambda x: rcurry(rpartial(g, x), n - 1))
            update_wrapper(wrapper, f)
            return wrapper
        return rcurry(f, n)
    return rcurry
