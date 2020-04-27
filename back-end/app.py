from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
from environs import Env
import os

app = Flask(__name__)
CORS(app)
heroku = Heroku(app)

env = Env()
env.read_env()
# DATABASEURL = env("DATABASE_URL")

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Tool(db.Model):
    __tablename__ = "Tools"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tool_type = db.Column(db.String(100), nullable=False)
    site = db.Column(db.String(150), nullable=False)

    def __init__(self, name, tool_type, site):
        self.name = name
        self.tool_type = tool_type
        self.site = site

class ToolSchema(ma.Schema);
    class Meta:
        fields:('id', 'name', 'tool_type', 'site')

tool_schema = ToolSchema()
tools_schema = ToolSchema(many=True)

class Site(db.Model):
    __tablename__ = "Site"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(150), nullable=False)
    superintendent = db.Column(db.String(100), nullable=False)

    def __init__(self, location, superintendent):
        self.location = location
        self.superintendent = superintendent

class SiteSchema(ma.Schema):
    class Meta:
        fields:('id', 'location', 'superintendent')

site_schema = SiteSchema()
sites_schema = SiteSchema(many=True)

class Superintendent(db.Model):
    __tablename__ = "Superintendent"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    site = db.Column(db.String(150), nullable=False)

    def __init__(self, name, site):
        self.name = name
        self.site = site
        
class SuperintendentSchema(ma.Schema):
    class Meta:
        fields:('id', 'name', 'site')

superintendent_schema = SuperintendentSchema()
superintendents_schema = SuperintendentSchema(many=True)

class User(db.Model):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

class UserSchema(ma.Schema):
    class Meta:
        fields('id', 'name', 'email', 'password', 'role')

user_schema = UserSchema()
users_schema = UserSchema(many=True)