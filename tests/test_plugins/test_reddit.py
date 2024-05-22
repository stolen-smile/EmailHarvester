import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the root directory of your project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from plugins.reddit import Plugin, search

class TestRedditPlugin(unittest.TestCase):
    def test_(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()