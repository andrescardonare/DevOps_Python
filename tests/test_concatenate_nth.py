import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from concatenate_nth import concatenate_nth

class TestConcatenateNth(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(concatenate_nth(['abc', 'de', 'fgh']), 'aeh')

    def test_single(self):
        self.assertEqual(concatenate_nth(['x']), 'x')

    def test_error_short(self):
        self.assertEqual(concatenate_nth(['a', 'b']), 'Invalid word list: not all words have required length')

    def test_mixed_types(self):
        self.assertEqual(concatenate_nth(['ab', 123, 'xyz']), 'Invalid word list: not all words have required length')

if __name__ == '__main__':
    unittest.main()
