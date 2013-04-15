PRICES = {
    'apples':100,
    'bananas':150,
    'cherries':75
}
total = 0
no_cherries = 0
def is_even(n):
    return n % 2 == 0

def running_total(s):
    global total, no_cherries
    if s in PRICES:
        total += PRICES[s]
        if s == 'cherries':
            no_cherries +=1
            if is_even(no_cherries):
                total -= 20

    return '%s : %s' % (s, total)

def resettotal():
    global total
    total = 0