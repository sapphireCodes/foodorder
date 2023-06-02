from flask import Flask, jsonify, request
from app.service.restaurant_service import Restaurant
from app.service.category_service import Category
from app.service.cuisine_service import Cuisine
from app.service.user_service import User
from flask_cors import CORS

app = Flask(__name__)
CORS(app)