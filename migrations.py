from app import app, db
from models import UserRating

with app.app_context():
    db.create_all()
    print("Database tables created")