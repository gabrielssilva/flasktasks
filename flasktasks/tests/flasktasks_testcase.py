import os
import flasktasks
import unittest
import tempfile


class FlaskTasksTestCase(unittest.TestCase):
    def setUp(self):
        self.db_file_handle, self.db_file = tempfile.mkstemp()
        flasktasks.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' %\
                                                           self.db_file
        self.app = flasktasks.app.test_client()
        with flasktasks.app.app_context():
            flasktasks.db.create_all()

    def tearDown(self):
        os.unlink(self.db_file)
        os.close(self.db_file_handle)
