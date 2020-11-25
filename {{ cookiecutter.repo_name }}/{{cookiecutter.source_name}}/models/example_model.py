from models.base_model import BaseModel


class ExampleModel(BaseModel):
    """An example of a model"""

    def __init__(self, name, **kwargs):
        """Constructor for Example model"""
        super().__init__(name)
        raise NotImplementedError

    def train(self, X, y=None, **kwargs):
        raise NotImplementedError

    def predict(self, X, **kwargs):
        raise NotImplementedError



