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
from models import db, User, Characters, Planets
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

 # brings all users data
@app.route('/user', methods=['GET'])
def get_user():
    all_users = User.query.all()
    map_user = list(map(lambda user : user.serialize() ,all_users))
    return jsonify(map_user), 200

#brings one specific user data
@app.route('/user/<int:user_id>', methods=['GET'])    
def get_specific_user(user_id):
    specific_user = User.query.filter_by(id = user_id).first()
    return jsonify(specific_user.serialize()), 200

#create a new user
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

#Add a favorite
# @app.route('/favorites/characters/<int:character_id>', methods=['POST'])
# def add_fav_character(Favs_characters):

#     input_fav = request.get_json()['favorite']#input_fav is the body of the post
#     input_user = request.get_json()['name']#input_fav is the body of the post
#     user_fav = User(name = input_user, favorite = input_fav)

#     db.session.add(user_fav)
#     db.session.commit()

#     print(Favs_characters.user_name)

#     response_body = {"msg":"Favorito ha sido creado"}

#     return jsonify(response_body),200






#brings all characters data
@app.route('/characters', methods=['GET'])    
def get_characters():
    all_characters = Characters.query.all()
    map_characters = list(map(lambda character : character.serialize() ,all_characters))
    return jsonify(map_characters), 200

#Brings specific character data
@app.route('/characters/<int:characters_id>', methods=['GET'])    
def get_specific_character(characters_id):
    specific_characters = Characters.query.filter_by(id = characters_id).first()
    return jsonify(specific_characters.serialize()), 200


#Brings all planets data
@app.route('/planets', methods=['GET'])    
def get_planets():
    all_planets = Planets.query.all()
    map_planets = list(map(lambda planet : planet.serialize() ,all_planets))
    return jsonify(map_planets), 200

#Brings specific planet data
@app.route('/planets/<int:planets_id>', methods=['GET'])    
def get_specific_planet(planets_id):
    specific_planet = Planets.query.filter_by(id = planets_id).first()
    return jsonify(specific_planet.serialize()), 200





# # Delete specific user 
# @app.route('/user/<int:user_id>', methods=['DELETE'])    
# def delete_user(user_id):
#     db.session.delete(user_id)
#     db.session.commit()
#     return 






# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
