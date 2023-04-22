from utils.log import create_logger

logger = create_logger("medusa")
werkzeug_logger = create_logger("werkzeug")

# TODO: look into flask_seeder and flask_migrate logging 
# flask_migrate_logger = create_logger("flask_migrate")