from flask import Blueprint, request, jsonify
from app.extensions import db


reader = Blueprint("read", __name__)