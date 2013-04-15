import unittest
from shop_functions import running_total, resettotal, clean_string

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

    def test_banana_buy_one_get_one_free(self):
        self.assertEqual(running_total('bananas'),'bananas : 150' )
        self.assertEqual(running_total('bananas'),'bananas : 150' )
        self.assertEqual(running_total('bananas'),'bananas : 300' )
        self.assertEqual(running_total('bananas'),'bananas : 300' )

    def test_csv_input(self):
        self.assertEqual(running_total('apples,cherries,bananas'),'apples,cherries,bananas : 325')

    def test_dirty_csv_input(self):
        # self.assertEqual(running_total('apples, cherries, bananas'),'apples, cherries, bananas : 325')
        # self.assertEqual(running_total('Apple,Cherries,Bananas'),325)
        # self.assertEqual(running_total('Apple, Cherries, Bananas'),325)
        # self.assertEqual(running_total('Cherries,Cherries'), 130)
        # self.assertEqual(running_total('Cherries, Cherries'), 130)
        # self.assertEqual(running_total('cherries,cherries'), 130)
        # self.assertEqual(running_total('cherries, cherries'), 130)
        pass

    def test_allow_pommes(self):
        self.assertEqual(running_total('pommes'),'pommes : 100')

    def test_allow_mele(self):
        self.assertEqual(running_total('mele'),'mele : 100')

    def acceptance_test_2(self):
        self.assertEqual(running_total('cherries'),'cherries : 75')
        self.assertEqual(running_total('pommes'),'pommes : 175')
        self.assertEqual(running_total('cherries'),'cherries : 230')
        self.assertEqual(running_total('bananas'),'bananas : 380')
        self.assertEqual(running_total('bananas'),'bananas : 380')
        self.assertEqual(running_total('apples'),'apples : 480')

    def test_string_cleaner(self):
        self.assertEqual(clean_string(' aaa '),'aaa')
        self.assertEqual(clean_string(' Aaa '),'aaa')
        self.assertEqual(clean_string(' Aaa B '),'aaa b')

    def test_iteration_5_acceptance_test(self):
        self.assertEqual(running_total('mele'),'mele : 100')
        self.assertEqual(running_total('pommes'),'pommes : 200')
        self.assertEqual(running_total('pommes'),'pommes : 300')
        self.assertEqual(running_total('apples'),'apples : 400')
        self.assertEqual(running_total('pommes'),'pommes : 400')
        self.assertEqual(running_total('mele'),'mele : 450')
        self.assertEqual(running_total('cherries'),'cherries : 525')
        self.assertEqual(running_total('cherries'),'cherries : 580')
