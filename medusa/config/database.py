import os


def db_ext_check(SQLALCHEMY_DATABASE_URI: str) -> str:
    """
    Modify the SQLAlchemy database URI if the database type is SQLite. Replace any spaces in the database name with
    underscores.

    Args:
        SQLALCHEMY_DATABASE_URI (str): The original SQLAlchemy database URI.

    Returns:
        str: The modified SQLAlchemy database URI.
    """
    # Check if the database type is SQLite
    if DatabaseConfig.DATABASE_TYPE == "sqlite":
        # Define the directory where the database file will be stored
        database_dir = os.path.join(os.getcwd(), "medusa", "database")
        # Create the database directory if it does not already exist
        if not os.path.exists(database_dir):
            os.makedirs(database_dir)
        # Replace spaces with underscores in the database name
        database_name = SQLALCHEMY_DATABASE_URI.split("/")[-1]
        # Modify the database URI to include the database directory and name
        SQLALCHEMY_DATABASE_URI = (
            f"sqlite:///{os.path.join(database_dir, database_name)}.db"
        )
    # Return the modified database URI
    return SQLALCHEMY_DATABASE_URI


def build_sqlalchemy_uri(database_name: str) -> str:
    """
    Build the SQLAlchemy database URI based on the database type and user credentials.

    Args:
        database_name (str): The name of the database.

    Returns:
        str: The SQLAlchemy database URI.
    """
    # Build the database URI based on the database type and user credentials
    uri = f"{DatabaseConfig.DATABASE_TYPE}://"
    if (
        DatabaseConfig.DATABASE_TYPE != "sqlite"
        and os.environ.get("DATABASE_USER")
        and os.environ.get("DATABASE_PASSWORD")
    ):
        uri += f"{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@"
    uri += f"/{database_name}".lower().replace(" ", "_")
    # Check and modify the database URI if the database type is SQLite
    return db_ext_check(uri)


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
