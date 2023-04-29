import os

import redis
from flask import Flask
from flask_migrate import Migrate
from flask_session.__init__ import Session
from flask_wtf import CSRFProtect

from app_api import bp as api
from app_library import bp as library
from database import db

config_name = os.getenv("CONFIG_NAME", "DevelopmentConfig")

app = Flask(__name__)
app.config.from_object(f"config.{config_name}")
app.config['SESSION_REDIS'] = redis.from_url(app.config['SESSION_REDIS'])

db.init_app(app)
migrate = Migrate(app=app, db=db)
csrf = CSRFProtect(app)
sess = Session()
sess.init_app(app)

app.register_blueprint(api)
app.register_blueprint(library)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
