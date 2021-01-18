# German License Plate
The goal of the task is to build a simple backend application that accepts valid German license plates, stores them in a database and provides an endpoint to retrieve all stored plates. This project consists in a RESTful api and a frontend to consume this API. Flask web framework, SQLAlchemy as ORM were used. Frontend is created by Vue.js framework. The frontend is build using VueJS and Bootstrap. You can view plates.

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")

## Features
* [Flask](https://flask-restful.readthedocs.io/en/latest/) 
* [Vue.js](https://vuejs.org/)
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://github.com/axios/axios/) for backend communication

# Usage
Some imports are required to use flask and sqlalchemy.

from flask import Flask, request, jsonify<br />
from flask_sqlalchemy import SQLAlchemy<br />
from sqlalchemy import exc<br />

# Error handling
Common response codes indicating success, failure due to client-side problem, failure due to server-side problem:
* 200 - OK
* 400 - Bad Request
* 402 - Invalid Request
* 409 - Conflict Error
* 500 - Internal Server Error
* 502 - Internal Server Error

# GET
/plate <br />
Posted plates are viewed with get request.

![Data Structure](/docs/data_structure.png "Data Structure")

# POST
/plate <br />
Request is checked according to some restrictions using regex in Python.
* Missing field (plate) and missing request are controlled and this conditions return 400 status code.
* German plate is controlled by validity conditions. If the plate is valid, it returns 200 status code. If plate isn't valid, it returns 422 status code.

Plate is inserted as ÄE-A2574. 200 status code and message are returned.

Request:

	{
		"plate": "ÄE-A2574"
	}

Response:

	{
	    "msg": "the ÄE-A2574 is a valid German plate"
	}
	
Plate is inserted as ÄE-A2574 again. 500 status code and message returned.

Request:

	{
		"plate": "ÄE-A2574"
	}
	
Response:

	{
	    "msg": "plate is already registered"
	}

Plate is inserted as ÄE-A0574. 422 status code and message are returned.

Request:

	{
		"plate": "ÄE-A0574"
	}

Response:

	{
	    "msg": "the ÄE-A0574 is not a valid German plate"
	}
	
Plate is inserted as ÄFGE-AÄ123. 422 status code and message are returned.

Request:

	{
		"plate": "ÄFGE-AÄ123"
	}

Response:

	{
	    "msg": "the ÄFGE-AÄ123 is not a valid German plate"
	}
	
Plate is inserted as ÄBE-AA231. 200 status code and message are returned.

Request:

	{
		"plate": "ÄBE-AA231"
	}

Response:

	{
	    "msg": "the ÄBE-AA231 is a valid German plate"
	}


# DELETE
/plate/<plate_id> <br />
Posted plate is deleted if plate is exist. 
200 status code and message are returned for plate/ÄBE-AA231 delete operation.

Response:

	{
	    "msg": "plate ÄBE-AA231 is deleted successfully"
	}

409 status code and message are returned if plate is not registered in database.

Response:

	{
	    "msg": "Plate BE-A231 is not registered"
	}
	
# Database
Valid plates are written to database. Error is checked for database. 502 status code is returned in case of internal error. If plate is written to database successfully, 200 status code is returned.

 # Frontend
 Posted plates are viewed in frontend application.
 
 ![Frontend Logo](/docs/frontend.png "Frontend")








