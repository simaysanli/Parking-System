# German License Plate
The goal of the task is to build a simple backend application that accepts valid German license plates, stores them in a database and provides an endpoint to retrieve all stored plates. This project consists in a RESTful api and a frontend to consume this API. Flask web framework, SQLAlchemy as ORM were used. Frontend is created by Vue.js framework. The frontend is build using VueJS and Bootstrap. You can view plates.

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")

## Features
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* [Vue.js](https://vuejs.org/)
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://github.com/axios/axios/) for backend communication

# Usage
Some imports are required to use flask and sqlalchemy.

from flask import Flask, request, jsonify<br />
from flask_sqlalchemy import SQLAlchemy<br />
from sqlalchemy import exc<br />

# GET
/plate <br />
Posted plates are viewed with get request.

![Data Structure](/docs/data_structure.png "Data Structure")

# POST
/plate <br />
Request is checked according to some restrictions using regex in Python.
* Missing field (plate) and missing request are controlled and this conditions return 400 status code.
* German plate is controlled by validity conditions. If the plate is valid, it returns 200 status code. If plate isn't valid, it returns 422 status code.

Plate is inserted as ÄE-A2574. 200 status code is returned.

{
	"plate": "ÄE-A2574"
}


{
    "msg": "the ÄE-A2574 is a valid German plate"
}

Plate is inserted as ÄE-A0574. 422 status code is returned.

{
	"plate": "ÄE-A0574"
}

{
    "msg": "the ÄE-A0574 is not a valid German plate"
}

Plate is inserted as ÄBE-AA231. 200 status code is returned.

{
	"plate": "ÄBE-AA231"
}

{
    "msg": "the ÄBE-AA231 is a valid German plate"
}

# DELETE
/plate/<plate_id> <br />
Posted plate is deleted if plate is exist. 

# Database
Valid plates are written to database. Error is checked for database. 502 status code is returned in case of internal error. If plate is written to database successfully, 200 status code is returned.

 # Frontend
 Posted plates are viewed in frontend application.
 ![Frontend Logo](/docs/frontend.png "Frontend")








