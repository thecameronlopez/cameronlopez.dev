from flask import Blueprint, request, jsonify
from app.extensions import db


deleter = Blueprint("delete", __name__)