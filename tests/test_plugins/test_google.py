import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add the root directory of your project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from plugins.google import Plugin, search

class TestGooglePlugin(unittest.TestCase):
    pass
   

if __name__ == '__main__':
    unittest.main()