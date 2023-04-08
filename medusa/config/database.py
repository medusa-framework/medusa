import os


def build_sqlalchemy_uri(database_name: str) -> str:
    """
    Builds the SQLAlchemy URI for the specified database.
    Args:
        database_name (str): The name of the database.
    Returns:
        str: The SQLAlchemy URI for the specified database.
    """

    database_type = DatabaseConfig.DATABASE_TYPE
    if "postgres" in database_type:
        database_type = "postgresql"
    elif "mysql" in database_type:
        database_type = "mysql+pymysql"
    uri = f"{database_type}:///"
    if database_type != "sqlite" and os.environ.get("DATABASE_USER") and os.environ.get("DATABASE_PASSWORD"):
        uri += f"{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@"
    if "sqlite" in uri:
        database_dir = os.path.join(os.getcwd(), "medusa", "database")
        uri += f"{os.path.join(database_dir, database_name)}.db"
        if not os.path.exists(database_dir):
            os.makedirs(database_dir)
    else:
        uri += f"{database_name}"
    return uri.lower().replace(" ", "_")


class DatabaseConfig:
    """
    Class defining the database configuration variables.

    Attributes:
        APP_NAME (str): The name of the Flask application.
        DATABASE_TYPE (str): The type of the database. Default is SQLite.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Whether to track modifications in SQLAlchemy.
        DATABASE_NAME (str): The name of the database. Default is APP_NAME converted to lowercase.
    """

    # The name of the Flask application.
    APP_NAME = os.environ.get("APP_NAME", "medusa")
    # The type of the database.
    DATABASE_TYPE = os.environ.get("DATABASE_TYPE", "sqlite")
    # The name of the database.
    DATABASE_NAME = os.environ.get("DATABASE_NAME", APP_NAME.lower())
    # Whether to track modifications in SQLAlchemy.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
