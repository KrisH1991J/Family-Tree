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
from models import db, User
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# MIGRATE = Migrate(app, db)
# db.init_app(app)
CORS(app)
# setup_admin(app)

smith_family = FamilyStructure("Smith")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members')
def create_family_tree():
    members = smith_family.getAllMembers()
    grandparent = members[0]
    parent_1 = smith_family.createFamilyMember("Allan", 40, (grandparent['id']))
    parent_2 = smith_family.createFamilyMember("Eric", 38, (grandparent['id']))
    p_1_child_1 = smith_family.createFamilyMember("Zoey", 21, (parent_1['id']))
    p_1_child_2 = smith_family.createFamilyMember("Van", 17, (parent_1['id']))
    p_2_child_1 = smith_family.createFamilyMember("Luke", 19, (parent_2['id']))
    p_2_child_2 = smith_family.createFamilyMember("Hailey", 16, (parent_2['id']))
    family_tree = smith_family.getAllMembers()
    return jsonify(family_tree), 200

@app.route('/members/all')
def get_members():
    members = smith_family.getAllMembers()
    return jsonify(members), 200

@app.route('/member/<int:id>')
def get_single_member(id):
    member = smith_family.getSingleMember(id)
    return jsonify(member), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
