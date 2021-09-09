import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

class greeting():
    def __init__(self):
        self.message = 'Hello World!'
