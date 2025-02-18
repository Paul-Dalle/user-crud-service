from flask import Flask
from config import Config
from models import db
from views import user_bp
import logging

# Create Flask app instance
app = Flask(__name__)
app.config.from_object(Config)

from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://admin:password@localhost/postgres')

print('connected')

db.init_app(app)

app.register_blueprint(user_bp)

logging.basicConfig(filename='../logs/app.log', level=logging.DEBUG)

@app.before_request
def create_tables():
    db.create_all()

@app.before_request
def test_db_connection():
    try:
        db.engine.connect()
        print("Connected to the database successfully!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
