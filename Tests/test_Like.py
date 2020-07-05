import unittest
from ..Tasks.Like import MyClass

class TestLike(unittest.TestCase):

    def test_like(self):

        self.var = 'Alex, Jacob, Mark, Max, Alexander, Daniil, John, David'
        self.assertEqual(MyClass().likes(self.var), 'Alex, Jacob and 6 others like this')
        self.assertNotEqual(MyClass().likes(self.var), 'Alex, Jacob like this')

if __name__ == '__main__':
    unittest.main()