from . import create_app, get_db_connection
from bson import json_util, ObjectId
from flask import current_app, url_for


class RestTests(unittest.TestCase):

    db = None

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = get_db_connection('testing')
        self.db.patient.drop()
        self.client = self.app.test_client

    def tearDown(self):
        if self.db:
            self.db.patients.drop()
        self.db.positionals_data.drop()
        self.app_context.pop()

    def test_db_connection(self):
        patient_obj = self.db['patient'].insert_one({'name': 'testing'})
        patient_obj = self.db.patient.find_one({'name': 'testing'})
        self.assertTrue(patient_obj['name'] == 'testing')

    def test_get_patient(self):
        patient_id = self.db.patients.insert_one(
            {'name': 'Douglas'}).inserted_id
        url = url_for('gpsat_api_0.get_patient', id=patient_id)
        r = self.client.get(url)
        patient = json_util.loads(r.data.decode('utf-8'))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(patient['name'], 'roberto')
