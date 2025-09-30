import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hashmap.hashmap import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.d = Dictionary(10)

    def test_add_and_lookup(self):
        self.assertEqual(self.d.add('a', 'alpha'), 'Entry added successfully')
        self.assertEqual(self.d.lookup('a'), 'alpha')
        self.assertEqual(self.d.add('a', 'alpha'), 'Entry already exists')

    def test_lookup_nonexistent(self):
        self.assertEqual(self.d.lookup('missing'), 'Entry not found')

    def test_update(self):
        self.d.add('b', 'bravo')
        self.assertEqual(self.d.update('b', 'beta'), 'Entry updated successfully')
        self.assertEqual(self.d.lookup('b'), 'beta')
        self.assertEqual(self.d.update('missing', 'value'), 'Entry not found')

    def test_delete(self):
        self.d.add('c', 'charlie')
        self.assertEqual(self.d.delete('c'), 'Entry deleted successfully')
        self.assertEqual(self.d.lookup('c'), 'Entry not found')
        self.assertEqual(self.d.delete('c'), 'Entry not found')

    def test_collision_handling(self):
        # Force collision by using keys with same index
        # This depends on hash and size, so we use a small size and override get_hash
        class TestDict(Dictionary):
            def get_hash(self, key):
                return 1  # All keys collide
        td = TestDict(2)
        self.assertEqual(td.add('x', 'xray'), 'Entry added successfully')
        self.assertEqual(td.add('y', 'yankee'), 'Entry added successfully')
        self.assertEqual(td.lookup('x'), 'xray')
        self.assertEqual(td.lookup('y'), 'yankee')
        self.assertEqual(td.delete('x'), 'Entry deleted successfully')
        self.assertEqual(td.lookup('x'), 'Entry not found')
        self.assertEqual(td.lookup('y'), 'yankee')

if __name__ == '__main__':
    unittest.main()
