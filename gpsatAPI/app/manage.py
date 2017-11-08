import os
from gpsat_api import create_app
from gpsat_api.tests import RestTests
from flask_script import Manager, Shell, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
app.debug = True
manager = Manager(app)


def make_shell_context():
    return dict(app=app)


def test():
    import unittest
    suite = unittest.TestSuite(
        [unittest.TestLoader().loadTestsFromTestCase(RestTests)])
    unittest.TextTestRunner(verbosity=2).run(suite)


def main():
    manager.add_command("runserver", Server(port=5000, host='0.0.0.0'))
    manager.add_command("shell", Shell(make_context=make_shell_context))
    manager.run()

if __name__ == '__main__':
    main()
