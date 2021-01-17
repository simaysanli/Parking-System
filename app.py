from flask import Flask, request, jsonify
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(80), unique=True, nullable=False)
    request_time = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, plate):
        self.plate = plate
        ts = datetime.datetime.now().timestamp()
        self.request_time = str(datetime.datetime.fromtimestamp(ts).isoformat())

    def __str__(self):
        return '{self.plate}'.format(self=self)

    def __repr__(self):
        return self.plate


db.create_all()


@app.route('/plate', methods=['POST'])
def post_plate():
    return check_request_validity(request)


def check_request_validity(coming_request):
    if not coming_request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    plate_info = coming_request.json.get('plate')

    if plate_info is None:
        return jsonify({"msg": "Missing field (plate) in JSON request"}), 400


if __name__ == '__main__':
    app.run()
