import logging
import unittest


class Assertion(unittest.TestCase):
    def assertion(self, expected, actual, msg):
        try:
            self.assertEqual(expected, actual, msg)
        except AssertionError as error:
            logging.exception(error)
