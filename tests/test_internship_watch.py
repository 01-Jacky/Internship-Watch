import os
import web_result
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, web_result.app.config['DATABASE'] = tempfile.mkstemp()
        web_result.app.testing = True
        self.app = web_result.app.test_client()
        with web_result.app.app_context():
            web_result.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(web_result.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()