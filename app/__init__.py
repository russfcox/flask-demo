import os
import sys
from flask import Flask
from app.main.controllers import main

app = Flask(__name__)

# # set config
# app.config.from_object('app.config.DevelopmentConfig')
# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# print(app.config, file=sys.stderr)
app.register_blueprint(main, url_prefix='/')
