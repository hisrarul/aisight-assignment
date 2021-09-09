import unittest
import logging
from helloWorld import greeting

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

class HelloWorldTest(unittest.TestCase):
    def test_helloworld(self):
        logging.info('Test case started ..')
        case1 = greeting()
        self.assertEqual(case1.message, 'Hello World!')
        logging.info('Test case stopped ..!')