from flask import Blueprint, request, jsonify
from app.extensions import db


authorizer = Blueprint("auth", __name__)

