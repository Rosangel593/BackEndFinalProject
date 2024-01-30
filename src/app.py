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

@app.route('/', methods=['GET'])
def User():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    #PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=5432, debug=False)
