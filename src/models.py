from flask_sqlalchemy import SQLAlchemy
import base64

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120),unique=False, nullable=False)
    favorites = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return "{}".format(self.name)

    def serialize(self):
        if self.password:
            password_encoded = base64.b64encode(self.password.encode('utf-8')).decode('utf-8')
            return {
            "id": self.id,
            "name": self.name,
            "password":self.password,
            "email":self.email
        }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "email": self.email,
            }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    species = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(), unique=False, nullable=False)

    def __repr__(self):
        return "{}".format(self.name)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "species": self.species
        }

class Planets(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(120), unique=True, nullable=False)
     terrain = db.Column(db.String(80), unique=False, nullable=False)
     population = db.Column(db.Integer, unique=False, nullable=False)

     def __repr__(self):
        return "{}".format(self.name)

     def serialize(self):
         return {
            "id": self.id,
            "name": self.name,
            "terrain": self.terrain
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
            "characters_id": self.characters_id,
            "user_id": self.user_id
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
            "planets_id": self.planets_id,
            "user_id": self.user_id
        }