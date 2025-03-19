from flask import Blueprint, request, jsonify
from connections import mongo
from models import User
from werkzeug.security import check_password_hash

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 400

    username = data["username"]
    password = data["password"]

    existing_user = mongo.db.users.find_one({"username": username})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    user = User(username, password)
    mongo.db.users.insert_one(user.to_dict())

    return jsonify({"message": "Registered successfully"}), 201

@api_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 400

    username = data["username"]
    password = data["password"]

    user = mongo.db.users.find_one({"username": username})
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful"}), 200