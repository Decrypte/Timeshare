from extensions import db

class Resort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))  # City, State, Country
    accommodations = db.Column(db.String(100))  # Brief description
    dining = db.Column(db.String(100))  # Summary of dining options
    fitness_wellness = db.Column(db.String(100))  # Summary of facilities
    business_facilities = db.Column(db.String(100))
    concierge_services = db.Column(db.String(100))
    entertainment = db.Column(db.String(100))
    additional_services = db.Column(db.String(100))
    security = db.Column(db.String(100))
    access_level = db.Column(db.String(100))  # Membership level access

    def __repr__(self):
        return f'<Resort {self.name}>'
