from flask import Blueprint, request, jsonify
from app.extensions import db


updator = Blueprint("update", __name__)