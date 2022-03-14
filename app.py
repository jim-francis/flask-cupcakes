"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from models import GENERIC_IMAGE, db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "NGE4ev"

connect_db(app)

@app.route('/')
def show_homepage():
    return render_template("home.html")

@app.route('/api/cupcakes')
def list_cupcakes():
    """Get all cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """Get a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def create_cupcate():
    """Make a cupcake"""
    data = request.json
    fresh_cupcake = Cupcake(
        flavor=data["flavor"],
        rating=data["rating"],
        size=data["size"],
        image=data["image"] or None)
    
    # if fresh_cupcake.image is None or "None":
    #     fresh_cupcake.image = GENERIC_IMAGE
    
    db.session.add(fresh_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=fresh_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Update a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.image = request.json.get('image', cupcake.image)
    
    db.session.add(cupcake)
    db.session.commit()
    
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    
    db.session.delete(cupcake)
    db.session.commit()
    
    return jsonify(message="deleted")