from abc import ABC, abstractmethod

__all__ = ["Composable"]

class Composable(ABC):
    @abstractmethod
    def __matmul__(self, other):
        """Return this Composable composed with other."""
        pass

    def __lshift__(self, other):
        """Alias for @ operator."""
        return self @ other

    @abstractmethod
    def __rshift__(self, other):
        """Return other composed with this Composable."""
        pass

    @abstractmethod
    def __rmatmul__(self, other):
        """Return other composed with this Composable."""
        pass

    def __rlshift__(self, other):
        """Alias for reflected @ operator."""
        return other @ self

    @abstractmethod
    def __rrshift__(self, other):
        """Return this Composable composed with other."""
        pass
