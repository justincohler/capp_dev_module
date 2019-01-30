"""
Unit Tests for the Neighbors Pipeline.

@author: Justin Cohler
"""
import unittest
import os


class TestNeighbors(unittest.TestCase):
    """Unit Tests for the Neighbors Pipeline."""

    def setUp(self):
        """Set up global vars for tests."""
        self.dirname = os.path.dirname(__file__)
        self.csv = os.path.join(self.dirname, '../data/credit-data.csv')


if __name__ == '__main__':
    unittest.main()
