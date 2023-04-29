from modules.app.base.factories.generator import Generator


class BaseFactory(Generator):
    def __init__(self) -> None:
        super().__init__()
    
    def factory(self):
        table = self.__class__.__table__
        kwargs = {}
        for column in table.columns:
            if not column.name.startswith('_'):
                if column.name == "id" or column.name == "uuid":
                    continue
                kwargs[column.name] = self.generate_value(column)
        return kwargs

    def model_factory(self, count):
        record_ids = []
        for i in range(int(count)):
            kwargs = self.factory()
            record_ids.append(self.model_create(**kwargs).id)
            print(kwargs)
        return self.filter_by_any(record_ids).all()