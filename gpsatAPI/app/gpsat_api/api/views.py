from . import main_blueprint
from flask import current_app, request
from flask.json import jsonify
from bson import json_util, ObjectId
from pymongo import MongoClient
from flask_api import status


def get_db():
    connection = MongoClient(current_app.config['DB_URI'])
    db = connection[current_app.config['DB_NAME']]
    return db


@main_blueprint.route('/patients/<id>/')
def get_patient(id):
    db = get_db()
    patient = db.patient.find_one({'_id': ObjectId(id)})
    if patient:
        return json_util.dumps(patient), status.HTTP_200_OK
    else:
        return jsonify({'error': 'not found'}), status.NOT_FOUND


@main_blueprint.route('/patients/', methods=['GET', 'POST', 'PUT'])
def patients():
    db = get_db()
    if request.method == 'GET':
        patients = list(db.patients.find({}))
        return json_util.dumps(patient), status.HTTP_200_OK
    else:
        patient = json_util.loads(request.data)
    if request.method == 'POST':
        patient_id = db.patient.insert_one(patient).inserted_id
        patient = db.patient.find_one({'_id': ObjectId(patient_id)})
        return json_util.dumps(patient), status.HTTP_201_CREATED


@main_blueprint.route('/patients/update/<id>/', methods=['PUT'])
def update_patient():
    db = get_db()
    updated_data = json_util.loads(request.data)
    patient = db.patient.find_one({'_id': ObjectId(id)})

    if not patient:
        return jsonify({'error': 'not found'}), status.HTTP_404_NOT_FOUND
    else:
        return db.patient.replace_one({'_id': patient['_id']}, updated_data),
        status.HTTP_202_ACCEPTED
