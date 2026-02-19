from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer)
    home = db.Column(db.String(100))
    away = db.Column(db.String(100))
    odds_home = db.Column(db.Float)
    odds_draw = db.Column(db.Float)
    odds_away = db.Column(db.Float)
    status = db.Column(db.String(20), default='open')
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    balance = db.Column(db.Float, default=1000)
