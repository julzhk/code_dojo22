import unittest
from shop_functions import running_total, resettotal

class test_shop(unittest.TestCase):
    def setUp(self):
        resettotal()

    def test_buy_one_apple(self):
        self.assertEqual(running_total('apples'),'apples : 100')

    def test_buy_two_apple(self):
        self.assertEqual(running_total('apples'),'apples : 100')
        self.assertEqual(running_total('apples'),'apples : 200')

    def test_acceptance(self):
        self.assertEqual(running_total('apples'),'apples : 100')
        self.assertEqual(running_total('cherries'),'cherries : 175')
        self.assertEqual(running_total('cherries'),'cherries : 250')
