import gzip
import pickle


class PickableMixin:
    """A mixins to make a class a pickable object"""
    def dump(self, file_name: str) -> None:
        with open('{}.pkl'.format(file_name), 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load(cls, file_name: str) -> 'PickableMixin':
        with open('{}.pkl'.format(file_name), 'rb') as f:
            return pickle.load(f)
