from flask import Flask, request, jsonify
import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

plates = {}


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(80), unique=True, nullable=False)
    request_time = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, plate):
        self.plate = plate
        ts = datetime.datetime.now().timestamp()
        self.request_time = str(datetime.datetime.fromtimestamp(ts).isoformat()[:-7] + 'Z')

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        return {
            'plate': self.plate,
            'timestamp': self.request_time
        }

    def __str__(self):
        return '{self.plate}'.format(self=self)

    def __repr__(self):
        return self.plate


db.create_all()


@app.route('/plate', methods=['GET'])
def get_plate():
    cars = db.session.query(Car).all()
    car_plates = [elem.serialized for elem in cars]
    response = jsonify(car_plates)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/plate', methods=['POST'])
def post_plate():
    response = check_request_validity(request)
    return response


@app.route('/plate/<plate_id>', methods=['DELETE'])
def delete_plate(plate_id):

    car = Car.query.filter_by(plate=plate_id).first()

    if car is None:
        return jsonify({"msg": "Plate " + plate_id + " is not registered"}), 409

    db.session.delete(car)
    db.session.commit()
    return jsonify({"msg": "plate " + plate_id + " is deleted successfully"}), 200


def check_request_validity(coming_request):
    if not coming_request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    plate_info = coming_request.json.get('plate')

    if plate_info is None:
        return jsonify({"msg": "Missing field (plate) in JSON request"}), 400

    if check_plate_format_validity(plate_info) is None:
        return jsonify({"msg": "the " + coming_request.json['plate'] + " is not a valid German plate"}), 422

    if db.session.query(Car.plate).filter_by(plate=plate_info).scalar() is not None:
        return jsonify({"msg": "plate is already registered"}), 500

    current_car = Car(plate_info)

    if write_to_database(current_car):
        return jsonify({"msg": "the " + coming_request.json['plate'] + " is a valid German plate"}), 200
    else:
        return jsonify({"msg": "internal error occurred"}), 502


def write_to_database(car):
    try:
        db.session.add(car)
        db.session.commit()
        return True
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        db.session.flush()
        return False


def check_plate_format_validity(plate):
    valid_plate = re.match(r'^[A-ZÄÖÜß]{1,3}-[aA-ZÄÖÜß]{1,2}[1-9]{0,4}$', plate, re.M | re.I)
    return valid_plate


if __name__ == '__main__':
    app.run()
