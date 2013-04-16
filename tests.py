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

    def test_acceptance_test1(self):
        self.assertEqual('apples : 100',   running_total('apples'))
        self.assertEqual('cherries : 175', running_total('cherries'))
        self.assertEqual('cherries : 230', running_total('cherries'))

    def test_acceptance_test_2_with_four_cherries(self):
        '''
        new client requiremnt: buy 2 sets of cherries &
        get a discount of 20p
        '''
        self.assertEqual('apples : 100',   running_total('apples'))
        self.assertEqual('cherries : 175', running_total('cherries'))
        self.assertEqual('cherries : 230', running_total('cherries'))
        self.assertEqual('cherries : 305', running_total('cherries'))
        self.assertEqual('cherries : 360', running_total('cherries'))

    def test_non_inventory_item(self):
        self.assertEqual('apple : 0', running_total('apple'))

    def test_acceptance_test_3_banana_buy_one_get_one_free(self):
        '''
        we now have a special offer on bananas,
        buy one get one free
        '''
        self.assertEqual(running_total('bananas'),'bananas : 150' )
        self.assertEqual(running_total('bananas'),'bananas : 150' )
        self.assertEqual(running_total('bananas'),'bananas : 300' )
        self.assertEqual(running_total('bananas'),'bananas : 300' )

    def test_csv_input(self):
        '''
        We want to accept a list of items as well as singularly
        '''
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

    def acceptance_test_4(self):
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
        '''
        Special discounts for apples in some regions
        '''
        self.assertEqual(running_total('mele'),'mele : 100')
        self.assertEqual(running_total('pommes'),'pommes : 200')
        self.assertEqual(running_total('pommes'),'pommes : 300')
        self.assertEqual(running_total('apples'),'apples : 400')
        self.assertEqual(running_total('pommes'),'pommes : 400')
        self.assertEqual(running_total('mele'),'mele : 450')
        self.assertEqual(running_total('cherries'),'cherries : 525')
        self.assertEqual(running_total('cherries'),'cherries : 580')


    def test_iteration_6a_acceptance_test(self):
        # client requiremnt:
        # 4 apples ( with any name) get a discount of -100
        # and 5 item get a discount -200
        self.assertEqual(running_total('mele,pommes,pommes,mele',
                                       four_apple_discount=True),
                         'mele,pommes,pommes,mele : 250')
    def test_iteration_6b_acceptance_test(self):
        # client requiremnt:
        # 4 apples ( with any name) get a discount of -100
        # and 5 item get a discount -200
        self.assertEqual(running_total('mele,pommes,pommes,mele,apples',
                                       four_apple_discount=True),
                         'mele,pommes,pommes,mele,apples : 150')



