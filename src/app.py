"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Pets, Veterinarians, Vaccines, Appointment, Prescriptions
#from models import Person

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://mibasededatos.db"
db.init_app(app)
migrate = Migrate(app, db)

#GET METHOD

@app.route('/', methods=['GET'])
def User():
    users = User.query.all()
    users = list(map(lambda user: user.serialize_1(), users))
    
    return jsonify({
        "data": users,
        "status": 'success'
    }),200
    

#POST METHOD

@app.route("/create", methods=["POST"])
def create():
  get_from_body = request.json.get("email")
  usuario = Ususario()
  usuario_existente = Ususario.query.filter_by(email=get_from_body).first()
  if usuario_existente is not None:
    return "El usuario ya existe"
  else:
    usuario.nombre = request.json.get("nombre")
    usuario.apellido = request.json.get("apellido")
    usuario.email = request.json.get("email")
    usuario.password = request.json.get("password")

    db.session.add(usuario)
    db.session.commit()

  return f"Se creo el usuario", 201

#REGISTER POST METHOD

@app.route("/register", methods=["POST"])
def register():
  get_email_from_body = request.json.get("email")
  get_rut_from_body = request.json.get("rut")
  user = User()
  existing_user = User.query.filter_by(email=get_email_from_body, rut= get_rut_from_body).first()
  if existing_user is not None:
    return "User already exists"
  else:
    user.name = request.json.get("name")
    user.rut = request.json.get("rut")
    user.email = request.json.get("email")
    user.address = request.json.get("address")
    user.password = request.json.get("password")
    user.phone_number = request.json.get("phone_number")

    db.session.add(user)
    db.session.commit()

  return f"User created", 201

#LOGIN GET METHOD

@app.route("/login", methods=["POST"])
def login():
  login_email = request.json.get("email")
  login_password = request.json.get("password")
  user = User.query.filter_by(login_email = "email").first()
  if user is not None:
    if user.password == login_password:
      return f"Login accepted", 200
    else:
      return f"Invalid email or password", 401
  else:
    return f"Invalid email or password", 401


# this only runs if `$ python src/app.py` is executed
if __name__ == "__main__":
  app.run(host="localhost", port=5007, debug=True)
