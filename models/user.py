from flask_login import UserMixin
from extensions import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    membership_type = db.Column(db.String(50))  # e.g., Bronze, Silver, Gold, etc.
    membership_start_date = db.Column(db.Date)
    annual_maintenance_fees = db.Column(db.Float)
    password = db.Column(db.String(255))
    is_admin = db.Column(db.Boolean, default=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    residence = db.Column(db.String(100))
    joining_year = db.Column(db.Integer)
    profile_picture = db.Column(db.String(255))
    # Add other fields as necessary

    def __repr__(self):
        return f'<User {self.username}>'
