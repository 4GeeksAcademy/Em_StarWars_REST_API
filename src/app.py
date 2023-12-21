"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Favs_characters, Favs_planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app) 


# ---------------------------------------ALL USER'S FUNCTIONS BELOW--------------------------------------------------
# Create a new user
@app.route('/user', methods=['POST'])
def add_user():
    user_input = request.get_json()['name']
    user_password = request.get_json()['password']
    user_email = request.get_json()['email']
    new_user = User(name = user_input, password = user_password, email = user_email)
    serialized_user = new_user.serialize()
    db.session.add(new_user)
    db.session.commit()
    return jsonify(serialized_user), 200

# Get all users data
@app.route('/user', methods=['GET'])
def get_user():
    all_users = User.query.all()
    map_user = list(map(lambda user : user.serialize() ,all_users))
    return jsonify(map_user), 200

# Get one specific user data
@app.route('/user/<int:user_id>', methods=['GET'])    
def get_specific_user(user_id):
    specific_user = User.query.filter_by(id = user_id).first()
    return jsonify(specific_user.serialize()), 200

# ---------------------------------------ALL CHARACTERS'S FUNCTIONS BELOW--------------------------------------------------
#Add a new character
@app.route('/characters', methods=['POST'])
def add_character():
    character_name = request.get_json()['name']
    character_species = request.get_json()['species']
    character_height = request.get_json()['height']
    character_eye_color = request.get_json()['eye_color']
    new_character = Characters(name = character_name, species = character_species, height = character_height, eye_color = character_eye_color)
    serialized_character = new_character.serialize()
    db.session.add(new_character)
    db.session.commit()
    return jsonify(serialized_character), 200

# Get all characters data
@app.route('/characters', methods=['GET'])    
def get_characters():
    all_characters = Characters.query.all()
    map_characters = list(map(lambda character : character.serialize() ,all_characters))
    return jsonify(map_characters), 200

# Get specific character data
@app.route('/characters/<int:characters_id>', methods=['GET'])    
def get_specific_character(characters_id):
    specific_characters = Characters.query.filter_by(id = characters_id).first()
    return jsonify(specific_characters.serialize()), 200

# ---------------------------------------ALL PLANETS'S FUNCTIONS BELOW--------------------------------------------------
# Add a new planet
@app.route('/planets', methods=['POST'])
def add_planet():
    planet_name = request.get_json()['name']
    planet_terrain = request.get_json()['terrain']
    planet_population = request.get_json()['population']
    new_planet = Planets(name = planet_name, terrain = planet_terrain, population = planet_population)
    serialized_planet = new_planet.serialize()
    db.session.add(new_planet)
    db.session.commit()
    return jsonify(serialized_planet), 200

# Get all planets data
@app.route('/planets', methods=['GET'])    
def get_planets():
    all_planets = Planets.query.all()
    map_planets = list(map(lambda planet : planet.serialize() ,all_planets))
    return jsonify(map_planets), 200

#Get specific planet data
@app.route('/planets/<int:planets_id>', methods=['GET'])    
def get_specific_planet(planets_id):
    specific_planet = Planets.query.filter_by(id = planets_id).first()
    return jsonify(specific_planet.serialize()), 200

# ---------------------------------------FAVORITE CHARACTERS'S FUNCTIONS BELOW--------------------------------------------------
# Add a favorite character
@app.route('/favs_characters', methods=['POST'])
def add_favorite_character():
    user_id = request.get_json()['user_id']
    existing_user = User.query.get(user_id)
    character_id = request.get_json()['character_id']
    existing_character = Characters.query.get(character_id)
    new_favorite = Favs_characters(user_id=existing_user.id, characters_id=existing_character.id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({'message': 'Favorite character successfully added.'}), 201

# Get favorite characters
@app.route('/favs_characters', methods=['GET'])
def get_favs_characters():
    all_favs_characters = Favs_characters.query.all()
    map_favs_characters = list(map(lambda Favs_characters : Favs_characters.serialize() ,all_favs_characters))
    return jsonify(map_favs_characters), 200

# Delete favorite character
@app.route('/favs_character/<int:id>', methods=['DELETE'])
def delete_fav_character(id):
        fav_delete = Favs_characters.query.get(id)
        db.session.delete(fav_delete)
        db.session.commit()
        return jsonify({'message': 'Favorite character successfully deleted.'}), 200

# ---------------------------------------FAVORITE PLANET'S FUNCTIONS BELOW--------------------------------------------------
# Add a favorite planet
@app.route('/favs_planets', methods=['POST'])
def add_favorite_planet():
    user_id = request.get_json()['user_id']
    existing_user = User.query.get(user_id)
    planet_id = request.get_json()['planets_id']
    existing_planet = Planets.query.get(planet_id)
    new_favorite = Favs_planets(user_id=existing_user.id, planets_id=existing_planet.id)
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify({'message': 'Favorite planet successfully added.'}), 201

# Get favorite planets
@app.route('/favs_planets', methods=['GET'])
def get_favs_planets():
    all_favs_planets = Favs_planets.query.all()
    map_favs_planets = list(map(lambda Favs_planets : Favs_planets.serialize() ,all_favs_planets))
    return jsonify(map_favs_planets), 200

# Delete favorite planet
@app.route('/favs_planets/<int:id>', methods=['DELETE'])
def delete_fav_planet(id):
        fav_delete = Favs_planets.query.get(id)
        db.session.delete(fav_delete)
        db.session.commit()
        return jsonify({'message': 'Favorite planet successfully deleted.'}), 200














# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
