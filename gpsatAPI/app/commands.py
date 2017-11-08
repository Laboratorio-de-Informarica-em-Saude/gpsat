from flask_script import Command
import unittest
from gpsat_api.test import RestTests


class TestCommand(Command):

    def run(self):
        suite = unittest.TestSuite([
            unittest.TestLoader().loadTestsFromTestCase(RestTests)
        ])
        unittest.TextTestRunner(verbosity=2).run(suite)
