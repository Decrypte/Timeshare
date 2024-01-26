from extensions import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'), nullable=False)
    check_in_date = db.Column(db.Date, nullable=False)
    check_out_date = db.Column(db.Date, nullable=False)
    booking_date = db.Column(db.DateTime, default=datetime.utcnow)

    resort_id = db.Column(db.Integer, db.ForeignKey('resort.id'), nullable=False)
    resort = db.relationship('Resort', backref=db.backref('bookings', lazy=True))

    def __repr__(self):
        return f'<Booking {self.id}>'
