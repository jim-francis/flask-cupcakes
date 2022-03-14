"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from secrets import secret_key
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret_key

connect_db(app)

def serialize_cupcake(cupcake):
    """Return SQLAlchemy obj to dictionary"""
    
    return{
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }
    
