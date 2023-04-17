class BaseController():
    def __init__(self) -> None:
        super().__init__()

    def controller_create(self, **request_json):
        return self.model_create(**request_json)

    def controller_update(self, request_args=None, **request_json):
        return self.model_update(request_args, **request_json)

    def controller_delete(self, **request_args):
        return self.model_delete(**request_args)

    def controller_get(self, **request_args):
        return self.model_get(**request_args)

    def controller_factory(self, **request_json):
        return self.model_factory(**request_json)
