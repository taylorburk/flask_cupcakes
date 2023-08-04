"""Flask app for Cupcakes"""
from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "idonthaveasecret"


connect_db(app)

@app.route('/')
def root():
    return render_template("index.html")

@app.route('/api/cupcakes', methods=["GET"])
def list_cupcakes():
    cupcakes = [cupcake.cupcakedict() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def one_cupcake(cupcake_id):
    cupcake = cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["POST"])
def create_cupcake(cupcake_id):
    data = request.json

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes/<int:cupcakes_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    data = request.json

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']
    
    db.session.add(cupcake)
    db.session.commit()
    
    cupcake = cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")