from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin@localhost:5432/postgres"

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
