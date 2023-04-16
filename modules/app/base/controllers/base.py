class BaseController():
    def __init__(self) -> None:
        super().__init__()

    def controller_create(self, **kwargs):
        return self.model_create(**kwargs)

    def controller_update(self, request_args=None, **kwargs):
        return self.model_update(request_args, **kwargs)

    def controller_delete(self, **request_args):
        return self.model_delete(**request_args)

    def controller_get(self, **request_args):
        return self.model_get(**request_args)

    def controller_factory(self, **kwargs):
        return self.model_factory(**kwargs)
