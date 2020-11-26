from abc import ABC, abstractmethod
from models.example_model import ExampleModel


class BaseModel(ABC):
    """A core class for a base model"""

    @abstractmethod
    def train(self, X, y=None, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def predict(self, X, **kwargs):
        raise NotImplementedError
