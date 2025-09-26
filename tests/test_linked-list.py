import unittest

from linked_list import linked_list_node

class test_LinkedListNodeRead(unittest.TestCase):
    def setUp(self):
        # Create a linked list: a -> b -> c
        self.head = linked_list_node('a', 'alpha')
        self.head.append('b', 'bravo')
        self.head.append('c', 'charlie')

    def test_read_head(self):
        self.assertEqual(self.head.read('a'), 'alpha')

    def test_read_middle(self):
        self.assertEqual(self.head.read('b'), 'bravo')

    def test_read_tail(self):
        self.assertEqual(self.head.read('c'), 'charlie')

    def test_read_nonexistent(self):
        self.assertIsNone(self.head.read('d'))

    def test_read_empty_list(self):
        single = linked_list_node('x', 'xray')
        self.assertIsNone(single.read('y'))

class test_LinkedListNodeUpdate(unittest.TestCase):
    def setUp(self):
        self.head = linked_list_node('a', 'alpha')
        self.head.append('b', 'bravo')
        self.head.append('c', 'charlie')

    def test_update_existing(self):
        self.head.update('b', 'beta')
        self.assertEqual(self.head.read('b'), 'beta')

    def test_update_head(self):
        self.head.update('a', 'alfa')
        self.assertEqual(self.head.read('a'), 'alfa')

    def test_update_tail(self):
        self.head.update('c', 'charlie-updated')
        self.assertEqual(self.head.read('c'), 'charlie-updated')

    def test_update_nonexistent(self):
        result = self.head.update('d', 'delta')
        self.assertFalse(result)
        self.assertIsNone(self.head.read('d'))

class test_LinkedListNodeDelete(unittest.TestCase):
    def setUp(self):
        self.head = linked_list_node('a', 'alpha')
        self.head.append('b', 'bravo')
        self.head.append('c', 'charlie')

    def test_delete_middle(self):
        result, successful = self.head.delete('b')
        self.assertTrue(successful)
        self.assertIsNone(result.read('b'))
        self.assertEqual(result.read('c'), 'charlie')

    def test_delete_head(self):
        new_head, successful = self.head.delete('a')
        self.assertTrue(successful)
        self.assertIsNotNone(new_head)
        self.assertIsNone(new_head.read('a'))
        self.assertEqual(new_head.read('b'), 'bravo')
        self.assertEqual(new_head.read('c'), 'charlie')

    def test_delete_tail(self):
        result, successful = self.head.delete('c')
        self.assertTrue(successful)
        self.assertIsNone(result.read('c'))
        self.assertEqual(result.read('b'), 'bravo')

    def test_delete_nonexistent(self):
        result, successful = self.head.delete('d')
        self.assertFalse(successful)
        self.assertEqual(result.read('a'), 'alpha')
        self.assertEqual(result.read('b'), 'bravo')
        self.assertEqual(result.read('c'), 'charlie')

if __name__ == '__main__':
    unittest.main()