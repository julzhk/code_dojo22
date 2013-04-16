PRICE_OF_APPLES = 100
BULK_CHERRY_DISCOUNT = 20
PRICES = {
    'apples': PRICE_OF_APPLES,
    'pommes': PRICE_OF_APPLES,
    'mele': PRICE_OF_APPLES,
    'bananas':150,
    'cherries':75
}
total = 0
no_cherries = 0
no_bananas = 0
no_pommes = 0
no_mele = 0
no_apples = 0


def is_even(n):
    return n % 2 == 0

def is_div_by_three(n):
    return n % 3 == 0

def is_div_by_four(n):
    return n is not 0 and n % 4 == 0


def apply_discount(s):
    '''
    for every second bag of cherries, give a special 20p discount
    '''
    global no_cherries, no_bananas, no_pommes, no_mele, no_apples
    if s == 'apples':
        no_apples += 1
    if s == 'cherries':
        no_cherries += 1
        if is_even(no_cherries):
            return -BULK_CHERRY_DISCOUNT
    if s == 'bananas':
        no_bananas  += 1
        if is_even(no_bananas):
            return -PRICES['bananas']
    if s == 'pommes':
        no_pommes += 1
        if is_div_by_three(no_pommes):
            return -100
    if s == 'mele':
        no_mele += 1
        if is_even(no_mele):
            return -50
    return 0

def four_apples_discount(s):
    global no_cherries, no_bananas, no_pommes, no_mele, no_apples
    total_apples_by_any_name = no_pommes + no_mele + no_apples
    if is_div_by_four(total_apples_by_any_name):
        return -100
    return 0



def add_to_running_total(bought_item):
    global total
    if bought_item in PRICES:
        total += PRICES[bought_item]
        total += apply_discount(bought_item)
        # total += four_apples_discount(bought_item)
    return '%s : %s' % (bought_item, total)

def clean_string(input_string):
    return input_string.lower().strip()

def running_total(bought_item):
    global total, no_cherries
    if ',' in bought_item:
        productlist = bought_item.split(',')
        [add_to_running_total(clean_string(product)) for product in productlist]
        return '%s : %s' % (bought_item, total)

    else:
        return add_to_running_total(bought_item)

def resettotal():
    global total, no_pommes, no_bananas, no_mele, no_cherries,no_apples
    total, no_pommes, no_bananas, no_mele, no_cherries, no_apples= 0,0,0,0,0,0