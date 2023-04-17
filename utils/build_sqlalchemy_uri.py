import os


def build_sqlalchemy_uri(database_type: str, database_name: str) -> str:
    database_type = database_type.lower()
    database_name = database_name.lower()
    if "postgres" in database_type:
        database_type = "postgresql"
    elif "mysql" in database_type:
        database_type = "mysql+pymysql"
    uri = f"{database_type}:///"
    if database_type != "sqlite" and os.environ.get("DATABASE_USER") and os.environ.get("DATABASE_PASSWORD"):
        uri += f"{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@"
    if "sqlite" in uri:
        database_dir = os.path.join(os.getcwd(), "database")
        uri += f"{os.path.join(database_dir, database_name)}.db"
        if not os.path.exists(database_dir):
            os.makedirs(database_dir)
    else:
        uri += f"{database_name}"
    return uri.lower().replace(" ", "_")
