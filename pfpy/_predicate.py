from collections.abc import Callable
from functools import update_wrapper

__all__ = ["Predicate", "predicate"]

class Predicate(Callable):
    """Represent a predicate function."""

    def __init__(self, f):
        """Create a new Predicate to represent predicate function f."""
        self._f = f

    # === Implement Callable ===
    def __call__(self, obj):
        return self._f(obj)

    # === Unary operators ===
    def __invert__(self):
        return Predicate(lambda x: not self(x))

    # === Binary operators ===
    def __and__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: self(x) and other(x))

    def __or__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: self(x) or other(x))

    # === Reflected binary operators ===
    def __rand__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: other(x) and self(x))

    def __ror__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: other(x) or self(x))

def predicate(f):
    """Decorator that lifts a predicate function into a Predicate."""
    wrapper = Predicate(f)
    update_wrapper(wrapper, f)
    return wrapper
