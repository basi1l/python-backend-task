from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

# Initialize the extensions (db, bcrypt, jwt) outside of the app context
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    # Initialize the app
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Import and register blueprints
    from auth import auth_bp
    from project import project_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(project_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

