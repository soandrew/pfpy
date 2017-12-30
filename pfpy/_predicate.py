from collections.abc import Callable
from pfpy._composable import Composable
from functools import update_wrapper
from pfpy._function import Function

__all__ = ["Predicate", "predicate"]

class Predicate(Callable, Composable):
    """Represent an unary predicate."""

    def __init__(self, f):
        """Create a new Predicate to represent unary predicate f."""
        self._f = f

    # === Implement Callable ===
    def __call__(self, x):
        return self._f(x)

    # === Implement Composable ===
    def __matmul__(self, other):
        """Return this Predicate composed with other."""
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: self(other(x)))

    def __rshift__(self, other):
        """Return other composed with this Predicate."""
        if isinstance(other, Composable):
            return other @ self
        elif isinstance(other, Callable):
            return Function(lambda x: other(self(x)))
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        """Return other composed with this Predicate."""
        if not isinstance(other, Callable):
            return NotImplemented
        return self >> other

    def __rrshift__(self, other):
        """Return this Predicate composed with other."""
        if isinstance(other, Callable):
            return self @ other
        else:
            return self(other)  # Function application
        

    # === Logical operators ===
    def __invert__(self):
        return Predicate(lambda x: not self(x))

    def __and__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: self(x) and other(x))

    def __or__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: self(x) or other(x))

    # === Reflected logical operators ===
    def __rand__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: other(x) and self(x))

    def __ror__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Predicate(lambda x: other(x) or self(x))

def predicate(f):
    """Decorator that lifts an unary predicate into a Predicate."""
    wrapper = Predicate(f)
    update_wrapper(wrapper, f)
    return wrapper
