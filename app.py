import postgres_copy
from flask import jsonify
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate
from flask import request
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

migrate = Migrate(app, db)

@app.cli.command()
def import_ur_data():
    file_path = os.path.abspath("files/register.csv")
    print(file_path)
    sql = text("COPY registrs (regcode, name, registered, terminated, closed, address, index, region, city) FROM 'C:/Users/eddy/Desktop/projects/urapi/files/register.csv' WITH CSV HEADER DELIMITER ';'")
    result = db.engine.execute(sql)
    names = []
    for row in result:
        names.append(row[0])

    print(names)

@app.route('/ur/api/v1.0/registrs', methods=['GET'])
def get_companies():
    return jsonify({'task': 1}), 201

if __name__ == '__main__':
    app.run()