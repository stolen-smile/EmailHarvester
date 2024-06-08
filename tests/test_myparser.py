import unittest
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import EmailHarvester

class TestMyParser(unittest.TestCase):
    def setUp(self):
        self.testParser = EmailHarvester.myparser()

    def test_extract(self):
        self.testParser.extract("some results", "example.com")
        self.assertEqual(self.testParser.results, "some results")
        self.assertEqual(self.testParser.word, "example.com")


    def test_genericClean(self):
        self.testParser.extract("<KW>test</KW>%2f<em>email</em>", "example.com")
        self.testParser.genericClean()
        expected_result = "test email"
        self.assertEqual(self.testParser.results, expected_result)

    def test_emails(self):
        self.testParser.extract("Contact us at info@example.com and support@example.com", "example.com")
        emails = self.testParser.emails()
        expected_emails = ["info@example.com", "support@example.com"]
        self.assertEqual(set(emails), set(expected_emails))

    def test_unique(self):
        self.testParser.temp = ["duplicate@example.com", "unique@example.com", "duplicate@example.com"]
        unique_emails = self.testParser.unique()
        expected_unique_emails = ["duplicate@example.com", "unique@example.com"]
        self.assertEqual(set(unique_emails), set(expected_unique_emails))


if __name__ == '__main__':
    unittest.main()