# Plate Project
The goal of the task is to build a simple backend application that accepts valid German license plates, stores them in a database and provides an endpoint to retrieve all stored plates. This project consists in a RESTful api and a frontend to consume this API. Flask web framework, SQLAlchemy as ORM were used. Frontend was created by Vue.js framework. The frontend was build using VueJS and Bootstrap. You can view plates.

![Vue Logo](/docs/vue-logo.png "Vue Logo") ![Flask Logo](/docs/flask-logo.png "Flask Logo")

## Features
* [Flask-RestPlus](http://flask-restplus.readthedocs.io) API with class-based secure resource routing
* [vue-cli 3](https://github.com/vuejs/vue-cli/blob/dev/docs/README.md) + yarn
* [Vue Router](https://router.vuejs.org/)
* [Axios](https://github.com/axios/axios/) for backend communication

# Usage
Flask and sqlalchemy are required some imports to use.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

# GET
/plate
Posted plates are viewed with get request.

# POST
/plate
Request is checked according to some restrictions using regex in Python.
* Missing field (plate) and missing request are controlled and this conditions return 400 status code.
* German plate is controlled by validity conditions. If the plate is valid, it returns 200 status code. If plate isn't valid, it returns 422 status code.

# DELETE
/plate/<plate_id>
Posted plate is deleted if plate is exist. 

# Database
Valid plates are written to database. Error is checked for database. 502 status code is returned in case of internal error. If plate is written to database successfully, 200 status code is returned.

    try:
        db.session.add(car)
        db.session.commit()
        return True
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        db.session.flush()
        return False
        
 # Frontend
 Posted plates are viewed in frontend application.
 ![Frontend Logo](/docs/frontend.png "Frontend")








