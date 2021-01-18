import unittest
import json
from app import Car
from app import app, db


class PlateTest(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        #SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/deneme.db'
        #self.db = db.create_all()

    #def tearDown(self):
        #self.db.session.remove()
        #self.db.drop_all()

    def test_get_valid_plate(self):
        response = self.app.get('/plate', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)

    #test for post requests
    def test_invalid_digit_plate(self):
        # Given
        x = {"plate": "ÄE-AÄ0123"}
        plate = json.dumps(x)

        # When
        response = self.app.post('/plate', headers={"Content-Type": "application/json"}, data=plate)
        # Then
        self.assertEqual(type("the " + x["plate"] + "  is not a valid German plate"), type(response.json['msg']))
        self.assertEqual("the " + x["plate"] + " is not a valid German plate", response.json['msg'])
        self.assertEqual(422, response.status_code)

    def test_invalid_alphabet_plate(self):
        # Given
        x = {"plate": "ÄE-123"}
        plate = json.dumps(x)

        # When
        response = self.app.post('/plate', headers={"Content-Type": "application/json"}, data=plate)
        # Then
        self.assertEqual(type("the " + x["plate"] + " is not a valid German plate"), type(response.json['msg']))
        self.assertEqual("the " + x["plate"] + " is not a valid German plate", response.json['msg'])
        self.assertEqual(422, response.status_code)

    def test_initial_alphabet_invalid_plate(self):
        # Given
        x = {"plate": "ÄFGE-AÄ123"}
        plate = json.dumps(x)

        # When
        response = self.app.post('/plate', headers={"Content-Type": "application/json"}, data=plate)
        # Then
        self.assertEqual(type("the " + x["plate"] + " is not a valid German plate"), type(response.json['msg']))
        self.assertEqual("the " + x["plate"] + " is not a valid German plate", response.json['msg'])
        self.assertEqual(422, response.status_code)

    def test_second_part_alphabet_invalid_plate(self):
        # Given
        x = {"plate": "S-AA123"}
        plate = json.dumps(x)
        current_car = Car(x['plate'])
        # When
        response = self.app.post('/plate', headers={"Content-Type": "application/json"}, data=plate)

        # Then
        self.assertEqual(type("the " + x["plate"] + " is a valid German plate"), type(response.json['msg']))
        self.assertEqual("the " + x["plate"] + " is a valid German plate", response.json['msg'])
        self.assertEqual(200, response.status_code)

    def test_second_part_alphabet_valid_plate(self):
        # Given
        x = {"plate": "AE-A123"}
        plate = json.dumps(x)
        # When
        response = self.app.post('/plate', headers={"Content-Type": "application/json"}, data=plate)

        # Then
        self.assertEqual(type("the " + x["plate"] + " is a valid German plate"), type(response.json['msg']))
        self.assertEqual("the " + x["plate"] + " is a valid German plate", response.json['msg'])
        self.assertEqual(200, response.status_code)

    def test_delete_plate(self):
        # Given
        x = {"plate": "KLM-K123"}
        plate = json.dumps(x)
        # When
        delete_response = self.app.delete('/plate/'+x["plate"]+"", headers={"Content-Type": "application/json"}, data=plate)
        # Then
        self.assertEqual(type("Plate " + x["plate"] + " is not registered"), type(delete_response.json['msg']))
        self.assertEqual("Plate " + x["plate"] + " is not registered", delete_response.json['msg'])
        self.assertEqual(409, delete_response.status_code)


if __name__ == '__main__':
    unittest.main()