BULK_CHERRY_DISCOUNT = 20
PRICES = {
    'apples':100,
    'bananas':150,
    'cherries':75
}
total = 0
no_cherries = 0

def is_even(n):
    return n % 2 == 0


def apply_discount(s):
    '''
    for every second bag of cherries, give a special 20p discount
    '''
    global no_cherries
    if s == 'cherries':
        no_cherries += 1
        if is_even(no_cherries):
            return -BULK_CHERRY_DISCOUNT
    return 0


def running_total(s):
    global total, no_cherries
    if s in PRICES:
        total += PRICES[s]
        total += apply_discount(s)
    return '%s : %s' % (s, total)

def resettotal():
    global total
    total = 0