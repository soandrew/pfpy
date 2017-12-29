from collections.abc import Callable
from pfpy._composable import Composable
from numbers import Real
from functools import update_wrapper

__all__ = ["Function", "unary", "identity", "constant"]

class Function(Callable, Composable):
    """Represents an unary function."""

    def __init__(self, f):
        """Create a new Function to represent unary function f."""
        self._f = f

    # === Implement Callable ====
    def __call__(self, x):
        return self._f(x)

    # === Implement Composable ===
    def __matmul__(self, other):
        """Return this Function composed with other."""
        if isinstance(other, Callable):
            return Function(lambda x: self(other(x)))
        else:
            return self(other)  # function application

    def __rshift__(self, other):
        """Return other composed with this Function."""
        if isinstance(other, Composable):
            return other @ self
        elif isinstance(other, Callable):
            return Function(lambda x: other(self(x)))
        else:
            return NotImplemented

    def __rmatmul__(self, other):
        """Return other composed with this Function."""
        if not isinstance(other, Callable):
            return NotImplemented
        return self >> other

    def __rrshift__(self, other):
        """Return this Function composed with other."""
        return self @ other

    # === Arithmetic operators ===
    def __pos__(self):
        return Function(lambda x: +self(x))

    def __neg__(self):
        return Function(lambda x: -self(x))

    def __add__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: self(x) + other(x))

    def __sub__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: self(x) - other(x))

    def __mul__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: self(x) * other(x))

    def __truediv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: self(x) / other(x))

    def __floordiv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: self(x) // other(x))

    def __pow__(self, other):
        if not isinstance(other, Real):
            return NotImplemented
        return Function(lambda x: self(x) ** other)

    # === Reflected arithmetic operators ===
    def __radd__(self, other):
        if other == 0:
            return self  # Allows sum() to work
        elif isinstance(other, Callable):
            return self + other
        else:
            return NotImplemented

    def __rsub__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: other(x) - self(x))

    def __rmul__(self, other):
        if isinstance(other, Real):
            return Function(lambda x: other * self(x))  # Scalar multiplication
        elif isinstance(other, Callable):
            return self * other
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: other(x) / self(x))

    def __rfloordiv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda x: other(x) // self(x))

def unary(f):
    """Decorator that lifts an unary function into a Function."""
    wrapper = Function(f)
    update_wrapper(wrapper, f)
    return wrapper

@unary
def identity(x):
    """Return x."""
    return x

@unary
def constant(x):
    """Return an unary function that always returns x."""
    return Function(lambda _: x) 
