import unittest
from shop_functions import running_total, resettotal

class test_shop(unittest.TestCase):
    def setUp(self):
        resettotal()

    def test_buy_one_apple(self):
        self.assertEqual('apples : 100', running_total('apples'))

    def test_buy_two_apple(self):
        self.assertEqual('apples : 100', running_total('apples'))
        self.assertEqual('apples : 200', running_total('apples'))

    def test_acceptance(self):
        self.assertEqual('apples : 100',   running_total('apples'))
        self.assertEqual('cherries : 175', running_total('cherries'))
        self.assertEqual('cherries : 230', running_total('cherries'))

    def test_acceptance_with_four_cherries(self):
        self.assertEqual('apples : 100',   running_total('apples'))
        self.assertEqual('cherries : 175', running_total('cherries'))
        self.assertEqual('cherries : 230', running_total('cherries'))
        self.assertEqual('cherries : 305', running_total('cherries'))
        self.assertEqual('cherries : 360', running_total('cherries'))

    def test_non_inventory_item(self):
        self.assertEqual('apple : 0', running_total('apple'))
