from models import ExampleModel, BaseModel

model_dict: dict = {"ex": ExampleModel}


def model_factory(name: str, params: dict = None) -> BaseModel:
    params = params if params else {}
    if name in model_dict.keys():
        return model_dict[name](**params)
    else:
        raise ValueError("{} is not a valid model type".format(name))
