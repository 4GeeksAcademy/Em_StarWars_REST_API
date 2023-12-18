from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    Username = db.Column(db.String(120), unique=False, nullable=False)
    is_not_jedi = db.Column(db.Boolean(), unique=False, nullable=False)
    is_jedi = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return "username de usuario {} y correo electronico {}".format(self.Username, self.email)

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
        return "personaje con nombre {} y de la especie {}".format(self.name, self.species)

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
         return '<Planets %r>' % self.id

     def serialize(self):
         return {
            "id": self.id,
            "name": self.name,
            "terrain": self.species
         }
    
class Favs_characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_relatioship = db.relationship(User)
    characters_id = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=False)
    characters_relatioship = db.relationship(Characters)


    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "characters_id": self.characters_id,
            "user_id": self.user_id
        }