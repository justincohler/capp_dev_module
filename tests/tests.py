"""
Unit Tests for the Neighbors Pipeline.

@author: Justin Cohler
"""
import unittest
import os


class Tests(unittest.TestCase):
    """Unit Tests for the Neighbors Pipeline."""

    def setUp(self):
        """Set up global vars for tests."""
        self.dirname = os.path.dirname(__file__)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
