from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_mail import Mail


db = SQLAlchemy()
migrate = Migrate()
seeder = FlaskSeeder()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()
