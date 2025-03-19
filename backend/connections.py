from flask_pymongo import PyMongo
from flask import Flask

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/healthcare_db"  # 🔥 Connect to MongoDB 4.4
mongo = PyMongo(app)