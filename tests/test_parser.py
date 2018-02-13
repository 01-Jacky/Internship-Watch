import unittest
from lib import parser
import datetime


class TestParser(unittest.TestCase):
    def test_today(self):
        DATE_FORMAT = '%Y-%m-%d'
        date_to_test = datetime.date.today().strftime(DATE_FORMAT)

        today = parser._convert_to_date('today')
        self.assertEqual(today, date_to_test)

        today = parser._convert_to_date('just posted')
        self.assertEqual(today, date_to_test)

    def test_x_day_ago(self):
        DATE_FORMAT = '%Y-%m-%d'

        date_to_test = datetime.date.today() - datetime.timedelta(days=1)
        date_to_test = date_to_test.strftime(DATE_FORMAT)
        converted = parser._convert_to_date('1 day ago')
        self.assertEqual(converted, date_to_test)

        date_to_test = datetime.date.today() - datetime.timedelta(days=10)
        date_to_test = date_to_test.strftime(DATE_FORMAT)
        converted = parser._convert_to_date('10 days ago')
        self.assertEqual(converted, date_to_test)

        converted = parser._convert_to_date('30+ days ago')
        self.assertEqual(converted, '30+ days ago')

if __name__ == '__main__':
    unittest.main()