from abc import ABC, abstractmethod

__all__ = ["Composable"]

class Composable(ABC):
    @abstractmethod
    def __matmul__(self, other):
        """Return this Composable composed with other."""
        pass

    @abstractmethod
    def __rshift__(self, other):
        """Return other composed with this Composable."""
        pass

    @abstractmethod
    def __rmatmul__(self, other):
        """Return other composed with this Composable."""
        pass

    @abstractmethod
    def __rrshift__(self, other):
        """Return this Composable composed with other."""
        pass
