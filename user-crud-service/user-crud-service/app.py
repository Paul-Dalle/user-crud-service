from flask import Flask
from configs.config import DBConfig
from src.views import user_bp
from src.models import db
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(DBConfig)

    db.init_app(app)

    app.register_blueprint(user_bp)

    logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

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

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
