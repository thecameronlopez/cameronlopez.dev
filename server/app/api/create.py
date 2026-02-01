from flask import Blueprint, request, jsonify
from app.extensions import db


creator = Blueprint("create", __name__)