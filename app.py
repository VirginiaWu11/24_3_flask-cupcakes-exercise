from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/api/cupcakes')
def list_cupcakes():
    """Returns JSON with all cupcakes"""
    all_cupcakes= [cupcake.serialize() for cupcake in Cupcake.query.all() ]
    return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def cupcake_by_id(id):
    """Returns JSON with given cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def new_cupcake():
    """Returns JSON with given cupcake"""
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"],rating=request.json["rating"],image=request.json["image"] or None)
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json,201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    """Update given cupcake and respond with JSON of the updated todo"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor=request.json.get('flavor',cupcake.flavor)
    cupcake.size=request.json.get('size',cupcake.size)
    cupcake.rating=request.json.get('rating',cupcake.rating)
    cupcake.image=request.json.get('image',cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Update given cupcake and respond with JSON of the updated todo"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")

# id flavor size rating image

@app.route('/')
def show_home_page():
    cupcakes = Cupcake.query.all()
    return render_template('home.html',cupcakes=cupcakes)