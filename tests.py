import unittest
from shop_functions import (running_total, resettotal,
                            clean_string, calculate_totals, PRICES,
                            BULK_CHERRY_DISCOUNT, count_cherries
                            )

class test_shop(unittest.TestCase):
    def setUp(self):
        resettotal()

    def test_buy_one_apple(self):
        self.assertEqual('apples : 100', running_total('apples'))

    def test_buy_one_apple_total(self):
        self.assertEqual(PRICES['apples'], calculate_totals('apples'))

    def test_buy_two_apple(self):
        self.assertEqual(PRICES['apples'], calculate_totals('apples'))
        self.assertEqual(2 * PRICES['apples'], calculate_totals('apples'))

    def test_acceptance_test1(self):
        self.assertEqual(PRICES['apples'], calculate_totals('apples'))
        self.assertEqual(PRICES['apples']+
                         PRICES['cherries'], calculate_totals('cherries'))

        self.assertEqual(
                         PRICES['apples']+
                         PRICES['cherries']+
                         PRICES['cherries']-
                         BULK_CHERRY_DISCOUNT, calculate_totals('cherries'))

    def test_acceptance_test_2_with_four_cherries(self):
        '''
        new client requiremnt: buy 2 sets of cherries &
        get a discount of 20p
        '''
        self.assertEqual(PRICES['apples'],   calculate_totals('apples'))
        self.assertEqual(PRICES['apples']+
                         PRICES['cherries'], calculate_totals('cherries'))
        self.assertEqual(
            PRICES['apples']+
            PRICES['cherries']+
            PRICES['cherries']-
            BULK_CHERRY_DISCOUNT, calculate_totals('cherries'))
        self.assertEqual(
            PRICES['apples'] +
            PRICES['cherries'] +
            PRICES['cherries'] +
            PRICES['cherries'] -
            BULK_CHERRY_DISCOUNT, calculate_totals('cherries'))
        self.assertEqual(
            PRICES['apples'] +
            PRICES['cherries'] +
            PRICES['cherries'] +
            -BULK_CHERRY_DISCOUNT+
            PRICES['cherries'] +
            PRICES['cherries'] -
            BULK_CHERRY_DISCOUNT

            , calculate_totals('cherries'))

    def test_non_inventory_item(self):
        self.assertEqual('pineapple : 0', running_total('pineapple'))

    def test_acceptance_test_3_banana_buy_one_get_one_free(self):
        '''
        we now have a special offer on bananas,
        buy one get one free
        '''
        self.assertEqual(calculate_totals('bananas'),PRICES['bananas'] )
        self.assertEqual(calculate_totals('bananas'),PRICES['bananas'] )
        self.assertEqual(calculate_totals('bananas'),PRICES['bananas']+PRICES['bananas'] )
        self.assertEqual(calculate_totals('bananas'),PRICES['bananas']+PRICES['bananas'] )

    def test_csv_input(self):
        '''
        We want to accept a list of items as well as singularly
        '''
        self.assertEqual(calculate_totals('apples,cherries,bananas'),
                         PRICES['apples']+PRICES['cherries']+PRICES['bananas'])

    def test_dirty_csv_input1(self):
        self.assertEqual(calculate_totals('apples, cherries, bananas'),
                         PRICES['apples']+PRICES['cherries']+PRICES['bananas'])
    def test_dirty_csv_input2(self):
        self.assertEqual(calculate_totals('Apples,Cherries,Bananas'),
                         PRICES['apples']+PRICES['cherries']+PRICES['bananas'])
    def test_dirty_csv_input3(self):
        self.assertEqual(calculate_totals('Apples, Cherries, Bananas'),
                         PRICES['apples']+PRICES['cherries']+PRICES['bananas'])
    def test_dirty_csv_input4(self):
        self.assertEqual(calculate_totals('Cherries,Cherries'),
                         PRICES['cherries']+PRICES['cherries']-BULK_CHERRY_DISCOUNT)
    def test_dirty_csv_input5(self):
        self.assertEqual(calculate_totals('Cherries, Cherries'),
                         PRICES['cherries']+PRICES['cherries']-BULK_CHERRY_DISCOUNT)

    def test_allow_pommes(self):
        self.assertEqual(calculate_totals('pommes'),PRICES['pommes'])

    def test_allow_mele(self):
        self.assertEqual(calculate_totals('mele'),PRICES['mele'])

    def acceptance_test_4(self):
        self.assertEqual(calculate_totals('cherries'),
                         PRICES['cherries'])
        self.assertEqual(calculate_totals('pommes'),
                         PRICES['cherries']+ PRICES['pommes'])
        self.assertEqual(calculate_totals('cherries'),
                         PRICES['cherries']+
                         PRICES['pommes']  +
                         PRICES['cherries']-
                         BULK_CHERRY_DISCOUNT)
        self.assertEqual(calculate_totals('bananas'),'bananas : 380')
        self.assertEqual(calculate_totals('bananas'),'bananas : 380')
        self.assertEqual(calculate_totals('apples'),'apples : 480')

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

    def test_cherry_count_function(self):
        purchases = ['cherries']
        self.assertEqual(count_cherries(purchases),1)
        purchases = ['cherries'] * 4
        self.assertEqual(count_cherries(purchases),4)
        purchases = ['cherries'] * 41
        self.assertEqual(count_cherries(purchases),41)

