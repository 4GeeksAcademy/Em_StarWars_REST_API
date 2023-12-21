from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120),unique=False, nullable=False)
    favorites = db.Column(db.String(80),unique=False, nullable=True)

    def __repr__(self):
        return "{}".format(self.name)

    def serialize(self):
            return {
            "id": self.id,
            "name": self.name,
            "password":self.password,
            "email":self.email
            }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "{}".format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species,
            "height": self.height,
            "eye_color" : self.eye_color
        }

class Planets(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(120), unique=True, nullable=False)
     terrain = db.Column(db.String(80), unique=False, nullable=False)
     population = db.Column(db.String(80), unique=False, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

     def __repr__(self):
        return "{}".format(self.name)

     def serialize(self):
         return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain,
            "population": self.population
         }
    
class Favs_characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_relatioship = db.relationship(User)
    characters_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False)
    characters_relatioship = db.relationship(Characters)

    def __repr__(self):
        return "{}".format(self.id)

    def serialize(self):
        return {
            "id" :self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id
        }
    
class Favs_planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_relatioship = db.relationship(User)
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=False)
    planets_relatioship = db.relationship(Planets)


    def __repr__(self):
        return "{}".format(self.id)

    def serialize(self):
        return {
            "id" :self.id,
            "user_id": self.user_id,  
            "planets_id": self.planets_id
        }