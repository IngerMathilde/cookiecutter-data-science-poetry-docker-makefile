from abc import ABC, abstractmethod
from models.example_model import ExampleModel


class BaseModel(ABC):
    """A core class for a base model"""
    def __new__(cls, name, **kwargs):
        if name == "":
            return super(BaseModel, cls).__new__(ExampleModel, name, **kwargs)
        else:
            raise ValueError("{} is not a valid model".format(name))

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def train(self, X, y=None, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def predict(self, X, **kwargs):
        raise NotImplementedError
