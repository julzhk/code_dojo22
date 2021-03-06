BUY_ANY_FIVE_ITEMS_DISCOUNT = 200
BUY_FOUR_APPLES_BY_ANY_NAME_DISCOUNT = 100
BUY_TWO_MELE_DISCOUNT = 50
BUY_THREE_POMMES_DISCOUNT = 100
PRICE_OF_APPLES = 100
BULK_CHERRY_DISCOUNT = 20
PRICES = {
    'apples': PRICE_OF_APPLES,
    'pommes': PRICE_OF_APPLES,
    'mele': PRICE_OF_APPLES,
    'bananas':150,
    'cherries':75
}
purchases = []
total = 0


def is_multiple(val,divisor):
    return val is not 0 and val % divisor == 0

def is_even(n):
    return is_multiple(n,2)

def is_div_by_three(n):
    return is_multiple(n,3)

def is_div_by_four(n):
    return is_multiple(n,4)

def is_div_by_five(n):
    return is_multiple(n,5)

def count_items(purchases,count_item):
    return sum([1 for item in purchases if item == count_item])

def count_cherries(purchases):
    return count_items(purchases,'cherries')

def count_bananas(purchases):
    return count_items(purchases,'bananas')


def apply_discount(purchases):
    '''
    for every second bag of cherries, give a special 20p discount
    '''
    most_recent_purchase = purchases[-1]
    if most_recent_purchase == 'cherries':
        if is_even(count_cherries(purchases)):
            return -BULK_CHERRY_DISCOUNT
    if most_recent_purchase == 'bananas':
        if is_even(count_bananas(purchases)):
            return -PRICES['bananas']
    if most_recent_purchase == 'pommes':
        if is_div_by_three(count_items(purchases,'pommes')):
            return -BUY_THREE_POMMES_DISCOUNT
    if most_recent_purchase == 'mele':
        if is_even(count_items(purchases,'mele')):
            return -BUY_TWO_MELE_DISCOUNT
    return 0

def four_apples_discount(purchases):
    total_apples_by_any_name = count_items(purchases,'pommes')+\
                               count_items(purchases,'mele')+\
                               count_items(purchases,'apples')
    r = 0
    if is_div_by_four(total_apples_by_any_name):
        r = r- BUY_FOUR_APPLES_BY_ANY_NAME_DISCOUNT
    if is_div_by_five(len(purchases)):
        r = r - BUY_ANY_FIVE_ITEMS_DISCOUNT
    return r


def add_to_running_total(bought_item,four_apple_discount=False):
    global total, purchases
    if bought_item in PRICES:
        total += PRICES[bought_item]
        purchases.append(bought_item)
        total += apply_discount(purchases)
        if four_apple_discount:
            total += four_apples_discount(purchases)
    return bought_item, total

def clean_string(input_string):
    return input_string.lower().strip()


def calculate_totals(bought_item, four_apple_discount=False):
    global total
    if ',' in bought_item:
        productlist = bought_item.split(',')
        [add_to_running_total(clean_string(product), four_apple_discount=four_apple_discount) for product in
         productlist]
    else:
        bought_item, total = add_to_running_total(bought_item, four_apple_discount=four_apple_discount)
    return total


def running_total(bought_item,four_apple_discount=False):
    total = calculate_totals(bought_item, four_apple_discount)
    return '%s : %s' % (bought_item, total)

def resettotal():
    global total, purchases
    total= 0
    purchases = []