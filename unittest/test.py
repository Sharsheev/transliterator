import unittest

from calc import add, subtract, multiply, divide


class TestAddFunc(unittest.TestCase):
    """
    calc модулундагы add функциясын текшерүү
    """

    def test_add_integers(self):
        """
        Эки бүтүн санды кошкондо суммасы туура чыгаарын текшерүү
        """
        result = add(3, 2)
        self.assertEqual(result, 5)

    def test_add_floats(self):
        """
        Эки чыныгы сандын суммасы туура чыгаарын текшерүү
        """
        result = add(10.5, 6)
        self.assertEqual(result, 16.5)

    def test_add_strings(self):
        """
        Эки саптык маанини кошкондо бир чапталган саптык маани чыгат
        """
        result = add('абв', 'өңү')
        self.assertEqual(result, 'абвөңү')


if __name__ == '__main__':
    unittest.main()
