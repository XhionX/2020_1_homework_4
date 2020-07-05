import unittest
from ..Tasks.Flags import MyClass

class TestFlags(unittest.TestCase):

    def test_flags(self):

        self.n = '14'
        self.assertEquals(MyClass().flags(self.n), 'Ошибочка, количество флагов должно быть от 1 до 9')

if __name__ == '__main__':
    unittest.main()