from flask_app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    public_id = db.Column(db.String(50), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"Admin('{self.name}', '{self.email}')"