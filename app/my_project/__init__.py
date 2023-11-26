# my_project/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config, additional_config):
    app = Flask(__name__)
    app.config.update(config)
    app.config.update(additional_config)

    db.init_app(app)

    # Додайте інші налаштування та ініціалізацію, якщо потрібно.

    return app
