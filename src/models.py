from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    Username = db.Column(db.String(120), unique=False, nullable=False)
    is_jedi = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(), unique=False, nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species
        }
    
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.String(120), unique=False, nullable=False)

def __repr__(self):
    return '<Planet %r>' % self.id

def serialize(self):
    return {
        "id": self.id,
        "name": self.name,
        "terrain": self.terrain
    }