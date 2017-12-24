from collections.abc import Callable
from functools import update_wrapper

__all__ = ["Predicate", "predicate"]

class Predicate(Callable):
    """Represent a predicate function."""

    def __init__(self, f):
        """Create a new Predicate to represent predicate function f."""
        self._f = f

    # === Getters ===
    @property
    def f(self):
        """Return the predicate function this Predicate represents."""
        return self._f

    # === Implement Callable ===
    def __call__(self, obj):
        return self.f(obj)

    # === Unary operators ===
    def __invert__(self):
        return Predicate(lambda obj: not self.f(obj))

    # === Binary operators ===
    def __and__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda obj: self.f(obj) and other(obj))

    def __or__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda obj: self.f(obj) or other(obj))

    # === Reflected binary operators ===
    def __rand__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return self & other

    def __ror__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return self | other

def predicate(f):
    """Decorator that lifts a predicate function into a Predicate."""
    wrapper = Predicate(f)
    update_wrapper(wrapper, f)
    return wrapper
