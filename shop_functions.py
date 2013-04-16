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
    r = 0
    if is_div_by_four(total_apples_by_any_name):
        r = r-100
    if is_div_by_five(sum([no_cherries, no_bananas, total_apples_by_any_name])):
        r = r -200
    return r


def add_to_running_total(bought_item,four_apple_discount=False):
    global total
    if bought_item in PRICES:
        total += PRICES[bought_item]
        total += apply_discount(bought_item)
        if four_apple_discount:
            total += four_apples_discount(bought_item)
    return bought_item, total

def clean_string(input_string):
    return input_string.lower().strip()


def calculate_totals(bought_item, four_apple_discount=False):
    global total, no_cherries
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
    global total, no_pommes, no_bananas, no_mele, no_cherries,no_apples
    total, no_pommes, no_bananas, no_mele, no_cherries, no_apples= 0,0,0,0,0,0