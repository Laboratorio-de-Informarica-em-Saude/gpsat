"""Test class for gpsat api."""
from . import create_app, get_db_connection
from bson import json_util
from flask import url_for
from flask_api import status
import unittest


class RestTests(unittest.TestCase):

    db = None

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = get_db_connection('testing')
        self.db.patient.drop()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        if self.db:
            self.db.patient.drop()
        self.db.positionals_data.drop()
        self.app_context.pop()

    def test_db_connection(self):
        patient_obj = self.db['patient'].insert_one({'name': 'testing'})
        patient_obj = self.db.patient.find_one({'name': 'testing'})
        self.assertTrue(patient_obj['name'] == 'testing')

    def test_get_patient(self):
        patient_id = self.db.patient.insert_one(
            {'name': 'Douglas'}).inserted_id
        url = url_for('gpsat_api_0.get_patient', id=patient_id)
        r = self.client.get(url)
        patient = json_util.loads(r.data.decode('utf-8'))
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        self.assertEqual(patient['name'], 'Douglas')

    def test_get_patient_404(self):
        url = url_for(
            'gpsat_api_0.get_patient',
            id=u'000000000000000000000000'
        )
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

    def test_add_patient(self):
        payload = json_util.dumps({'name': 'Mary Jane'})
        r = self.client.post(url_for('gpsat_api_0.patients'), headers={
            'Content-Type': 'application/json'}, data=payload)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        patient = json_util.loads(r.data.decode('utf-8'))
        self.assertEqual(patient['name'], 'Bruna Silva')
