from flask import jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
from flask import request
from pprint import pprint
from flask_marshmallow import Marshmallow
import postgres_copy
import os
import sys

PACKAGE_PARENT = ''
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://urapiuser:urapiuser@localhost/urapiuser'
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .models import *

migrate = Migrate(app, db)

@app.cli.command()
def import_ur_data():
    #file_path = os.path.abspath("files/register.csv")
    #sql = text("COPY registrs FROM '%s' WITH CSV HEADER DELIMITER ';'" % (file_path))
    #result = db.engine.execute(sql)
    with open('files/register.csv') as fp:
        postgres_copy.copy_from(fp, Registrs, db.engine, format='csv', delimiter=';', header=True)

@app.route('/ur/api/v1.0/registrs', methods=['GET'])
def get_companies():
    search = request.args.get('s')
    companies = Registrs.query.filter(Registrs.regcode.like(search+"%")).all()
    companies_schema = RegistrsSchema(many=True)
    result = companies_schema.dump(companies).data
    return jsonify({'companies': result})