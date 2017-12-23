from collections.abc import Callable
from numbers import Real
from functools import update_wrapper

class Function(Callable):
    """Represents an unary function."""

    def __init__(self, f):
        """Create a new Function to represent unary function f."""
        self._f = f

    # === Getters ===
    @property
    def f(self):
        """Return the unary function this Function represents."""
        return self._f

    # === Implement Callable ====
    def __call__(self, obj):
        return self.f(obj)

    # === Unary operators ===
    def __pos__(self):
        return Function(lambda obj: +self.f(obj))

    def __neg__(self):
        return Function(lambda obj: -self.f(obj))

    # === Binary operators ===
    def __add__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: self.f(obj) + other(obj))

    def __sub__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: self.f(obj) - other(obj))

    def __mul__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: self.f(obj) * other(obj))

    def __floordiv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: self.f(obj) // other(obj))

    def __truediv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: self.f(obj) / other(obj))

    def __pow__(self, other):
        if not isinstance(other, Real):
            return NotImplemented
        return Function(lambda obj: self.f(obj) ** other)

    def __lshift__(self, other):
        """Return this Function composed with other."""
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: self.f(other(obj)))

    def __rshift__(self, other):
        """Return other composed with this Function."""
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: other(self.f(obj)))

    def __xor__(self, other):
        """Alias for ** operator."""
        if not isinstance(other, Real):
            return NotImplemented
        return self ** other

    def __matmul__(self, other):
        """Alias for << operator."""
        if not isinstance(other, Callable):
            return NotImplemented
        return self << other

    # === Reflected binary operators ===
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
        return Function(lambda obj: other(obj) - self.f(obj))

    def __rmul__(self, other):
        if isinstance(other, Real):
            return Function(lambda obj: other * self.f(obj))  # Scalar multiplication
        elif isinstance(other, Callable):
            return self * other
        else:
            return NotImplemented

    def __rfloordiv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: other(obj) // self.f(obj))

    def __rtruediv__(self, other):
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: other(obj) / self.f(obj))

    def __rlshift__(self, other):
        """Return other composed with this Function."""
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: other(self.f(obj)))

    def __rrshift__(self, other):
        """Return this Function composed with other."""
        if not isinstance(other, Callable):
            return NotImplemented
        return Function(lambda obj: self.f(other(obj)))

    def __rmatmul__(self, other):
        """Alias for << operator."""
        if not isinstance(other, Callable):
            return NotImplemented
        return other << self


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

def unary(f):
    """Decorator that lifts an unary function into a Function."""
    wrapper = Function(f)
    update_wrapper(wrapper, f)
    return wrapper

@unary
def I(x):
    return x

@unary
def Z(x):
    return 0

if __name__ == '__main__':
    pass
