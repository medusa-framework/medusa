from config.system import db
from config import logger


class BaseSeeder():
    def __init__(self, db=None):
        super().__init__(db=db)

    def seeds(self):
        return None

    def run(self):
        if not self._class.query.all():
            seeds = self.seeds()
            if seeds:
                for seed in seeds:
                    model = self._class().model_create(**seed)
                logger.warn("%s Table has been seeded",
                             self._class.__name__.upper())
            else:
                logger.warn(
                    "%s Seeder has no defined seeds. Not seeding.", self._class.__name__.upper())
        else:
            logger.warn(
                "%s Table data exists. Not seeding.", self._class.__name__.upper())
