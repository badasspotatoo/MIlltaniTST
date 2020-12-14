from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd2a0e39be0acfb1a5e1781d37917dd18'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://ovxpvqzs:rasfIJbDGbiA6ymwE_X3GYi0ymX2ndYN@rajje.db.elephantsql.com:5432/ovxpvqzs'
db = SQLAlchemy(app)

from Miltani import routes
