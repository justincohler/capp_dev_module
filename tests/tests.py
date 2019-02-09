"""
Unit Tests.

@author: Justin Cohler
"""
import unittest
import os


class TestTests(unittest.TestCase):
    """Unit Tests."""

    def test_trivial(self):
        """Set up global vars for tests."""
        self.dirname = os.path.dirname(__file__)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
