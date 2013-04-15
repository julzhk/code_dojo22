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
        self.assertEqual('cherries : 220', running_total('cherries'))

    def test_acceptance_with_four_cherries(self):
        self.assertEqual('apples : 100',   running_total('apples'))
        self.assertEqual('cherries : 175', running_total('cherries'))
        self.assertEqual('cherries : 220', running_total('cherries'))
        self.assertEqual('cherries : 295', running_total('cherries'))
        self.assertEqual('cherries : 340', running_total('cherries'))

    def test_non_inventory_item(self):
        self.assertEqual('apple : 0', running_total('apple'))

    def test_banana_buy_one_get_one_free(self):
        self.assertEqual(running_total('bananas'),'bananas : 150' )
        self.assertEqual(running_total('bananas'),'bananas : 150' )
        self.assertEqual(running_total('bananas'),'bananas : 300' )
        self.assertEqual(running_total('bananas'),'bananas : 300' )

    def test_csv_input(self):
        self.assertEqual(running_total('apples,cherries,bananas'),'apples,cherries,bananas : 325')
        # self.assertEqual(running_total('apple, cherries, bananas'),325)
        # self.assertEqual(running_total('Apple,Cherries,Bananas'),325)
        # self.assertEqual(running_total('Apple, Cherries, Bananas'),325)
        # self.assertEqual(running_total('Cherries,Cherries'), 130)
        # self.assertEqual(running_total('Cherries, Cherries'), 130)
        # self.assertEqual(running_total('cherries,cherries'), 130)
        # self.assertEqual(running_total('cherries, cherries'), 130)
        pass
